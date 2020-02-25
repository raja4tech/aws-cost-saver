import json

from src.AWSCostSaverConfig import AWSCostSaverConfig
from src.AWSLayer import AWSLayer

print('AWS Cost Saver v1.0')

def main():
    config = AWSCostSaverConfig('../input.json')
    json_config = config.read_config()
    print(json_config)

    aws_layer = AWSLayer(json_config['AWSRegion'])
    aws_layer.get_all_instances_by_tag(json_config['UniqueTags'])

    for elb in json_config['ElasticLoadBalancers']:
        ins_elb = aws_layer.get_instances_under_elb( elb['Name'] )
        if ins_elb is not None:
            elb_instances_actual = {
                'Name': elb['Name'],
                'Instances': ins_elb,
                'InstanceCount': len(ins_elb)
            }

    print(elb_instances_actual)

if __name__ == "__main__":
    main()