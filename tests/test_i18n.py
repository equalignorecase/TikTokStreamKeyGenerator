import json
import os
import tempfile
import unittest
from unittest.mock import patch

from PySide6.QtWidgets import QApplication

from Libs.i18n import TRANSLATIONS, normalize_language, tr
import TiktokStreamKeyGenerator as app_module


class I18nTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._app = QApplication.instance() or QApplication([])

    def test_normalize_language_and_tr(self):
        self.assertEqual(normalize_language("th"), "th")
        self.assertEqual(normalize_language("th-TH"), "th")
        self.assertEqual(normalize_language("en"), "en")
        self.assertEqual(normalize_language(None), "en")
        self.assertEqual(normalize_language("fr"), "en")

        self.assertEqual(tr("button.go_live", "en"), "Go Live")
        self.assertEqual(tr("button.go_live", "th"), "เริ่มไลฟ์")
        self.assertEqual(tr("missing.key", "th"), "missing.key")

        for key, entry in TRANSLATIONS.items():
            self.assertIn("en", entry, f"Missing English translation for {key}")
            self.assertIn("th", entry, f"Missing Thai translation for {key}")

    def test_window_language_switch_and_persistence(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cfg_path = os.path.join(tmpdir, "config.json")
            with patch.object(app_module, "CONFIG_PATH", cfg_path), \
                 patch.object(app_module.StreamKeyGeneratorWindow, "start_device_initialization"), \
                 patch.object(app_module.StreamKeyGeneratorWindow, "refresh_account_info"):
                window = app_module.StreamKeyGeneratorWindow()
                try:
                    self.assertEqual(window.ui_language, "en")
                    self.assertEqual(window.go_live_button.text(), "Go Live")

                    idx = window.ui_language_combo.findData("th")
                    self.assertGreaterEqual(idx, 0)
                    window.ui_language_combo.setCurrentIndex(idx)

                    self.assertEqual(window.ui_language, "th")
                    self.assertEqual(window.go_live_button.text(), tr("button.go_live", "th"))
                    self.assertEqual(window.settings_button.text(), tr("button.settings", "th"))
                    self.assertEqual(window.settings_dialog.windowTitle(), tr("settings.title", "th"))

                    window.save_config(show_message=False)
                    with open(cfg_path, "r", encoding="utf-8") as fh:
                        saved = json.load(fh)
                    self.assertEqual(saved.get("ui_language"), "th")

                    window.apply_ui_language("en")
                    self.assertEqual(window.go_live_button.text(), "Go Live")

                    window.load_config()
                    self.assertEqual(window.ui_language, "th")
                    self.assertEqual(window.go_live_button.text(), tr("button.go_live", "th"))
                finally:
                    window.close()


if __name__ == "__main__":
    unittest.main()
