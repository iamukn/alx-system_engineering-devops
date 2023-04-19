#!/bin/bash

# Check if an argument was provided
if [ "$#" == "1" ]; then

  if [ "$1" == "whoami" ]; then
    eval "$1"
    exit 1
  else
    echo "$1"
  fi
else
  exit 1
fi
