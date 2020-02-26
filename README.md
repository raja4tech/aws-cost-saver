# aws-cost-saver [Work In Progress]
Set of python scripts that helps in monitoring AWS costs

# Goal of the Project:
To monitor & save AWS infrastructure costs.

# Problem Statement
1. In an agile world, where we are releasing softwares very frequently it becomes a nightmare to maintain AWS environments.
2. For eg. if we are following Blue/Green deployment model, we tend to have the older stack/auto scaling group for sometime before cleaning up.
3. If there are multiple components which share the same environment and multiple teams sharing the same AWS account, it can become a nightmare to properly delete the appropriate stacks/auto scaling groups.

Idea of this project:
1. Have a benchmark list of items required for the project in the form of a config. I'm visualizing something like below (Although it could change in the future)

ELB:
  - component1:
    elb_name: elb-component-1
    num_healthy_instances: 3
  - component2:
    elb_name: elb-component-2
    num_healthy_instances: 4
EC2: <Instances that aren't under ELB>
RDS:
ECS:
General_Ignore_List:

# Roadmap
1. Script to find out unwanted instances -   
- [ ] Basic working version - Based on tags that can uniquely identify a particular product/project/category, find out unwanted instances
- [ ] Add support for instances that are not under ELB. Eg. DB instances, server running Cron jobs, etc.  
- [ ] Add support for Application Load Balancers & Target Groups
- [ ] Add suppport for Network Load Balancers
- [ ] Prioritize other resources
