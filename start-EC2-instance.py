# In some companies, there is no need to run their EC2 instances 24/7; 
# they require instances to operate during specific time periods, on working hours, from 8:00 AM in the morning to 5:00 PM in the evening. 

# start one or many instances automatically

import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name='########') # Replace your Region name

    # Specify the instances ID of the EC2 instances you want to start
    instance_id = [
        '###########',
        '###########',
        ]# Replace your Instances IDs

    # Start the EC2 instances
    try:
        response = ec2_client.start_instances(InstanceIds=instance_id, DryRun=False)
        print(f"Starting EC2 instance {instance_id}...")
        print(f"Response: {response}")
        return {
            'statusCode': 200,
            'body': f"EC2 instances {instance_id} are being started."
        }
    except Exception as e:
        print(f"Error starting EC2 instances: {e}")
        return {
            'statusCode': 500,
            'body': f"Error starting EC2 instances: {str(e)}"
        }
