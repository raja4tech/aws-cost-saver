
class DiffAnalyzer:
    def __init__(self):
        pass

    def get_ec2_diff(self, full_list, ignore_list, instances_under_elb):
        print('Full List: %s' %full_list)
        print('Instances under ELB: %s' % instances_under_elb)

        diff_list = full_list

        for act_ins_list in instances_under_elb:
            for act_ins in act_ins_list['Instances']:
                print(act_ins)
                #diff_list.remove(act_ins)
                del diff_list[act_ins]

        for ins in ignore_list:
            if diff_list.get(ins):
                del diff_list[ins]

        print('Additional Instances: ')
        print(diff_list)
        return diff_list