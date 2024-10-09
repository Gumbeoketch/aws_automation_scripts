# Import all the necessary modules and libraries
import boto3

# Function to get the latest AMI ID for a specified instance type
def get_latest_ami(instance_type):
    ec2_console = aws_management_console.client(service_name="ec2")
    images = ec2_console.describe_images(Owners=['self', 'amazon'])['Images']
    # Logic to find the latest AMI based on creation date
    latest_ami = max(images, key=lambda x: x['CreationDate'] if 'CreationDate' in x else '')
    return latest_ami['ImageId']

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# List all running instances in a specified region
instances = ec2_console.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])['Reservations']
for reservation in instances:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        ami_id = instance['ImageId']
        tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}

        # Check if the instance is using the latest AMI
        latest_ami = get_latest_ami(instance_type)
        if ami_id != latest_ami:
            print(f"Instance ID: {instance_id} is using an outdated AMI: {ami_id}. Latest AMI: {latest_ami}.")
            # Implement a function to update instances with outdated AMIs (placeholder)
            print(f"Implementing update for Instance ID: {instance_id}...")  # You can add actual update logic here
        else:
            print(f"Instance ID: {instance_id} is using the latest AMI: {ami_id}.")

        # List all environments using instance tags
        environment = tags.get('Environment', 'No Environment Tag')
        print(f"Instance ID: {instance_id}, Environment: {environment}")
