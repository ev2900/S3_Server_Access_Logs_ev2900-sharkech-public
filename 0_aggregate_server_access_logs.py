import boto3
import os

from boto3.session import Session
from datetime import datetime
from os import walk

#
# Download server access logs
#

# Create directory Raw_Server_Access_Logs/ if it does not exist
isExist = os.path.exists('Raw_Server_Access_Logs/')

if not isExist:
    os.makedirs('Raw_Server_Access_Logs/')

    print('Created folder Raw_Server_Access_Logs/')

print('Downloading S3 server access logs ...')

# Get credentials from aws_credentials.txt file
aws_credentials_file = open('aws_credentials.txt', 'r')

aws_credentials = aws_credentials_file.read()

aws_credentials_file.close()

ACCESS_KEY = aws_credentials.split(',')[0]
SECRET_KEY = aws_credentials.split(',')[1]

# Configure boto3 session
session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

s3 = session.resource('s3')

# List and download all file in the sharkech-logging-bucket bucket
my_bucket = s3.Bucket('sharkech-logging-bucket')

server_access_logs = []
server_access_logs_s3_keys = []

for s3_object in my_bucket.objects.all():

    path, filename = os.path.split(s3_object.key)
    
    my_bucket.download_file(s3_object.key, 'Raw_Server_Access_Logs/' + filename)

    server_access_logs.append(filename)
    server_access_logs_s3_keys.append(s3_object.key)

#
# Aggregate the many server access logs into a single large file
#

print('Aggregating server access logs ...')

# Create folder Aggregated_Server_Access_Logs/ if it doesn't exist
isExist = os.path.exists('Aggregated_Server_Access_Logs/')

if not isExist:
    os.makedirs('Aggregated_Server_Access_Logs/')

    print('Created Aggregated_Server_Access_Logs/')

# If the folder Aggregated_Server_Access_Logs/ delete the files in it
if isExist:

    aggregated_server_access_logs = next(walk('Aggregated_Server_Access_Logs/'), (None, None, []))[2]
    
    for aggregated_access_log in aggregated_server_access_logs:

        os.remove('Aggregated_Server_Access_Logs/' + aggregated_access_log)

    print('Deleted files in Aggregated_Server_Access_Logs/')


# Aggregate the server access logs
agg_server_access_logs_file = open('Aggregated_Server_Access_Logs/' + datetime.today().strftime('%Y-%m-%d'), 'w')

for access_log in server_access_logs:
    
    access_log_file = open('Raw_Server_Access_Logs/' + access_log, "r")

    for line in access_log_file:

        agg_server_access_logs_file.write(line)

    access_log_file.close()

agg_server_access_logs_file.close()

#
# Delete unaggregated server access logs from local Raw_Server_Access_Logs/ folder
# 

# Delete the files in the local Raw_Server_Access_Logs/ folder
print('Delete local unaggregated server access logs ...')

for access_log in server_access_logs:

   os.remove('Raw_Server_Access_Logs/' + access_log)

# Delete the Raw_Server_Access_Logs/ directory
if isExist:
    
    os.rmdir('Raw_Server_Access_Logs/')

    print('Deleted folder Raw_Server_Access_Logs/')

#
# Delete unaggregated server access logs from S3
# 
print('Delete unaggregated S3 server access logs ...')

for server_access_log_s3_key in server_access_logs_s3_keys:

    s3.Object('sharkech-logging-bucket', server_access_log_s3_key).delete()

#
# Uploaded aggregated server access logs from S3
# 

print('Upload aggregated S3 server access log file ...')

s3.Bucket('sharkech-logging-bucket').upload_file('Aggregated_Server_Access_Logs/' + datetime.today().strftime('%Y-%m-%d'), 'sharkech-public/' + datetime.today().strftime('%Y-%m-%d'))