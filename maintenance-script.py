import boto3

# Configure AWS credentials
session = boto3.session.Session()
ssm_client = session.client('ssm')
ec2_client = session.client('ec2')

# Create Run Command document for backup
ssm_client.create_document(
    Name='EC2Backup',
    Content={
        'Commands': [
            'sudo apt-get update',
            'sudo apt-get install rsync',
            'rsync -av /home/ubuntu/data /mnt/backup/data'
        ]
    },
    DocumentType='Command'
)

# Create maintenance window for backups
ssm_client.create_maintenance_window(
    Name='EC2BackupWindow',
    Schedule='cron(0 0 * * ?)',
    DurationInHours=1
)

# Create EC2 Scheduler schedule for backups
ec2_client.create_schedule(
    Name='EC2BackupSchedule',
    Description='Schedule for EC2 backups',
    TargetGroupArn='arn:aws:us-east-1:ec2:t2:tgw-1234567890/tg-1234567890',
    ScheduleExpression='cron(0 0 * * ?)',
    State='ENABLED',
    DesiredCount=100,
    LaunchTemplateSpecifications=[
        {
            'LaunchTemplateId': 'lt-1234567890',
            'Version': '1'
        }
    ]
)
