import boto3
from botocore.exceptions import ClientError

TARGET_INSTANCE_IDs = ["i-0f8e23d613b7d62f0", "i-0a252bf0421dbbeb4"]

ec2 = boto3.client("ec2")


def stopInstance(instanceID):
    try:
        response = ec2.stop_instances(InstanceIds=instanceID, DryRun=False)
        print(f"STOP SUCCESS : {response}")
    except ClientError as e:
        print(f"ERROR : {e}")


def startInstance(instanceID):
    try:
        response = ec2.start_instances(InstanceIds=instanceID, DryRun=False)
        print(f"START SUCCESS : {response}")
    except ClientError as e:
        print(f"STOP ERROR : {e}")


def rebootInstance(instanceID):
    try:
        response = ec2.reboot_instances(InstanceIds=instanceID, DryRun=False)
        print(f"REBOOT SUCCESS : {response}")
    except ClientError as e:
        print(f"REBOOT ERROR : {e}")


def lambda_handler(event, context):
    # stopInstance(TARGET_INSTANCE_IDs)
    startInstance(TARGET_INSTANCE_IDs)
    # rebootInstance(TARGET_INSTANCE_IDs)


# lambda_handler("test", "test")
