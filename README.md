# 🚀 CryptoCurrency Project (CoinGecko API) จัดทำโดย นนทพัทธ์ บุญประสิทธิ์ 6610685205

โปรเจกต์นี้ใช้ CoinGecko API เพื่อดึงข้อมูลของเหรียญคริปโตชั้นนำ เช่น Bitcoin, Ethereum, Binance Coin, Cardano และ Solana แล้วจัดเก็บลงฐานข้อมูล SQLite เพื่อใช้ในการวิเคราะห์และสร้างกราฟเปรียบเทียบมูลค่าทางการเงิน

---

## 🔧 โครงสร้างโปรเจกต์

### `coin_data.py`
- เชื่อมต่อกับ [CoinGecko API](https://www.coingecko.com/en/api) เพื่อดึงข้อมูลเหรียญ 5 อันดับ ได้แก่:
  - Bitcoin, Ethereum, Binance Coin, Cardano, Solana
- สร้างฐานข้อมูล `crypto_data.db` พร้อมตาราง `crypto_data`
- เก็บข้อมูล:
  - `id`, `name`, `symbol`
  - `current_price`, `market_cap`, `total_volume`
  - `high_24h`, `low_24h`, `change_24h`
  - `timestamp` (เวลาที่บันทึกข้อมูล)

### `analyze_coin_data.py`
- อ่านข้อมูลจากฐานข้อมูล SQLite
- คำนวณอันดับเหรียญตาม:
  - ราคาล่าสุด (`current_price`)
  - มูลค่าตลาด (`market_cap`)
  - ปริมาณการซื้อขาย (`total_volume`)
  - การเปลี่ยนแปลงราคา 24 ชั่วโมง
- สร้างกราฟ:
  - 📈 **Line Chart**: แสดงการเปรียบเทียบราคาของเหรียญ
  - 📊 **Bar Chart**: แสดงการเปรียบเทียบ Market Cap

---

## ✅ วิธีใช้งาน

### 1. Fork Repository และเปิดใน Codespaces 

### 2. ติดตั้ง dependency (เฉพาะกรณีใช้ `matplotlib`, `seaborn`, `pandas`)
```bash
pip install requests matplotlib seaborn pandas
```
### 3. run code ตามลำดับด้านล่างดังนี้
```bash
python coin_data.py
python analyze_coin_data.py
```
## สรุปและข้อเสนอแนะ
- ได้เรียนรู้การใช้ API, การจัดการฐานข้อมูล และการวิเคราะห์ข้อมูล
- ในอนาคตอาจเพิ่มฟีเจอร์วิเคราะห์เหรียญเพิ่มเติม, สร้างระบบแจ้งเตือนเมื่อราคาขึ้นหรือลงเกินกำหนด
