import boto3
import os
import re

from boto3.session import Session
from datetime import datetime

# Get credentials from aws_credentials.txt file
aws_credentials_file = open('aws_credentials.txt', 'r')

aws_credentials = aws_credentials_file.read()

aws_credentials_file.close()

ACCESS_KEY = aws_credentials.split(',')[0]
SECRET_KEY = aws_credentials.split(',')[1]

# Configure boto3 session
session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

s3 = session.resource('s3')

# Get list of all YAML files in the sharkech-logging-bucket bucket
my_bucket = s3.Bucket('sharkech-public')

cloudformation_file_names = []

for s3_object in my_bucket.objects.all():

    path, filename = os.path.split(s3_object.key)

    if filename.endswith(".yaml"):
    	cloudformation_file_names.append(path + "/" + filename)

# Open log file and write each line to a list
with open("./Aggregated_Server_Access_Logs/" + datetime.today().strftime('%Y-%m-%d')) as file:
	log_file_lines = [line.rstrip() for line in file]
file.close()

# Open output file to write results to
output_results_file = open("Server_Access_Log_Data/" + datetime.today().strftime('%Y-%m-%d') + ".csv", "w")
output_results_file.write("Filename,Number of Object Get Resquests\n")

for cloudformation_file_name in cloudformation_file_names:

	downloads = 0

	for line in log_file_lines:

		regex = r".*REST.GET.OBJECT " + cloudformation_file_name
		
		if re.match(regex, line):
			downloads = downloads + 1

	output_results_file.write(cloudformation_file_name + "," + str(downloads) + "\n")

output_results_file.close()