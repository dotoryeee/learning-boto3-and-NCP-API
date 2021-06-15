from datetime import datetime
from pytz import timezone
import boto3

#########################
REGION = "ap-northeast-2"
#########################

def makeSnapshot():
    ec2 = boto3.resource('ec2', region_name=REGION)

    instances = ec2.instances.filter(
        Filters=[
            {'Name': 'tag:autoSnapShot', 'Values': ['True']}
        ]
    )    
    time_format = "%Y-%m-%d-%H:%M:%S"
    timestamp = datetime.now(timezone('Asia/Seoul')).strftime(time_format)

    for instance in instances.all():
        print('='*18, end='')
        print(f'INSTANCE {instance.id} SNAPSHOT', end='')
        print('='*18)
        for volume in instance.volumes.all():
            print(f'VOLUME : {volume.id} ..... ', end='')
            snapshot = volume.create_snapshot(Description=f'{instance.id}/{volume.id}/{timestamp}')
            print(f"SNAPSHOT ID : {snapshot.id}")

def clearSnapshot():
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    
    ec2 = boto3.client('ec2', region_name=REGION)
    response = ec2.describe_snapshots(OwnerIds=[account_id])
    snapshots = response["Snapshots"]
    snapshots.sort(key=lambda x: x["StartTime"])
    print(f'현재 스냅샷 개수 : {len(snapshots)}\n'+'-'*25+'삭제할 스냅샷'+'-'*25)
    snapshots = snapshots[:-2]
    for snap in snapshots:
        print(snap["Description"])
    for snapshot in snapshots:
        id = snapshot['SnapshotId']
        try:
            ec2.delete_snapshot(SnapshotId=id)
            print(f'{id} 삭제 성공')
        except Exception as e:
            print(f'ERROR : fail to remove {id} / {e}')
            continue

def lambda_handler(event, context):
    # makeSnapshot()
    clearSnapshot()

lambda_handler('','')