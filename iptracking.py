import requests
import argparse

def get_ip_info(ip):
    url = f"http://ipinfo.io/{ip}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("IPアドレス情報:")
        print(f"  IP: {data.get('ip', '不明')}")
        print(f"  ホスト名: {data.get('hostname', '不明')}")
        print(f"  市区町村: {data.get('city', '不明')}")
        print(f"  地域: {data.get('region', '不明')}")
        print(f"  国: {data.get('country', '不明')}")
        print(f"  ISP: {data.get('org', '不明')}")
        print(f"  緯度・経度: {data.get('loc', '不明')}")
    else:
        print(f"エラー: IP情報を取得できませんでした（{response.status_code}）")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="指定したIPアドレスの情報を取得します。")
    parser.add_argument("-u", "--url", required=True, help="調査するIPアドレス")
    
    args = parser.parse_args()
    
    get_ip_info(args.url)
