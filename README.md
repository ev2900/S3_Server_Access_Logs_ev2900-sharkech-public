# S3 Server Access Log Parser - ev2900-sharkech-public

Many of my GitHub repositories include a CloudFormation stack. The CloudFormation stack(s) can be deployed via. a button that looks like ![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png) each time this stack is deployed a YAML file defining the stack is retrieved from an S3 bucket. 

To better understand the usage of the repositories I create, I can look at the number of times the YAML file(s) corresponding to a CloudFormation stack are accessed. This is a proxy measurement of how many times a CloudFormation stack has been deployed

## How does it work

