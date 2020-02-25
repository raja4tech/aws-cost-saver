import json

from src.AWSCostSaverConfig import AWSCostSaverConfig

print('AWS Cost Saver v1.0')
#
# client = boto3.client('ec2','ap-south-1')
#
# response = client.describe_security_groups()
#
# print(response)
#
# ec2_response = client.describe_instances()
#
# print(ec2_response)
#
# elb_client = boto3.client('elb','ap-south-1')
# elb_response = elb_client.describe_load_balancers()
# print(elb_response)



def main():
    config = AWSCostSaverConfig('../input.json')
    json_config = config.read_config()
    print(json_config)


if __name__ == "__main__":
    main()

