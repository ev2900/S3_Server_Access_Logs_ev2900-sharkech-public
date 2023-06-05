import os 
import re

from datetime import datetime

#
# OpenSearch_CloudWatch_Alarms
#

with open("./Server_Access_Log_Data/" + datetime.today().strftime('%Y-%m-%d') + ".csv") as file:
	server_access_log_agg_results = [line.rstrip() for line in file]
file.close()

# Get the number of GET OBJECTs for the repository
for line in server_access_log_agg_results:

	regex = r"misc-public/OpenSearch_cloudwatch_alarms.yaml.*"
		
	if re.match(regex, line):
		split_line = line.split(",")
		openSearch_cloudWatch_alarms_downloads = split_line[1]

# Git pull on the OpenSearch_CloudWatch_Alarms repo
os.system("git -C C:\\Users\\sharkech\\Desktop\\GitHub\\OpenSearch_CloudWatch_Alarms pull")
print("Git pull on OpenSearch_CloudWatch_Alarms")

# Open the README for OpenSearch_CloudWatch_Alarms
with open("C:/Users/sharkech/Desktop/GitHub/OpenSearch_CloudWatch_Alarms/README.md") as README_file:
	README_lines = [line.rstrip() for line in README_file]
README_file.close()

new_README_lines = []

for line in README_lines:

	regex = r'<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-.*-blue">'

	if re.match(regex, line):
		new_README_lines.append('<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-' + str(openSearch_cloudWatch_alarms_downloads) + '-blue">')
	else:
		new_README_lines.append(line)

new_README_file = open("C:/Users/sharkech/Desktop/GitHub/OpenSearch_CloudWatch_Alarms/README.md", "w")

for line in new_README_lines:
	new_README_file.write(line + "\n")

new_README_file.close()

os.system("git -C C:\\Users\\sharkech\\Desktop\\GitHub\\OpenSearch_CloudWatch_Alarms add .")
os.system('git -C C:\\Users\\sharkech\\Desktop\\GitHub\\OpenSearch_CloudWatch_Alarms commit -m "Updating downloads"')
os.system("git -C C:\\Users\\sharkech\\Desktop\\GitHub\\OpenSearch_CloudWatch_Alarms push")