# dnanexus_archival

This repo contains some scripts used to periodically archive projects in DNA Nexus.

The config script can be used to define the prefixes to be used to select and rename projects.

The input is a file generated with the command `dx find projects --created-before 2019-06-01 --auth-token abc123 > project_list.txt`
This command is sued to make sure only old projects are archived (eg those older than 6 months)

This input file is then hardcoded in the script.

For each project in that list if it starts with the desired prefix (eg 002) and year (eg 20) the script will ouput a command to rename the project eg `002_ --> 802_` and an archive command

These commands can then be written to file or copied and pasted into the terminal.

### to note
Please note, currently 003_ projects are not archived as this can cause issues with inputs to workflows being randomly selected from projects, including from archived projects and this can stop workflows from running.
