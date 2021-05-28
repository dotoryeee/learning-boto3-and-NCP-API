from logging import error
import boto3

TARGET_INSTANCE_IDs = ["i-0f8e23d613b7d62f0"]
TARGET_GROUP_ARN = ""

elb = boto3.client("elbv2")


def attachInstance(TGarn, instanceID):
    try:
        response = elb.register_targets(
            TargetGroupArn=TGarn,  # string
            Targets=[{"Id": instanceID}],  # dict in list
        )
        print(response)
        return response
    except:
        raise Exception("ERROR : FAIL TO ATTACH INSTANCE TO TARGET GROUP")
