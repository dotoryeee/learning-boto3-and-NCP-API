from datetime import datetime
from pytz import timezone
import boto3


def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name="ap-northeast-2")

    instances = ec2.instances.filter(
        Filters=[
            {'Name': 'tag:backup', 'Values': ['true']}
        ]
    )
    
    time_format = "%Y-%m-%d-%H:%M:%S"
    timestamp = datetime.now(timezone('Asia/Seoul'))
    # print(timestamp.strftime(time_format))    

    for instance in instances.all():
        print('='*18, end='')
        print(f'INSTANCE {instance.id} SNAPSHOT', end='')
        print('='*18)
        for volume in instance.volumes.all():
            print(f'VOLUME : {volume.id} ..... ', end='')
            snapshot = volume.create_snapshot(Description=f'{instance.id}/{volume.id}/{timestamp}')
            print(f"SNAPSHOT ID : {snapshot.id}")

lambda_handler('','')