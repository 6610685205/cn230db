import requests
import sqlite3
from datetime import datetime

API_URL = 'https://api.coingecko.com/api/v3/coins/markets'
DB_FILE = 'crypto_data.db'

def create_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS crypto_data (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        symbol TEXT,
                        current_price REAL,
                        market_cap REAL,
                        total_volume REAL,
                        high_24h REAL,
                        low_24h REAL,
                        change_24h REAL,
                        timestamp DATETIME
                    )''')

    try:
        cursor.execute("ALTER TABLE crypto_data ADD COLUMN high_24h REAL")
        cursor.execute("ALTER TABLE crypto_data ADD COLUMN low_24h REAL")
        cursor.execute("ALTER TABLE crypto_data ADD COLUMN change_24h REAL")
        print("Columns added successfully.")
        
    except sqlite3.OperationalError:
        print("Columns already exist.")
    
    conn.commit()
    conn.close()

def fetch_and_store_data():
    coins = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'solana']
    params = {
        'vs_currency': 'usd',  
        'ids': ','.join(coins), 
    }

    response = requests.get(API_URL, params=params)
    data = response.json()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for coin in data:
        cursor.execute('''
            INSERT OR REPLACE INTO crypto_data (id, name, symbol, current_price, market_cap, total_volume, high_24h, low_24h, change_24h, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (coin['id'], coin['name'], coin['symbol'], coin['current_price'], coin['market_cap'], coin['total_volume'], coin['high_24h'], coin['low_24h'], coin['price_change_percentage_24h'], datetime.now()))

    conn.commit()
    conn.close()
    print("Data fetched and stored successfully.")

create_db()
fetch_and_store_data()
