import boto3

client = boto3.client("ec2")

TARGET_INSTANCE_IDs = ["i-0351fd54bd47a17db"]

for instanceID in TARGET_INSTANCE_IDs:
    client.stop_instances(InstanceIds=[instanceID])
    waiter = client.get_waiter("instance_stopped")
    waiter.wait(InstanceIds=[instanceID])

    client.modify_instance_attribute(
        InstanceId=instanceID, Attribute="instanceType", Value="t2.nano"
    )

    client.start_instances(InstanceIds=[instanceID])
