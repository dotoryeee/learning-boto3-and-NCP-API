from logging import error
import boto3
from stopAndStartEC2 import stopInstance

TARGET_INSTANCE_IDs = ["i-082ec8f7f04524c30"]
TARGET_GROUP_ARN = ""

elb = boto3.client("elbv2")


def detachInstance(TGarn, instanceID):
    try:
        response = elb.deregister_targets(
            TargetGroupArn=TGarn,  # string
            Targets=[{"Id": instanceID}],  # dict in list
        )
        print(response)
        return response
    except:
        raise Exception("ERROR : FAIL TO DETACH INSTANCE FORM TARGET GROUP")
