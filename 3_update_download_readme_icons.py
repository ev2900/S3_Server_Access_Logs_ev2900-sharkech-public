import os 
import re

from datetime import datetime

# Create function to get the number of GET OBJECTs for a given repository
def get_number_of_deployments(yaml_file_name):

	# Open the input file with the number of CloudFormation download for each repo
	with open("./Server_Access_Log_Data/" + datetime.today().strftime('%Y-%m-%d') + ".csv") as file:
		server_access_log_agg_results = [line.rstrip() for line in file]
	file.close()

	# Match the name of the yaml file with a regex
	for line in server_access_log_agg_results:
 
		if re.match(r"misc-public/" + yaml_file_name + ".*", line):
			split_line = line.split(",")
			number_of_downloads = split_line[1]

	return number_of_downloads

# Create function to update the cloudformation template deployments in the read me
def update_cloudformation_template_deployments_in_readme (repo_path, number_of_cloudformation_template_deployments):

	# Git pull
	os.system("git -C " + repo_path + " pull")

	# Open the README
	with open(repo_path + "\\README.md") as README_file:
		README_lines = [line.rstrip() for line in README_file]
	README_file.close()

	new_README_lines = []

	for line in README_lines:

		regex = r'<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-.*-blue">'

		if re.match(regex, line):
			new_README_lines.append('<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-' + str(number_of_cloudformation_template_deployments) + '-blue">')
		else:
			new_README_lines.append(line)

	new_README_file = open(repo_path + "\\README.md", "w")

	for line in new_README_lines:
		new_README_file.write(line + "\n")

	new_README_file.close()

	# Git push
	os.system("git -C " + repo_path + " add .")
	os.system('git -C ' + repo_path + ' commit -m "Updating downloads"')
	os.system("git -C " + repo_path + " push")

	# Print the number of deployments
	print("Number of " + repo_path.split('\\')[-1].replace('_', ' ') + " downloads = " + str(number_of_cloudformation_template_deployments))

#
# OpenSearch_CloudWatch_Alarms
#

openSearch_cloudWatch_alarms_downloads = get_number_of_deployments("OpenSearch_cloudwatch_alarms.yaml")

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_CloudWatch_Alarms", openSearch_cloudWatch_alarms_downloads)

#
# OpenSearch_Dashboard_Nginx_Proxy
#

openSearch_dashboard_nginx_proxy_downloads = get_number_of_deployments("opensearch_nginx.yaml")

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_Dashboard_Nginx_Proxy", openSearch_dashboard_nginx_proxy_downloads)

#
# OpenSearch_kNN_Vector_Search
#

openSearch_kNN_vector_search_downloads = get_number_of_deployments("OpenSearch_kNN_Vector_Search.yaml")

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_kNN_Vector_Search", openSearch_kNN_vector_search_downloads)

#
# OpenSearch_Local_Dashboard_Server
#

openSearch_local_dashboard_server_downloads = get_number_of_deployments("opensearch-dashboard-no-ssl-ecs-fargate.yaml")

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_Local_Dashboard_Server", openSearch_local_dashboard_server_downloads)

#
# Glue_Aggregate_Small_Files 
#

glue_aggregate_small_files_downloads = get_number_of_deployments("Aggregate_Small_Parquet_File_Glue_Job_Deployment.yaml")

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\Glue_Aggregate_Small_Files", glue_aggregate_small_files_downloads)

#
# DataZone_Demo 
#

dataZone_demo_downloads = get_number_of_deployments("0_datazone_cloudformation.yaml")

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\DataZone_Demo", dataZone_demo_downloads)