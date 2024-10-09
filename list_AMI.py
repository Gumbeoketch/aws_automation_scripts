# Import all the modules and Libraries
import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# Use Boto3 Documentation to get more information
result = ec2_console.describe_images(Owners=['self', 'amazon'])['Images']

# Loop through and print AMI ID, name, and creation date
for each_image in result:
    print(f"AMI Name: {each_image['Name']}, AMI ID: {each_image['ImageId']}, Creation Date: {each_image['CreationDate']}")


