from logging import error
import boto3
from stopAndStartEC2 import stopInstance
from detachInstanceFromTG import detachInstance

TARGET_INSTANCE_IDs = ["i-082ec8f7f04524c30"]
TARGET_GROUP_ARN = ""

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
