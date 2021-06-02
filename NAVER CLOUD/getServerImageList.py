import requests
import hashlib
import hmac
import base64
import requests
import time
import json

######################################################
ACCESS_KEY = "FEFECEECC2B8E2FCB41C"
SECRET_KEY = "76C215E35B101A66F01BF883CAF76CB246D62710"
######################################################


method = "GET"
url = "https://ncloud.apigw.ntruss.com"
uri = "/vserver/v2/getServerImageProductList?responseFormatType=json"

time_stamp = str(int(time.time() * 1000))


def makeSignature():
    secret_key = bytes(SECRET_KEY, "UTF-8")
    message = method + " " + uri + "\n" + time_stamp + "\n" + ACCESS_KEY
    message = bytes(message, "UTF-8")
    signKey = base64.b64encode(
        hmac.new(secret_key, message, digestmod=hashlib.sha256).digest()
    )
    return signKey


def main():
    signKey = makeSignature()
    headers = {
        "x-ncp-iam-access-key": ACCESS_KEY,
        "x-ncp-apigw-timestamp": time_stamp,
        "x-ncp-apigw-signature-v2": signKey,
    }
    r = requests.get(url + uri, headers=headers)
    returnCode = r.status_code
    if returnCode == 200:
        data = json.loads(r.text)
        data = data["getServerImageProductListResponse"]["productList"]
        print("=" * 40, end="")
        print("이미지 목록", end="")
        print("=" * 40)
        print("타입\t\t이미지 이름\t\t\t\t\t이미지 코드")
        for i in data:
            print(
                f'{i["productType"]["code"]}\t{i["productDescription"].ljust(40)}\t  {i["productCode"]}'
            )
        print("=" * 90)
    else:
        print(f"Error Code: {returnCode} / {r.text}")


main()
