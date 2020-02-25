import boto3

class AWSLayer:
    def __init__(self, region):
        #self.unique_tags = tags
        self.client = boto3.client('ec2', region)
        self.running_instance_list = []

    def get_all_instances_by_tag(self, tags):
        self.unique_tags = tags
        filters = self.unique_tags
        filters.append(
            {
                "Name": "instance-state-name",
                "Values": ["stopped"]
            }
        )

        try:
            ec2_response = self.client.describe_instances(Filters=filters)
            print(ec2_response)
            for reservation in ec2_response['Reservations']:
                for instance in reservation['Instances']:
                    print(instance['InstanceId'])
                    self.running_instance_list.append(instance['InstanceId'])
        except Exception as ex:
            print(ex.message())

    def get_instances_under_elb(self, elb_name):

        try:

            elb_client = boto3.client('elb')
            elb_response = elb_client.describe_load_balancers(
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