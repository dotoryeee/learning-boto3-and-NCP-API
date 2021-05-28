import requests
import hashlib
import hmac
import base64
import requests
import time
import xmltodict

######################################################
ACCESS_KEY = "5724A942A8DBEDD50524"
SECRET_KEY = "656D758405AED7944511EA27B4DF26E4272FF302"
######################################################

method = "GET"
url = "https://ncloud.apigw.ntruss.com"
uri = "/vserver/v2/getServerInstanceList"

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
        data = r.text
        data = xmltodict.parse(data)
        data = data["getServerInstanceListResponse"]["serverInstanceList"][
            "serverInstance"
        ]
        print("----------------------서버 목록--------------------------")
        print("  서버이름\t\t 인스턴스ID\t   상태\t\t퍼블릭IP")
        for i in data:
            print(
                f'{i["serverName"].ljust(20)}\t  {i["serverInstanceNo"]}\t  {i["serverInstanceStatusName"]}\t  {i["publicIp"]}'
            )
        print("--------------------------------------------------------")
    else:
        print(f"Error Code: {returnCode} / {r.text}")


main()
