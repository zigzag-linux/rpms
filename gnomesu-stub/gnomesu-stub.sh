#!/bin/bash
while [[ $# -gt 1 ]]
do
    key="$1"

    case $key in
        -c)
            COMMAND="$2"
            shift # past argument
            ;;
        *)
            ;;
    esac
    shift # past argument or value
done

lxqt-sudo --sudo $COMMAND
