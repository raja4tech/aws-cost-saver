import boto3


class AWSEC2Layer:
    def __init__(self, region):
        #self.unique_tags = tags
        self.client = boto3.client('ec2', region)
        self.running_instance_list = []

    def get_all_instances_by_tag(self, tags):
        print('Getting all instances by Tag:')
        self.unique_tags = tags
        filters = self.unique_tags
        filters.append(
            {
                "Name": "instance-state-name",
                "Values": ["running"]
            }
        )

        try:
            instance_dict = {}
            ec2_response = self.client.describe_instances(Filters=filters)
            print(ec2_response)
            for reservation in ec2_response['Reservations']:
                for instance in reservation['Instances']:
                    print(instance['InstanceId'])
                    instance_id = instance['InstanceId']
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name':
                            print(tag['Value'])
                            instance_name = tag['Value']
                            instance_dict[instance_id] = instance_name

                    self.running_instance_list.append({
                        'InstanceId': instance_id,
                        'InstanceName': instance_name
                    })
        except Exception as ex:
            print(ex.message())

        return instance_dict


class AWSELBLayer:
    def __init__(self):
        self.elb_client = boto3.client('elb')

    def get_instances_under_elb(self, elb_name):

        try:

            elb_response = self.elb_client.describe_load_balancers(
                LoadBalancerNames = [elb_name]
            )
            print(elb_response)
            instances_under_elb = []

            for lb in elb_response['LoadBalancerDescriptions']:
                for ins in lb['Instances']:
                    print(ins['InstanceId'])
                    instances_under_elb.append(ins['InstanceId'])
            return instances_under_elb

        except Exception as ex:
            print(str(ex))
            return None