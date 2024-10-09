# Import all the necessary modules and libraries
import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# List all security groups in a specified region
def list_security_groups():
    response = ec2_console.describe_security_groups()
    security_groups = response['SecurityGroups']
    return security_groups

# Identify overly permissive inbound rules
def identify_overly_permissive_rules(security_groups):
    for sg in security_groups:
        for permission in sg['IpPermissions']:
            if 'IpRanges' in permission and any(ip['CidrIp'] == '0.0.0.0/0' for ip in permission['IpRanges']):
                print(f"Security Group: {sg['GroupName']}, ID: {sg['GroupId']} - Overly permissive inbound rule found.")

# Update security groups to restrict overly permissive rules
def restrict_overly_permissive_rules(security_groups):
    for sg in security_groups:
        for permission in sg['IpPermissions']:
            if 'IpRanges' in permission and any(ip['CidrIp'] == '0.0.0.0/0' for ip in permission['IpRanges']):
                # Implement logic to update the security group here
                print(f"Restricting rules for Security Group: {sg['GroupName']}, ID: {sg['GroupId']}")

# Main execution
if __name__ == "__main__":
    security_groups = list_security_groups()
    identify_overly_permissive_rules(security_groups)
    restrict_overly_permissive_rules(security_groups)
