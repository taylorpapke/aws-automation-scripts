import boto3

# Configure AWS credentials
session = boto3.session.Session()
client = session.client('cloudformation')

# Define VPC parameters
vpc_cidr_block = '10.0.0.0/16'
subnet_cidr_block = '10.0.1.0/24'

# Define EC2 parameters
instance_type = 't2.micro'
ami_id = 'ami-0c55b159cbfafe1f0'

# Create VPC template
vpc_template = {
    'AWSTemplateFormatVersion': '2010-09-09',
    'Resources': {
        'VPC': {
            'Type': 'AWS::EC2::VPC',
            'Properties': {
                'CidrBlock': vpc_cidr_block
            }
        },
        'Subnet': {
            'Type': 'AWS::EC2::Subnet',
            'Properties': {
                'VpcId': {'Ref': 'VPC'},
                'CidrBlock': subnet_cidr_block
            }
        }
    }
}

# Create EC2 template
ec2_template = {
    'AWSTemplateFormatVersion': '2010-09-09',
    'Resources': {
        'EC2Instance': {
            'Type': 'AWS::EC2::Instance',
            'Properties': {
                'ImageId': ami_id,
                'InstanceType': instance_type,
                'SubnetId': {'Ref': 'Subnet'}
            }
        }
    }
}

# Create CloudFormation stacks for VPC and EC2
client.create_stack(StackName='VPCStack', TemplateBody=json.dumps(vpc_template))
client.create_stack(StackName='EC2Stack', TemplateBody=json.dumps(ec2_template))
