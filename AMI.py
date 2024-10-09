# Import all the modules and Libraries
import boto3

AWS_REGION = "us-east-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)

images = EC2_RESOURCE.images.all()

for image in images:
    print(f'AMI{image.id}: {image.name}')