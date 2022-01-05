# dnanexus_archival

This repo contains some scripts used to periodically archive projects in DNA Nexus.
### project list input
The input is a file generated with the command `dx find projects --created-before 2019-06-01 --auth-token abc123 > project_list.txt`

This command ensures only old projects are archived (eg those older than 6 months). The path to this file is defined in the config file.
### config script
The config script can be used to define the prefixes to be used to select and rename projects.
This includes the prefix of projects to be archived (eg 002) and the year (eg 21)

### How this code works.
For each project in the input list the script will ouput commands to rename the project (changing prefix from 002_ --> 802) and archive if the project  starts with the desired prefix (eg 002) and year (eg 20)

These commands can then be written to file or copied and pasted into the terminal.

### to note
Please note, currently 003_ projects are not archived as this can cause issues with inputs to workflows being randomly selected from projects, including from archived projects and this can stop workflows from running.
