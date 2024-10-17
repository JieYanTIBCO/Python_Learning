#!/bin/bash
echo "Hello World!"
greeting="This is Jackie from TIBCO support"
echo $greeting

if [[ "$1" =~ ^[0-9]+$ ]]; then
        if [ $1 -gt 10 ];
                then echo "this number is greater than 10"
                else echo "this number is less than 10"
        fi
    else echo "the input is not a number"
fi
