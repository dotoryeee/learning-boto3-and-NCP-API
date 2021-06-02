import boto3

ec2 = boto3.client("ec2")

TARGET_INSTANCE_IDs = ["i-0351fd54bd47a17db"]
TARGET_INSTANCE_TYPE = "t2.micro"

for instanceID in TARGET_INSTANCE_IDs:
    try:
        ec2.stop_instances(InstanceIds=[instanceID])
        print(f"trying to STOP INSTANCE {instanceID}...", end="")
        waiter = ec2.get_waiter("instance_stopped")
        waiter.wait(InstanceIds=[instanceID])
        print("SUCCESS")
    except:
        print(f"FAILED : STOP INSTANCE {instanceID}")

    try:
        ec2.modify_instance_attribute(
            InstanceId=instanceID, Attribute="instanceType", Value=TARGET_INSTANCE_TYPE
        )
        print(f"{instanceID} INSTANCE CHANGED TO {TARGET_INSTANCE_TYPE}")
    except:
        print(f"FAILED : CHANGE {instanceID} INSTANCE TYPE")

    try:
        ec2.start_instances(InstanceIds=[instanceID])
        print(f"RESTART {instanceID} SUCCESS")
    except:
        print(f"FAILED : START INSTANCE {instanceID}")
