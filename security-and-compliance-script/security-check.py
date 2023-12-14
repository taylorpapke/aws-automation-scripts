import boto3
import json

# Establish a connection to AWS services
ec2_client = boto3.client('ec2')
ssm_client = boto3.client('ssm')

# Retrieve instances to scan
instances = ec2_client.describe_instances()

# Iterate through each instance and perform security checks
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']

        # Retrieve security group IDs associated with the instance
        security_groups = ec2_client.describe_instance_attribute(
            InstanceId=instance_id,
            Attribute='securityGroups'
        )

        # Check for specific security group rules or security group configurations
        # based on your security requirements
