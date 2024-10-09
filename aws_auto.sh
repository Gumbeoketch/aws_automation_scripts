#!/bin/bash

# Define AWS region
REGION="us-west-2"

# List all running instances in the specified region
list_running_instances() {
    aws ec2 describe-instances --region $REGION --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].[InstanceId,ImageId,Tags]" --output table
}

# Check if instances are using the latest AMI
check_latest_ami() {
    for instance_id in $(aws ec2 describe-instances --region $REGION --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].InstanceId" --output text); do
        current_ami=$(aws ec2 describe-instances --region $REGION --instance-ids $instance_id --query "Reservations[].Instances[].ImageId" --output text)
        latest_ami=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/al2022-ami-kernel-5.10-x86_64 --region $REGION --query "Parameters[].Value" --output text)

        if [[ "$current_ami" != "$latest_ami" ]]; then
            echo "Instance $instance_id is using an outdated AMI ($current_ami). Latest is $latest_ami."
        else
            echo "Instance $instance_id is using the latest AMI."
        fi
    done
}

# List all environments based on instance tags
list_environments() {
    aws ec2 describe-instances --region $REGION --query "Reservations[].Instances[].[InstanceId,Tags[?Key=='Environment']|[0].Value]" --output table
}

# List all security groups in the specified region
list_security_groups() {
    aws ec2 describe-security-groups --region $REGION --query "SecurityGroups[].[GroupId,GroupName]" --output table
}

# Identify security groups with overly permissive inbound rules
check_security_groups() {
    aws ec2 describe-security-groups --region $REGION --query "SecurityGroups[?IpPermissions[?IpRanges[?CidrIp=='0.0.0.0/0']]].[GroupId,GroupName]" --output table
}

# Update security groups to restrict overly permissive rules
restrict_security_groups() {
    for sg_id in $(aws ec2 describe-security-groups --region $REGION --query "SecurityGroups[?IpPermissions[?IpRanges[?CidrIp=='0.0.0.0/0']]].GroupId" --output text); do
        aws ec2 revoke-security-group-ingress --group-id $sg_id --protocol all --port all --cidr 0.0.0.0/0
        echo "Restricted overly permissive rules in security group $sg_id."
    done
}

# Call functions
list_running_instances
check_latest_ami
list_environments
list_security_groups
check_security_groups
restrict_security_groups

