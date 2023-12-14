import boto3

# Configure AWS credentials
session = boto3.session.Session()
client = session.client('ec2')
sns_client = session.client('sns')

# Define alarm thresholds
cpu_utilization_threshold = 80
memory_utilization_threshold = 90

# Get EC2 instances
instances = client.describe_instances()['Reservations']

# Check each instance
for reservation in instances:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']

        # Get CPU utilization
        cpu_utilization = get_cpu_utilization(instance_id)

        # Check CPU utilization alarm
        if cpu_utilization > cpu_utilization_threshold:
            send_alert(sns_client, "CPU utilization too high for instance %s" % instance_id)

        # Get memory utilization
        memory_utilization = get_memory_utilization(instance_id)

        # Check memory utilization alarm
        if memory_utilization > memory_utilization_threshold:
            send_alert(sns_client, "Memory utilization too high for instance %s" % instance_id)
