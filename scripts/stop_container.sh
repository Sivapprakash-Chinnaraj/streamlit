#!/bin/bash
set -e


containerID= `sudo docker ps -a | awk -F" " "Print $1"`
sudo docker rm $containerID
