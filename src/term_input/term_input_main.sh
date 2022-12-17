#!/bin/bash   


# check if python installed

if ! ( command -v python &> /dev/null ||  command -v python3 &> /dev/null)
then
        echo 'neither python nor python3 could not be found'
        echo ' installing python3'
        python3 - venv app-venv
        source app-venv/bin/activate
        pip install -r requirements.txt
        exit
fi



python3 term_input_main.py




chmod +x term_input_main_bin

# ./Calculator_main