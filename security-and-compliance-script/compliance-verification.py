import boto3
import json

# Establish a connection to AWS services
config_client = boto3.client('config')

# Configure Config to record and evaluate your AWS resource configurations
config_client.put_configuration_recorder(
    ConfigurationRecorderName='MyConfigurationRecorder',
    RecordingGroupArn='YOUR_RECORDING_GROUP_ARN',
    RoleARN='YOUR_ROLE_ARN'
)

config_client.put_configuration_rule(
    ConfigRuleName='MyConfigurationRule',
    Source={
        'ConfigRuleName': 'MyConfigurationRule',
        'SourceIdentifier': 'AWS/Config'
    },
    Description='My Configuration Rule Description',
    InputParameters={
        'ResourceTypes': ['AWS::EC2::Instance', 'AWS::IAM::Role']
    },
    EvaluationPeriods={
        'Compliance': {
            'EvaluationFrequency'
        }
    }
)
    