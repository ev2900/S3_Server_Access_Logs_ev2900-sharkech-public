# S3 Server Access Log Parser - ev2900-sharkech-public

Many of my GitHub repositories include a CloudFormation stack. The CloudFormation stack(s) can be deployed via. a button that looks like ![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png) each time this stack is deployed a YAML file defining the stack is retreived from an S3 bucket. 

To better understand the usage of the repositories I create, I can look at the number of times the YAML file coresponding to a CloudFormation stack is accessed. This is a mesurement of how many time a CloudFormation stack may have been deployed
