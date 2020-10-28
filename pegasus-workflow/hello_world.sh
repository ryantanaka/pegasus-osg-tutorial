#!/bin/bash

set -e

printf "I'm running on $(hostname -f)\n" > output_file.txt
printf "OSG site: $OSG_SITE_NAME\n\n" >> output_file.txt

printf "Hello OSG!\nI ran on this OS:\n" >> output_file.txt
# show OS info
cat /etc/os-release >> output_file.txt


if command -v nvidia-smi &> /dev/null
then
    printf "\nAnd here is some GPU info:\n" >> output_file.txt
    nvidia-smi >> output_file.txt
fi
