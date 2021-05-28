from logging import error
import boto3

TARGET_INSTANCE_IDs = ["i-0f8e23d613b7d62f0"]
TARGET_GROUP_ARN = "arn:aws:elasticloadbalancing:ap-northeast-2:737382971423:targetgroup/testTG/36174c22e12f595e"

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


def test():
    for instance in TARGET_INSTANCE_IDs:
        detachInstance(TARGET_GROUP_ARN, instance)


test()
