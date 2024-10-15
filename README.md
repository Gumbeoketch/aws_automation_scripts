
## INSTALL PYTHON3
https://www.python.org/downloads/
## INSTALL AWS CLI
Follow the instructions to install AWS CLI:
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## AUTHENTICATE TO CLI USING IAM USER WITH TERRAFORM PERMISSION
Configure your AWS CLI with credentials:
aws configure

## INSTALL BOTO3
pip install boto3

**Go through the AWS Boto3 documentation, specifically for ec2 to understand the describe request and respond syntax##
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

## RUNNING THE SCRIPTS
python list_running_instances.py --region <region>
python check_update_ami.py --region <region>
python list_security_groups.py --region <region>
python restrict_security_groups.py --region <region>
