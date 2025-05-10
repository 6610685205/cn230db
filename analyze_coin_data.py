import sqlite3
import matplotlib.pyplot as plt
import numpy as np

DB_FILE = 'crypto_data.db'

def fetch_top_5_by_market_cap():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name, symbol, current_price, market_cap, total_volume, high_24h, low_24h, change_24h
        FROM crypto_data
        ORDER BY market_cap DESC
        LIMIT 5
    ''')

    rows = cursor.fetchall()
    conn.close()
    return rows

def plot_detailed_comparison():
    data = fetch_top_5_by_market_cap()
    if not data:
        print("No data available.")
        return

    names = [row[0] for row in data]
    symbols = [row[1] for row in data]
    prices = [row[2] for row in data]
    market_caps = [row[3] for row in data]
    volumes = [row[4] for row in data]
    highs = [row[5] for row in data]
    lows = [row[6] for row in data]
    changes = [row[7] for row in data]

    fig, ax = plt.subplots(2, 1, figsize=(12, 12))

    ax[0].bar(names, prices, color='skyblue', label="Price")
    ax[0].set_title('Top 5 Cryptocurrencies by Price')
    ax[0].set_xlabel('Cryptocurrency')
    ax[0].set_ylabel('Price (USD)')
    ax[0].tick_params(axis='x', rotation=45)

    x = np.arange(len(names))
    ax[1].plot(x, market_caps, label='Market Cap', marker='o', color='green', linestyle='-', linewidth=2)
    ax[1].set_title('Top 5 Cryptocurrencies by Market Cap')
    ax[1].set_xlabel('Cryptocurrency')
    ax[1].set_ylabel('Market Cap (USD)')
    ax[1].set_xticks(x)
    ax[1].set_xticklabels(names, rotation=45)
    ax[1].legend()

    plt.tight_layout()

    plt.savefig('crypto_comparison.png')  
    print("Graph saved as 'crypto_comparison.png'")
    plt.show()

    print("\nTop 5 Cryptocurrencies by Market Cap:")
    print("========================================")
    for i, name in enumerate(names):
        print(f"\n{name} ({symbols[i]}):")
        print(f"  - Current Price: ${prices[i]:,.2f}")
        print(f"  - Market Cap: ${market_caps[i]:,.2f}")
        print(f"  - Total Volume: ${volumes[i]:,.2f}")
        print(f"  - 24h High: ${highs[i]:,.2f}")
        print(f"  - 24h Low: ${lows[i]:,.2f}")
        print(f"  - 24h Price Change: {changes[i]:,.2f}%")

plot_detailed_comparison()
