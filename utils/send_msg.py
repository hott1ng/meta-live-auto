import requests
import base64
import hashlib

def send_warning(path):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6f50d05c-fde2-4539-941d-8288546dca5c'

    with open(path, 'rb') as f:
        img = f.read()
    md5 = hashlib.md5(img).hexdigest()

    data = {
        "msgtype": "image",
        "image": {
            "base64": base64.b64encode(img).decode("ascii"),
            "md5": md5
        }
    }
    response = requests.post(url, json=data)

    data = {
    "msgtype": "text",
    "text": {
        "content": '发生错误,请人工介入',
        "mentioned_list":["yufeifan"],
        # "mentioned_mobile_list":["13800001111","@all"]
    }
}

    response = requests.post(url, json=data)
