import archive_config as config
def create_dx_cmds(project_name,id):
    """
    take in project name eg 002_2000620_aj123 and project id (project-abc123)
    make new project name (replacing 002 with 802)
    return dx api calls to rename project and then archive
    """
    new_project_name=project_name.replace(config.project_codes_to_replace,config.new_project_code)
    return "dx api %s update \'{\"name\" : \"%s\"}\' --auth-token %s\ndx api %s archive --auth-token %s" % (id,new_project_name,config.Nexus_API_Key,id,config.Nexus_API_Key)
    

# open the file generated by `dx find projects --created-before 2019-06-01 > project_list.txt`
with open(config.project_list,'r') as project_list_file:
    project_list = project_list_file.readlines()

# line in project_list looks like:
# project-F3bZxxj0B0jpjf9b6pxJQBJk : 802_170130_NB551068_0029_AHFJY2BGX2_NGS150A_WES11 (ADMINISTER)
for line in project_list:
    # capture ID , projectname and access level
    id, name_full = line.split(":")
    name, permission = name_full.strip().split(" (")
    
    # try to extract date using underscore
    try:
        date = name.split("_")[1]
    except:
        date=""
    
    # check date is not empty and fit expected pattern (6 characters long, starting with project_years_to_archive) and name contains expected string
    if date and len(date) == 6 and date[0:2] == config.project_years_to_archive and name.startswith(config.project_codes_to_replace):
        # call function which cerates dx command
       print create_dx_cmds(name, id)
    
