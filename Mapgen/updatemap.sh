#!/bin/bash

# Infinite loop to repeatedly execute git commands
while true
do
    # Change to the directory where your Git repository is located
   

    # Execute the Git commands


    python3.11 Mapgen/MapGenerator.py


    # Sleep for 1 minute before running the loop again
    echo -e "Checking again in 10min...\n"
    sleep 10


done
