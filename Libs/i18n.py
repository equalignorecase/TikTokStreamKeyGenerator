"""Lightweight UI translation helpers for English and Thai."""

SUPPORTED_LANGUAGES = ("en", "th")
LANGUAGE_OPTIONS = (
    ("en", "English"),
    ("th", "ไทย"),
)

TRANSLATIONS = {
    # Header & navigation
    "menu.account": {"en": "Account", "th": "บัญชี"},
    "menu.views": {"en": "Views", "th": "มุมมอง"},
    "button.settings": {"en": "Settings", "th": "ตั้งค่า"},
    "summary.no_account": {"en": "No account loaded", "th": "ยังไม่ได้โหลดบัญชี"},
    "tab.live": {"en": "Stream", "th": "สตรีม"},
    "tab.stats": {"en": "Stats", "th": "สถิติ"},
    "tab.audience": {"en": "Audience", "th": "ผู้ชม"},
    "tab.safety": {"en": "Safety", "th": "ความปลอดภัย"},
    "tab.chat": {"en": "Chat", "th": "แชท"},

    # Stream setup
    "label.title": {"en": "Title:", "th": "ชื่อไลฟ์:"},
    "label.topic": {"en": "Topic:", "th": "หัวข้อ:"},
    "label.game": {"en": "Game:", "th": "เกม:"},
    "label.client_mode": {"en": "Client mode:", "th": "โหมดไคลเอนต์:"},
    "label.region": {"en": "Region:", "th": "ภูมิภาค:"},
    "placeholder.region": {"en": "Auto (detected region)", "th": "อัตโนมัติ (ตรวจจับภูมิภาค)"},
    "tooltip.device_settings": {"en": "Device settings", "th": "ตั้งค่าอุปกรณ์"},
    "button.retry_device_setup": {"en": "Retry device setup", "th": "ลองตั้งค่าอุปกรณ์ใหม่"},
    "button.details": {"en": "Details", "th": "รายละเอียด"},

    # Primary live controls
    "button.go_live": {"en": "Go Live", "th": "เริ่มไลฟ์"},
    "button.pause": {"en": "Pause", "th": "พัก"},
    "button.resume": {"en": "Resume", "th": "ทำต่อ"},
    "button.end_live": {"en": "End Live", "th": "จบไลฟ์"},
    "button.login": {"en": "Login", "th": "เข้าสู่ระบบ"},

    # Account panel
    "label.cookies_json": {"en": "Cookies JSON", "th": "ไฟล์ Cookies JSON"},
    "button.browse": {"en": "Browse", "th": "เลือกไฟล์"},
    "button.import_studio": {"en": "Import from LIVE Studio…", "th": "นำเข้าจาก LIVE Studio…"},
    "label.rapidapi_key": {"en": "RapidAPI Key", "th": "คีย์ RapidAPI"},
    "placeholder.rapidapi_key": {"en": "Paste your RapidAPI key", "th": "วางคีย์ RapidAPI ของคุณ"},
    "label.rapidapi_quota": {"en": "RapidAPI Quota", "th": "โควตา RapidAPI"},
    "button.refresh_account": {"en": "Refresh Account Info", "th": "รีเฟรชข้อมูลบัญชี"},
    "button.campaigns": {"en": "LIVE Campaigns", "th": "แคมเปญ LIVE"},

    # Menus
    "action.qr_login": {"en": "Log in with QR code", "th": "เข้าสู่ระบบด้วย QR code"},
    "action.import_cookies": {"en": "Import cookies…", "th": "นำเข้า cookies…"},
    "action.refresh_account": {"en": "Refresh account", "th": "รีเฟรชบัญชี"},
    "action.campaigns": {"en": "LIVE campaigns…", "th": "แคมเปญ LIVE…"},
    "action.account_settings": {"en": "Account settings…", "th": "ตั้งค่าบัญชี…"},
    "action.support_dev": {"en": "Support development", "th": "สนับสนุนผู้พัฒนา"},
    "action.restore_views": {"en": "Restore default views", "th": "คืนค่ามุมมองเริ่มต้น"},
    "action.device_settings": {"en": "Device settings…", "th": "ตั้งค่าอุปกรณ์…"},
    "action.stream_settings": {"en": "Stream settings…", "th": "ตั้งค่าสตรีม…"},
    "action.save_settings": {"en": "Save settings", "th": "บันทึกการตั้งค่า"},
    "action.refresh_stats": {"en": "Refresh stats", "th": "รีเฟรชสถิติ"},
    "action.refresh_safety": {"en": "Refresh audience / safety", "th": "รีเฟรชผู้ชม / ความปลอดภัย"},

    # Settings dialog
    "settings.title": {"en": "Settings", "th": "ตั้งค่า"},
    "settings.tab.account": {"en": "Account", "th": "บัญชี"},
    "settings.tab.stream": {"en": "Stream", "th": "สตรีม"},
    "settings.tab.comments": {"en": "Comments", "th": "คอมเมนต์"},
    "settings.footer_note": {
        "en": "Settings are saved when you close this window.",
        "th": "การตั้งค่าจะถูกบันทึกเมื่อปิดหน้าต่างนี้",
    },
    "settings.done": {"en": "Done", "th": "เสร็จสิ้น"},
    "settings.options": {"en": "Options:", "th": "ตัวเลือก:"},
    "settings.language": {"en": "Language:", "th": "ภาษา:"},
    "settings.generate_replay": {"en": "Generate Replay", "th": "สร้างรีเพลย์หลังจบไลฟ์"},
    "settings.age_restricted": {"en": "Age Restricted", "th": "จำกัดอายุผู้ชม"},
    "settings.close_room": {"en": "Close Room When Close Stream", "th": "ปิดห้องอัตโนมัติเมื่อหยุดสตรีม"},
    "settings.dual_layout": {"en": "Dual Layout (Portrait + Landscape)", "th": "ไลฟ์สองแนวพร้อมกัน (แนวตั้ง + แนวนอน)"},
    "settings.chat_sound": {"en": "Chat notification sound", "th": "เสียงแจ้งเตือนแชท"},
    "settings.allow_gifts": {"en": "Allow gifts", "th": "อนุญาตส่งของขวัญ"},
    "settings.allow_comments": {"en": "Allow comments", "th": "อนุญาตคอมเมนต์"},
    "settings.content_disclosure": {"en": "Content disclosure:", "th": "การเปิดเผยเนื้อหาโฆษณา:"},

    # Comment preferences
    "comments.note": {
        "en": "Saved for new LIVE rooms. Use Manage LIVE to change an existing room.",
        "th": "บันทึกไว้สำหรับห้อง LIVE ใหม่ หากต้องการแก้ห้องที่กำลังไลฟ์อยู่ให้ใช้ Manage LIVE",
    },
    "comments.filter_unkind": {"en": "Filter potentially unkind comments", "th": "กรองคอมเมนต์ที่อาจไม่สุภาพ"},
    "comments.subscriber_only": {"en": "Subscriber / Super Fans-only chat", "th": "แชทเฉพาะสมาชิก / Super Fans"},
    "comments.star_comments": {"en": "Star Comments:", "th": "Star Comments:"},
    "comments.additional_filters": {"en": "Additional Android filters:", "th": "ตัวกรองเพิ่มเติมสำหรับ Android:"},
    "comments.filter_spam": {"en": "Filter spam comments", "th": "กรองคอมเมนต์สแปม"},
    "comments.filter_flagged": {"en": "Filter community-flagged comments", "th": "กรองคอมเมนต์ที่ถูกรายงาน"},
    "comments.review_flagged": {"en": "Review community-flagged comments", "th": "ตรวจสอบคอมเมนต์ที่ถูกรายงาน"},
    "comments.manage_live": {"en": "Manage current LIVE / account tools", "th": "จัดการ LIVE ปัจจุบัน / เครื่องมือบัญชี"},

    # Realtime chat activity events
    "chat.joined": {"en": "joined", "th": "เข้าร่วม"},
    "chat.followed": {"en": "followed", "th": "ติดตามแล้ว"},
    "chat.shared": {"en": "shared the LIVE", "th": "แชร์ไลฟ์"},
    "chat.liked": {"en": "liked ×{count}", "th": "กดถูกใจ ×{count}"},
}


def normalize_language(value) -> str:
    """Return a supported language code ('en' or 'th'), defaulting to 'en'."""
    code = str(value or "").strip().lower()
    if code.startswith("th"):
        return "th"
    return "en"


def tr(key: str, lang: str = "en", **kwargs) -> str:
    """Translate `key` into `lang` ('en' or 'th'), falling back to English."""
    normalized = normalize_language(lang)
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key.format(**kwargs) if kwargs else key
    template = entry.get(normalized) or entry.get("en") or key
    return template.format(**kwargs) if kwargs else template
