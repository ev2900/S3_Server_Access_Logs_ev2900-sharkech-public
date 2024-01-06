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

		regex = r'.*<img width="\d{1,5}" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-.*-blue">.*'

		if re.match(regex, line):
			new_line = re.sub(r'(https://img.shields.io/badge/cloudformation template deployments-)\d+(-blue)', r'\g<1>' + str(number_of_cloudformation_template_deployments) + r'\2', line)

			new_README_lines.append(new_line)

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

# OpenSearch_CloudWatch_Alarms
downloads = get_number_of_deployments("OpenSearch_cloudwatch_alarms.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_CloudWatch_Alarms", downloads)

# OpenSearch_Dashboard_Nginx_Proxy
downloads = get_number_of_deployments("opensearch_nginx.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_Dashboard_Nginx_Proxy", downloads)

# OpenSearch_kNN_Vector_Search
downloads = get_number_of_deployments("OpenSearch_kNN_Vector_Search.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_kNN_Vector_Search", downloads)

# OpenSearch_Local_Dashboard_Server
downloads = get_number_of_deployments("opensearch-dashboard-no-ssl-ecs-fargate.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_Local_Dashboard_Server", downloads)

# Glue_Aggregate_Small_Files 
downloads = get_number_of_deployments("Aggregate_Small_Parquet_File_Glue_Job_Deployment.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\Glue_Aggregate_Small_Files", downloads)

# DataZone_Demo 
downloads = get_number_of_deployments("0_datazone_cloudformation.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\DataZone_Demo", downloads)

# EMR_Studio_Deployment
downloads = get_number_of_deployments("emr_studio_demo.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\EMR_Studio_Deployment", downloads)

# OpenSearch_DynamoDB_Example 
downloads_1 = get_number_of_deployments("dynamo_lambda_opensearch.yaml")
downloads_2 = get_number_of_deployments("dynamo_lambda_opensearch_vpc.yaml")

downloads = downloads_1 + downloads_2
downloads = str(downloads).lstrip('0')

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_DynamoDB_Example", downloads)

# OpenSearch_Kafka_Anomaly_Detection
downloads = get_number_of_deployments("msk_lambda_opensearch.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_Kafka_Anomaly_Detection", downloads)

# OpenSearch_Neural_Search
downloads = get_number_of_deployments("OpenSearch_Neural_Search.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_Neural_Search", downloads)

# OpenSearch_Sigv4_IAM_Auth
downloads = get_number_of_deployments("opensearch_Sigv4.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_Sigv4_IAM_Auth", downloads)

# SecurityLake_AmazonSecurityLakeMetaStoreManager
downloads = get_number_of_deployments("AmazonSecurityLakeMetaStoreManager_IAM_Role.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\SecurityLake_AmazonSecurityLakeMetaStoreManager", downloads)

# OpenSearch_API_Examples
downloads_1 = get_number_of_deployments("OpenSearch_demo_Cloud9_simple.yaml")
downloads_2 = get_number_of_deployments("OpenSearch_cross_cluster_replication_demo.yaml") 
downloads_3 = get_number_of_deployments("OpenSearch_demo_anomaly_detection.yaml")
downloads_4 = get_number_of_deployments("OpenSearch_demo_alerting.yaml")

downloads = downloads_1 + downloads_2 + downloads_3 + downloads_4
downloads = str(downloads).lstrip('0')

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\OpenSearch_API_Examples", downloads)

# Logstash_Example
downloads = get_number_of_deployments("logstash_cloud9_s3.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\Logstash_Example", downloads)

# Kinesis_Data_Stream_Hot_Shard_Demo
'''
downloads = get_number_of_deployments("kinesis_Cloud9.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\Kinesis_Data_Stream_Hot_Shard_Demo", downloads)
'''

# Fluentd_Examples
'''
downloads_1 = get_number_of_deployments("fluentd_cloud9.yml")
downloads_2 = get_number_of_deployments("fluentd_cloud9_opensearch.yml")

downloads = downloads_1 + downloads_2
downloads = str(downloads).lstrip('0')

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\Fluentd_Examples", downloads)
'''

# Neo4j_Infrastructure
downloads_1 = get_number_of_deployments("ecr_repository.yaml")
downloads_2 = get_number_of_deployments("neo4j_ecs_ssl_self-signed.yaml") 
downloads_3 = get_number_of_deployments("neo4j_ecs_basic.yaml")

downloads = int(downloads_1) + int(downloads_2) + int(downloads_3)
downloads = str(downloads).lstrip('0')

update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\Neo4j_Infrastructure", downloads)

# DataZone_Demo_FSI
downloads = get_number_of_deployments("0_data_zone_fsi_cloudformation.yaml")
update_cloudformation_template_deployments_in_readme("C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\DataZone_Demo_FSI", downloads)