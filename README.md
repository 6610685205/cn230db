# 🔍 วิเคราะห์และจัดอันดับ Cryptocurrency ด้วย CoinGecko API จัดทำโดย นนทพัทธ์ บุญประสิทธิ์ 6610685205

## 📌 บทนำ
โครงงานนี้มีวัตถุประสงค์เพื่อศึกษาข้อมูลสกุลเงินดิจิทัล (Cryptocurrency) จาก CoinGecko API ซึ่งเป็นแหล่งข้อมูลที่เชื่อถือได้ โดยเน้นวิเคราะห์เหรียญยอดนิยม เช่น Bitcoin, Ethereum, Binance Coin, Cardano และ Solana เพื่อนำเสนอราคา, มูลค่าตลาด (Market Cap), ปริมาณการซื้อขาย และอัตราการเปลี่ยนแปลงในรอบ 24 ชั่วโมง พร้อมทั้งสร้างกราฟเปรียบเทียบเพื่อให้เข้าใจข้อมูลได้ง่ายขึ้น

---

## 🎯 วัตถุประสงค์
- เพื่อเรียนรู้การดึงข้อมูลจาก API จริง
- วิเคราะห์และจัดอันดับเหรียญดิจิทัลตาม Market Cap
- สร้างฐานข้อมูล SQLite3 สำหรับจัดเก็บข้อมูลคริปโต
- สร้างกราฟ Line chart และ Bar chart เพื่อเปรียบเทียบข้อมูลสำคัญ

---

## ⚙️ วิธีดำเนินงาน

### 🔨 เครื่องมือที่ใช้
- ภาษา Python 3
- CoinGecko API
- SQLite3
- ไลบรารี: `requests`, `matplotlib`, `pandas`

### 🧭 ขั้นตอน
1. สร้างฐานข้อมูล `crypto_data.db`
2. ใช้ `coin_data.py` เพื่อดึงข้อมูลจาก API และบันทึกลงฐานข้อมูล
3. ใช้ `analyze_coin_data.py` เพื่อวิเคราะห์และแสดงผลผ่านกราฟ

---

## 🧪 ตัวอย่างผลการศึกษา

| ชื่อเหรียญ | ราคา (USD) | Market Cap | Volume 24h | High/Low 24h | เปลี่ยนแปลง 24h |
|------------|------------|-------------|--------------|----------------|-------------------|
| Bitcoin    | ✅ ดึงอัตโนมัติ | ✅ | ✅ | ✅ | ✅ |
| Ethereum   | ✅ | ✅ | ✅ | ✅ | ✅ |
| ...        | ... | ... | ... | ... | ... |

- แสดงกราฟเปรียบเทียบราคาล่าสุด (Line Chart)
- แสดงกราฟ Market Cap 5 อันดับ (Bar Chart)

> ✅ กราฟจะถูกสร้างโดยอัตโนมัติเมื่อรัน `analyze_coin_data.py`

---

## 🧠 ข้อเสนอแนะในการพัฒนาต่อ

- เพิ่มจำนวนเหรียญหรือการค้นหาแบบ Dynamic
- เชื่อมต่อ Dashboard ด้วย Streamlit หรือ Flask
- เพิ่มระบบแจ้งเตือนเมื่อราคาผันผวนเกินค่าที่กำหนด
- เก็บข้อมูลแบบ Time-Series สำหรับดูแนวโน้ม

---

## 🛠️ การติดตั้งและใช้งาน

### 1. ติดตั้งไลบรารี

```bash
pip install requests matplotlib pandas
```
## 2. รันโค้ดเพื่อดึงข้อมูลและวิเคราะห์
## ดึงข้อมูลจาก API และเก็บลงฐานข้อมูล
```bash
python coin_data.py
```
## วิเคราะห์ข้อมูลและสร้างกราฟ
```bash
python analyze_coin_data.py
```
## โครงสร้างไฟล์

├── coin_data.py              # ดึงข้อมูลจาก CoinGecko API
├── analyze_coin_data.py      # วิเคราะห์และสร้างกราฟ
├── crypto_data.db            # ฐานข้อมูล SQLite (สร้างอัตโนมัติ)
├── README.md                 # คำอธิบายโปรเจกต์


## ผู้จัดทำ
นาย นนทพัทธ์ บุญประสิทธิ์ รหัสนักศึกษา 6610685205

สาขาวิชา วิศวกรรมไฟฟ้าและคอมพิวเตอร์ คณะ วิศวกรรมศาสตร์

มหาวิทยาลัย ธรรมศาสตร์

## อ้างอิง

📚 อ้างอิง
CoinGecko API Documentation: https://www.coingecko.com/en/api/documentation

Python sqlite3 Module: https://docs.python.org/3/library/sqlite3.html

Requests Library: https://requests.readthedocs.io/en/latest/

Pandas Library: https://pandas.pydata.org/

Matplotlib Library: https://matplotlib.org/
