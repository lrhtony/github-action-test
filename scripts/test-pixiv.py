import os
import requests

access_token = os.getenv("PIXIV_ACCESS_TOKEN")
# access_token = ""
start_id = 95570000
end_id = 95570500
url = 'https://app-api.pixiv.net/v1/illust/detail'
headers = {
    'host': 'app-api.pixiv.net',
    'app-os': 'ios',
    'app-os-version': '14.6',
    'user-agent': 'PixivIOSApp/7.13.3 (iOS 14.6; iPhone13,2)',
    'Authorization': 'Bearer %s' % access_token,
    'accept-language': 'zh-cn'
}
for i in range(start_id, end_id):
    params = {
        'illust_id': i
    }
    try:
        data = requests.get(url=url, headers=headers, params=params).json()
        print(data)
    except requests.exceptions.SSLError:
        pass
    except requests.exceptions.ConnectionError:
        pass
