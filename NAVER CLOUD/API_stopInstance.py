import requests
import hashlib
import hmac
import base64
import requests
import time
import json

######################################################
ACCESS_KEY = "5724A942A8DBEDD50524"
SECRET_KEY = "656D758405AED7944511EA27B4DF26E4272FF302"
TARGET_INSTANCE_IDs = ["6799099"]
######################################################


method = "GET"
url = "https://ncloud.apigw.ntruss.com"
uri = "/vserver/v2/stopServerInstances?responseFormatType=json"


for num, ID in enumerate(TARGET_INSTANCE_IDs):
    uri = f"{uri}&serverInstanceNoList.{num+1}={ID}"


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
    # print(f"REQUEST {url + uri}")
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
        data = data["stopServerInstancesResponse"]["returnMessage"]
        print(f"STOP REQUEST : {data}")
    else:
        print(f"Error Code: {returnCode} / {r.text}")


main()
