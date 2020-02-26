import json

from src.AWSCostSaverConfig import AWSCostSaverConfig
from src.AWSLayer import *
from src.DiffAnalyzer import DiffAnalyzer

print('AWS Cost Saver v1.0')

def main():
    config = AWSCostSaverConfig('../input.json')
    json_config = config.read_config()
    print('Config file contents:\n' + str(json_config))

    aws_layer = AWSEC2Layer(json_config['AWSRegion'])
    aws_elb_layer = AWSELBLayer()
    total_ec2_list = aws_layer.get_all_instances_by_tag(json_config['UniqueTags'])

    instances_under_elbs = []
    for elb in json_config['ElasticLoadBalancers']:
        ins_elb = aws_elb_layer.get_instances_under_elb( elb['Name'] )
        if ins_elb is not None:
            elb_instances_actual = {
                'Name': elb['Name'],
                'Instances': ins_elb,
                'InstanceCount': len(ins_elb)
            }
            instances_under_elbs.append(elb_instances_actual)

    print(instances_under_elbs)

    diff = DiffAnalyzer()
    diff_ec2_instances = diff.get_ec2_diff(total_ec2_list, instances_under_elbs)
    print('\n\nInstances that could be shutdown:\n')
    print('InstanceId\t\t\tInstanceName')
    for instance_id, instance_name in diff_ec2_instances.items():
        print('%s\t%s' %(instance_id, instance_name))

if __name__ == "__main__":
    main()