from datetime import datetime
from pytz import timezone
import boto3

#########################
REGION         = "ap-northeast-2"
SNAPSHOT_COUNT = 5
#스냅샷을 몇 개 남길 지 선택
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
            try:
                print(f'VOLUME : {volume.id} ..... ', end='')
                snapshot = volume.create_snapshot(Description=f'{instance.id}/{volume.id}/{timestamp}')
                print(f"SNAPSHOT ID : {snapshot.id}")
            except Exception as e:
                print(f'ERROR : FAIL TO MAKE SNAPSHOT \n {e}')

def clearSnapshot():
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    ec2 = boto3.client('ec2', region_name=REGION)
    response = ec2.describe_snapshots(OwnerIds=[account_id])
    snapshots = response["Snapshots"]
    snapshots.sort(key=lambda x: x["StartTime"])
    print(f'현재 스냅샷 개수 : {len(snapshots)}\n'+'-'*23+'스냅샷 삭제 시작'+'-'*23)
    snapshots = snapshots[:-SNAPSHOT_COUNT]
    if len(snapshots) != 0:
        for snap in snapshots:
            print(snap["Description"])
            id = snap['SnapshotId']
            try:
                ec2.delete_snapshot(SnapshotId=id)
                print(f'{id} 삭제 성공')
            except Exception as e:
                print(f'ERROR : fail to remove {id} \n {e}')
    else:
        print('삭제할 스냅샷 없음'.rjust(32))

def lambda_handler(event, context):
    makeSnapshot()
    clearSnapshot()

lambda_handler('','')