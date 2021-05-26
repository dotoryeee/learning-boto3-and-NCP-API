###미완성###
import requests
import hashlib
import hmac
import base64
import requests
import time


def make_signature():
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)

    access_key = "5724A942A8DBEDD50524"  # ACCESS KEY
    secret_key = "656D758405AED7944511EA27B4DF26E4272FF302"  # SECRET KEY
    secret_key = bytes(secret_key, "UTF-8")

    method = "GET"
    uri = "/photos/puppy.jpg?query1=&query2"

    message = method + " " + uri + "\n" + timestamp + "\n"
    +access_key
    message = bytes(message, "UTF-8")
    signingKey = base64.b64encode(
        hmac.new(secret_key, message, digestmod=hashlib.sha256).digest()
    )
    return signingKey


def main(args):
    try:
        r = requests.get("https://naver.com")
        result = r.status_code
    except:
        result = "CONNECT FAIL"
    return {"result": result}
