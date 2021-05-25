import boto3
from botocore.exceptions import ClientError

TARGET_INSTANCE_IDs = []

ec2 = boto3.client("ec2")


def stopInstance():
    for instanceID in TARGET_INSTANCE_IDs:
        try:
            response = ec2.stop_instances(InstanceIDs=instanceID, DryRun=False)
            print(f"STOP SUCCESS : {response}")
        except ClientError as e:
            print(f"ERROR : {e}")


def startInstance():
    for instanceID in TARGET_INSTANCE_IDs:
        try:
            response = ec2.start_instances(InstanceIDs=instanceID, DryRun=False)
            print(f"START SUCCESS : {response}")
        except ClientError as e:
            print(f"STOP ERROR : {e}")


def rebootInstance():
    for instanceID in TARGET_INSTANCE_IDs:
        try:
            response = ec2.reboot_instances(InstanceIDs=instanceID, DryRun=False)
            print(f"REBOOT SUCCESS : {response}")
        except ClientError as e:
            print(f"REBOOT ERROR : {e}")
