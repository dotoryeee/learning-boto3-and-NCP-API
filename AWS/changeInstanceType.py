##############################################
TARGET_INSTANCE_IDs = ["i-0351fd54bd47a17db"]
TARGET_INSTANCE_TYPE = "t2.nano"
##############################################

import boto3

ec2 = boto3.client("ec2")


def stopInstance(instanceID):
    try:
        ec2.stop_instances(InstanceIds=[instanceID])
        print(f"trying to STOP INSTANCE {instanceID}...", end="")
        waiter = ec2.get_waiter("instance_stopped")
        waiter.wait(InstanceIds=[instanceID])
        print(f"SUCCESS")
    except:
        print(f"FAILED : STOP INSTANCE {instanceID}")


def modifyInstance(instanceID):
    try:
        ec2.modify_instance_attribute(
            InstanceId=instanceID, Attribute="instanceType", Value=TARGET_INSTANCE_TYPE
        )
        print(f"SUCCESS : {instanceID} INSTANCE CHANGED TO {TARGET_INSTANCE_TYPE}")
    except:
        print(f"FAILED : CHANGE {instanceID} INSTANCE TYPE")


def startInstance(instanceID):
    try:
        ec2.start_instances(InstanceIds=[instanceID])
        print(f"SUCCESS : RESTART {instanceID}")
    except:
        print(f"FAILED : START INSTANCE {instanceID}")


def main():
    for instanceID in TARGET_INSTANCE_IDs:
        stopInstance(instanceID)
        modifyInstance(instanceID)
        startInstance(instanceID)


main()
