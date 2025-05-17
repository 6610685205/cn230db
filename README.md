# 🚀 CryptoCurrency Project (CoinGecko API)

โปรเจกต์นี้ใช้ CoinGecko API เพื่อดึงข้อมูลของเหรียญคริปโตต่าง ๆ แล้วจัดเก็บลงฐานข้อมูล SQLite จากนั้นวิเคราะห์และแสดงผลผ่านกราฟ เพื่อเปรียบเทียบเหรียญชั้นนำด้านราคาและมูลค่าตลาด (Market Cap)

---

## 🔧 โครงสร้างโปรเจกต์

### `coin_data.py`
- ดึงข้อมูลคริปโตจาก CoinGecko API (สูงสุด 50 อันดับแรก)
- บันทึกข้อมูลสำคัญลงฐานข้อมูล `crypto.db`
  - เช่น: `id`, `name`, `symbol`, `price`, `market_cap`, `volume`, `high_24h`, `low_24h`, `price_change_percentage_24h`

### `analyze_coin_data.py`
- อ่านข้อมูลจากฐานข้อมูล
- วิเคราะห์และจัดอันดับ:
  - ราคาปัจจุบัน
  - Market Cap
  - Volume การซื้อขาย
  - ราคาสูงสุด/ต่ำสุดใน 24 ชม.
  - อัตราการเปลี่ยนแปลงใน 24 ชม.
- สร้างกราฟ:
  - 📈 Line Chart: แสดงราคาของเหรียญ 5 อันดับแรก
  - 📊 Bar Chart: แสดง Market Cap เปรียบเทียบกัน

---

## ✅ วิธีใช้งาน

### 1. Fork Repository และเปิด Codespaces

### 2. รันคำสั่งใน Terminal

```bash
python db.py
