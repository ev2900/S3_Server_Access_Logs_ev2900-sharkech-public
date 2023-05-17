# S3 Server Access Log Parser - ev2900-sharkech-public

Many of my GitHub repositories include a CloudFormation stack. The CloudFormation stack(s) can be deployed via. a button that looks like ![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png) each time this stack is deployed a YAML file defining the stack is retrieved from an S3 bucket. 

To better understand the usage of the repositories I create, I can look at the number of times the YAML file(s) corresponding to a CloudFormation stack are accessed. This is a proxy measurement of how many times a CloudFormation stack has been deployed

## How does it work

The repository has 2 python scripts. [aggregate_server_access_logs.py](https://github.com/ev2900/S3_Server_Access_Logs_ev2900-sharkech-public/blob/main/aggregate_server_access_logs.py) and [analyze_server_access_logs.py](https://github.com/ev2900/S3_Server_Access_Logs_ev2900-sharkech-public/blob/main/analyze_server_access_logs.py)

[aggregate_server_access_logs.py](https://github.com/ev2900/S3_Server_Access_Logs_ev2900-sharkech-public/blob/main/aggregate_server_access_logs.py) aggregates the many small files that store S3 server access logs into a single large file. This is not 100% necessary but it keeps the S3 bucket that holds the logs neat.

[analyze_server_access_logs.py](https://github.com/ev2900/S3_Server_Access_Logs_ev2900-sharkech-public/blob/main/analyze_server_access_logs.py) uses a regular expression to find the instances of ```REST.GET.OBJECT``` for specific YAML files and count how many times a get object request(s) were made.
