import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Get the current CPU utilization of the Auto Scaling group
asg_name = 'my-asg'
asg_metric = ec2.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])['AutoScalingGroups'][0]['Metrics'][0]
cpu_utilization = asg_metric['MetricValue']['Value']

# Define the target CPU utilization and scaling policy parameters
target_cpu_utilization = 50
cooldown = 300

# Scale up or down the Auto Scaling group based on CPU utilization
if cpu_utilization > target_cpu_utilization:
    desired_capacity = asg_metric['MetricValue']['MetricData']['Instances'] + 1
    ec2.set_desired_capacity(AutoScalingGroupName=asg_name, DesiredCapacity=desired_capacity)
elif cpu_utilization < target_cpu_utilization:
    desired_capacity = asg_metric['MetricValue']['MetricData']['Instances'] - 1
    ec2.set_desired_capacity(AutoScalingGroupName=asg_name, DesiredCapacity=desired_capacity)
