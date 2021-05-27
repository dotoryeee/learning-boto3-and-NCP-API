from logging import error
import boto3
from botocore.exceptions import ClientError

TARGET_INSTANCE_IDs = ["i-082ec8f7f04524c30"]
TARGET_GROUP_ARN = ""

ec2 = boto3.client("ec2")
elb = boto3.client("elbv2")


def stopInstance(instanceID):
    try:
        response = ec2.stop_instances(InstanceIds=instanceID, DryRun=False)
        print(f"STOP SUCCESS : {response}")
    except ClientError as e:
        print(f"ERROR : {e}")


def checkDraining():
    pass


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


def lambda_handler(event, context):
    detachInstance(TARGET_GROUP_ARN)
    while True:
        status = False
        if status:
            checkDraining()
        else:
            break
    stopInstance(TARGET_INSTANCE_IDs)
