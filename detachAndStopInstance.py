from logging import error
import boto3
from stopAndStartEC2 import stopInstance
from detachInstanceFromTG import detachInstance

TARGET_INSTANCE_IDs = ["i-0f8e23d613b7d62f0"]
TARGET_GROUP_ARN = "arn:aws:elasticloadbalancing:ap-northeast-2:737382971423:targetgroup/testTG/36174c22e12f595e"

elb = boto3.client("elbv2")


def checkDraining():
    if True:
        return "draining"
    else:
        return "detached"


def lambda_handler(event, context):
    drainingStatus = "draining"
    for instance in TARGET_INSTANCE_IDs:
        detachInstance(TARGET_GROUP_ARN, instance)
    while True:
        if drainingStatus == "draining":
            drainingStatus = checkDraining()
        else:
            break
    stopInstance(TARGET_INSTANCE_IDs)
