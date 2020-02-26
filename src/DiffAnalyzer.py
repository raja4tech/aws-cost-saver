
class DiffAnalyzer:
    def __init__(self):
        pass

    def get_ec2_diff(self, full_list, actual_list):
        print('Full List: %s' %full_list)
        print('Instances under ELB: %s' %actual_list)

        diff_list = full_list

        for act_ins_list in actual_list:
            for act_ins in act_ins_list['Instances']:
                print(act_ins)
                #diff_list.remove(act_ins)
                del diff_list[act_ins]


        print('Additional Instances: ')
        print(diff_list)
        return diff_list