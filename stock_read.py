import os
from urllib import response
import requests
import pprint
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 株価のデータをwebapiで取得して、pngで表示する機能
# apikeyはALPHA_VANTAGEから取得、
# スクリプトのディレクトリからターミナルでexport ALPHA_VANTAGE_KEY=キーの値
# =の後に取得したキーの値を入力し実行。それで一時的なパスを設定することができる。

def main():
    api_key = os.environ['ALPHA_VANTAGE_KEY']
    # 株価はsymbol=部分に入力済み。この例ではMSFT(マイクロソフト)の株価をここで取得
    url = 'https://www.alphavantage.co/query?' \
        f'function=TIME_SERIES_DAILY&symbol=MSFT&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # 最新から過去→過去から最新データに横方向へのデータ表示を変更する
    # .items()を呼び出して、reversed関数で逆表示、それをdict関数で辞書型に変換する
    # これで辞書の要素の順番が逆になる
    daily_data = dict(reversed(data['Time Series (Daily)'].items()))
    date_list = daily_data.keys()
    close_list = [float(x['4. close'])for x in daily_data.values()]

    # 横のサイス変更(figsize=(12, 4)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(date_list, close_list)
    # 表示する日の間隔を指定
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=15))
    ax.grid()
    fig.savefig('./stock.png')

if __name__ == '__main__':
    main()