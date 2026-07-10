#!/bin/bash
set -e


containerID=`sudo docker ps -a | awk -F" " "{print $1}"`
sudo docker rm -f $containerID
