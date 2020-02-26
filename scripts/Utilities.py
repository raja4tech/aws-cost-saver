
import boto3

class Boto3Automation:
    def __init__(self):
        self.ec2_client = boto3.client('ec2','ap-south-1')
        self.instance_type = 't2.micro'
        self.volume_size = 8

    def create_ec2_instance(self, instance_name, product, component, env):
        print('Creating instance %s' %instance_name)
        ebs_property = [
            {
                'DeviceName': '/dev/xvda',
                'Ebs': {
                    'DeleteOnTermination': True,
                    'VolumeSize': self.volume_size,
                    'VolumeType': 'gp2',
                    'Encrypted': False
                }
            }
        ]

        create_ec2_response = self.ec2_client.run_instances(
            BlockDeviceMappings=ebs_property,
            ImageId='ami-0d9462a653c34dab7',
            InstanceType=self.instance_type,
            KeyName='aws-learning-test1',
            MinCount=1,
            MaxCount=1,
            SecurityGroupIds=[
                'sg-0b2266ae6c973b4d1'
            ],
            SubnetId='subnet-84c1f0ec',
            DryRun=False,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Product',
                            'Value': product
                        },
                        {
                            'Key': 'Component',
                            'Value': component
                        },
                        {
                            'Key': 'Environment',
                            'Value': env
                        },
                        {
                            'Key': 'Name',
                            'Value': instance_name
                        }
                    ]
                }
            ]
        )

        print(create_ec2_response)

boto_handler = Boto3Automation()
boto_handler.create_ec2_instance('instance-product1-component2','product1','component2','qa')
boto_handler.create_ec2_instance('instance-product1-component3','product1','component3','qa')