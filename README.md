# TikTok Live Stream Key Generator for OBS Studio (Thai Edition)

เวอร์ชันปรับแต่งจากโปรเจกต์ต้นฉบับสำหรับสร้างห้อง TikTok LIVE และเชื่อมต่อกับ OBS Studio ผ่าน local FFmpeg RTMP proxy พร้อมใส่ stream metadata ที่ TikTok ต้องการให้อัตโนมัติ

- **Repository:** [equalignorecase/TikTokStreamKeyGenerator](https://github.com/equalignorecase/TikTokStreamKeyGenerator)
- **ต้นฉบับและลิขสิทธิ์ (Upstream Credit):** พัฒนาต่อยอดจาก [Loukious/TikTokStreamKeyGenerator](https://github.com/Loukious/TikTokStreamKeyGenerator) โดยลิขสิทธิ์โค้ดต้นฉบับและสิทธิ์ในบริการ RapidAPI Signer ยังคงเป็นของเจ้าของเดิม ([Loukious](https://github.com/Loukious))

---

## สิ่งที่ปรับปรุงในเวอร์ชันนี้

- **รองรับภาษาไทยใน UI:** สลับภาษา `English` / `ไทย` ได้จาก `Settings → Stream → Language` และบันทึกค่าลง `config.json`
- **จัดการโควตา RapidAPI ชัดเจนขึ้น:** แสดงวันรีเซ็ตบนแถบ `RapidAPI Quota` โดยตรง และแจ้งเตือนยืนยันก่อนกด **Go Live** เมื่อโควตาเหลือ `<= 10%` หรือหมดแล้ว
- **ประหยัดโควตาขณะไลฟ์:** ปรับลดความถี่ polling ของสถิติและ audience safety เพื่อยืดชั่วโมงการไลฟ์ให้ใช้งานได้นานขึ้น
- **UI สไตล์ Neutral Obsidian / Slate:** ปรับโทนสีพื้นหลัง ขอบการ์ด ระยะห่าง และเปลี่ยนหน้า **Realtime Stats** เป็น KPI Cards
- **อัปเดตจาก Repository ของตัวเอง:** เปลี่ยน `VersionChecker` ไปที่ `equalignorecase/TikTokStreamKeyGenerator` และนำหน้าต่างแจ้งเตือนโดเนทออก

---

## ความสามารถหลัก

- สร้างห้อง TikTok LIVE และรับ Stream URL / Stream Key สำหรับใช้งานกับ OBS Studio
- รัน local FFmpeg RTMP proxy ระหว่าง OBS กับ TikTok เพื่อแนบ SEI / stream metadata
- รองรับทั้งโหมด **PC (LIVE Studio)** และ **Android** รวมถึง **Dual Layout (แนวตั้ง + แนวนอน)** สำหรับบัญชีที่ได้รับสิทธิ์
- อ่าน **LIVE Chat** และ **ของขวัญ** แบบเรียลไทม์ผ่าน WebSocket พร้อมระบบ auto-reconnect และเสียงแจ้งเตือน
- จัดการตั้งค่าห้องไลฟ์: หัวข้อ, เกม, Replay, Age Restricted, เปิด/ปิดของขวัญและคอมเมนต์, Content Disclosure และ Region
- ดูสถานะบัญชี, โควตา RapidAPI, แคมเปญ, ประวัติ violation และการยื่นอุทธรณ์ (Appeals)

---

## สถาปัตยกรรมการทำงาน

1. แอปสร้างห้อง TikTok LIVE และรับ Push URL/Key จริงจาก TikTok
2. แอปเปิด local FFmpeg RTMP proxy ในเครื่อง
3. OBS ส่งภาพและเสียงมาที่ local RTMP (`rtmp://127.0.0.1:<port>/...`) ที่แอปแสดงให้
4. Proxy แนบ stream metadata แล้วส่งต่อไปยังเซิร์ฟเวอร์ TikTok

> **สำคัญ:** ให้นำ **Local RTMP URL/Key** ที่แอปแสดงไปใส่ใน OBS ไม่ควรนำ URL จริงของ TikTok ไปยิงตรงจาก OBS เพราะอาจถูกตัดการเชื่อมต่อหรือติดข้อจำกัดด้าน integrity/authenticity

---

## สิ่งที่ต้องเตรียม (Requirements)

- Python 3.10+ (แนะนำ Python 3.13 สำหรับ build)
- **FFmpeg** ติดตั้งอยู่ใน `PATH`
- **OBS Studio**
- บัญชี TikTok ที่มีสิทธิ์ไลฟ์ (TikTok LIVE / LIVE Studio access)
- **RapidAPI Key** จากบริการต้นฉบับ: [TikTok LIVE Studio API Signer on RapidAPI](https://rapidapi.com/Loukious/api/tiktok-live-studio-api-signer1)

---

## การติดตั้งและใช้งาน

ติดตั้ง dependency จากซอร์สโค้ด:

```bash
pip install -r requirements.txt
```

เปิดใช้งานแอป:

```bash
python TiktokStreamKeyGenerator.py
```

ขั้นตอนเริ่มต้น:
1. เข้าสู่ระบบ TikTok (QR Login หรือนำเข้า `cookies.json`)
2. กรอก **RapidAPI Key** ใน `Account` (หรือ `Settings → Account`)
3. ตั้งชื่อไลฟ์ เลือกหัวข้อ/เกม และตัวเลือกสตรีม
4. กด **Go Live** แล้วคัดลอก **Stream URL** และ **Stream Key** ไปใส่ใน OBS

---

## การเข้าสู่ระบบด้วย Exported Cookies

หากไม่สามารถล็อกอินผ่านเบราว์เซอร์หรือ QR ได้:
1. ติดตั้งส่วนขยาย Chrome: [Export cookie JSON file for Puppeteer](https://chromewebstore.google.com/detail/export-cookie-json-file-f/nmckokihipjgplolmcmjakknndddifde)
2. ล็อกอิน TikTok ใน Chrome แล้วเปิดค้างไว้ที่หน้า `tiktok.com`
3. กด Export เพื่อดาวน์โหลดไฟล์ JSON
4. ในแอปเลือก **Account → Import cookies…** แล้วเลือกไฟล์ที่ดาวน์โหลดมา

> ไฟล์ cookies เป็นข้อมูลยืนยันตัวตนของบัญชี ห้ามแชร์หรือ commit ลง git

---

## การรันทดสอบ (Offline Tests)

```bash
python -m pip install -r requirements-test.txt
python scripts/run_tests.py
```

---

## ลิขสิทธิ์และเครดิต (Credits & Copyright)

- โปรเจกต์ต้นฉบับพัฒนาโดย **[Loukious](https://github.com/Loukious)** ใน repository [Loukious/TikTokStreamKeyGenerator](https://github.com/Loukious/TikTokStreamKeyGenerator)
- สงวนสิทธิ์และเครดิตของสถาปัตยกรรมหลัก, โปรโตคอลการสื่อสาร, ระบบลงนามคำขอ (RapidAPI Signer) และคู่มือต้นฉบับไว้ให้เจ้าของผลงานเดิมทั้งหมด
- การปรับแต่งใน repository นี้จัดทำเพื่อใช้งานส่วนตัวและปรับปรุงประสบการณ์ผู้ใช้ภาษาไทยโดย **[equalignorecase](https://github.com/equalignorecase)**
