import time
import unittest
from unittest.mock import MagicMock, patch

from Libs.rapidapi_quota import format_quota, quota_warning_kind
import TiktokStreamKeyGenerator as app_module


class _FakeBar:
    def __init__(self):
        self.range = None
        self.value = None
        self.format_text = None
        self.style = None
        self.tooltip = None

    def setRange(self, minimum, maximum):
        self.range = (minimum, maximum)

    def setValue(self, value):
        self.value = value

    def setFormat(self, text):
        self.format_text = text

    def setStyleSheet(self, style):
        self.style = style

    def setToolTip(self, text):
        self.tooltip = text


class RapidApiQuotaTests(unittest.TestCase):
    def test_quota_warning_kind_states(self):
        now = 1_700_000_000
        future_reset = "3600"

        self.assertEqual(quota_warning_kind({}, now=now), "")
        self.assertEqual(
            quota_warning_kind({"limit": "10000", "remaining": "5000", "reset": future_reset, "updated": str(now)}, now=now),
            "",
        )
        self.assertEqual(
            quota_warning_kind({"limit": "10000", "remaining": "1000", "reset": future_reset, "updated": str(now)}, now=now),
            "low",
        )
        self.assertEqual(
            quota_warning_kind({"limit": "10000", "remaining": "0", "reset": future_reset, "updated": str(now)}, now=now),
            "exhausted",
        )
        self.assertEqual(
            quota_warning_kind({"limit": "10000", "used": "10000", "reset": future_reset, "updated": str(now)}, now=now),
            "exhausted",
        )

    def test_quota_warning_kind_ignores_stale_past_reset(self):
        now = 1_700_000_000
        stale = {"limit": "10000", "remaining": "0", "reset": "60", "updated": str(now - 120)}
        self.assertEqual(quota_warning_kind(stale, now=now), "")

    def test_update_rapidapi_quota_display_shows_reset_date_in_bar(self):
        now = int(time.time())
        snapshot = {"limit": "10000", "remaining": "9437", "reset": "86400", "updated": str(now)}
        window = app_module.StreamKeyGeneratorWindow.__new__(app_module.StreamKeyGeneratorWindow)
        window.rapidapi_quota_bar = _FakeBar()

        with patch.object(app_module, "read_quota", return_value=snapshot):
            window.update_rapidapi_quota_display()

        self.assertEqual(window.rapidapi_quota_bar.range, (0, 10000))
        self.assertEqual(window.rapidapi_quota_bar.value, 9437)
        self.assertEqual(window.rapidapi_quota_bar.format_text, format_quota(snapshot))
        self.assertIn("resets ", window.rapidapi_quota_bar.format_text)

    def test_confirm_low_rapidapi_quota_skips_when_unknown(self):
        window = app_module.StreamKeyGeneratorWindow.__new__(app_module.StreamKeyGeneratorWindow)

        with patch.object(app_module, "read_quota", return_value={}), \
             patch.object(app_module, "QMessageBox") as mock_box:
            self.assertTrue(window.confirm_low_rapidapi_quota())
            mock_box.assert_not_called()

    def test_confirm_low_rapidapi_quota_prompts_and_respects_choice(self):
        now = int(time.time())
        low_snapshot = {"limit": "10000", "remaining": "500", "reset": "86400", "updated": str(now)}
        window = app_module.StreamKeyGeneratorWindow.__new__(app_module.StreamKeyGeneratorWindow)

        continue_btn = object()
        cancel_btn = object()
        dialog = MagicMock()
        dialog.addButton.side_effect = [continue_btn, cancel_btn]
        dialog.clickedButton.return_value = cancel_btn

        with patch.object(app_module, "read_quota", return_value=low_snapshot), \
             patch.object(app_module, "QMessageBox", return_value=dialog):
            self.assertFalse(window.confirm_low_rapidapi_quota())

        dialog2 = MagicMock()
        dialog2.addButton.side_effect = [continue_btn, cancel_btn]
        dialog2.clickedButton.return_value = continue_btn
        with patch.object(app_module, "read_quota", return_value=low_snapshot), \
             patch.object(app_module, "QMessageBox", return_value=dialog2):
            self.assertTrue(window.confirm_low_rapidapi_quota())


if __name__ == "__main__":
    unittest.main()
