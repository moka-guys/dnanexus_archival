# define which projects looking to archive
project_codes_to_replace = "002_"
project_years_to_archive = "21"
# change project code to start with 8 eg 002-->802
new_project_code = "8" + project_codes_to_replace[1:]

# DNA Nexus authentication token
nexus_api_key_file = "/home/aled/Documents/.dnanexus_auth_token"
with open(nexus_api_key_file, "r") as nexus_api:
	Nexus_API_Key = nexus_api.readline().rstrip()
