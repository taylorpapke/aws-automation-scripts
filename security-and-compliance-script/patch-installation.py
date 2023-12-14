import boto3
import json

# Establish a connection to AWS services
patch_manager_client = boto3.client('patch')

# Create a patch baseline or use an existing one
patch_manager_client.create_patch_baseline(
    Name='MyPatchBaseline',
    Description='My Patch Baseline Description',
    OperatingSystem='windows-2019'
)

patch_manager_client.approve_patch_baseline(
    BaselineId='YOUR_BASELINE_ID',
    Patches=[
        {
            'PatchId': 'YOUR_PATCH_ID'
        }
    ]
)

# Create a patch group or use an existing one
patch_manager_client.create_patch_group(
    Name='MyPatchGroup',
    PatchBaselineId='YOUR_BASELINE_ID'
)

patch_manager_client.register_instances(
    InstanceIds=['YOUR_INSTANCE_ID'],
    PatchGroup='MyPatchGroup'
)

# Schedule a patch scan and deployment
patch_manager_client.schedule_state_manager_association(
    AssociationName='SSM_PATCH_SCAN_NAME',
    DocumentName='AWS-RunPatchBaseline',
    Targets=[
        {
            'InstanceId': 'YOUR_INSTANCE_ID'
        }
    ],
    Parameters={'BaselineId': 'YOUR_BASELINE_ID'}
)

patch_manager_client.schedule_state_manager_association(
    AssociationName='SSM_PATCH_DEPLOYMENT_NAME',
    DocumentName='AWS-ApplyPatchBaseline',
    Targets=[
        {
            'InstanceId': 'YOUR_INSTANCE_ID'
        }
    ],
    Parameters={'BaselineId': 'YOUR_BASELINE_ID'}
)
