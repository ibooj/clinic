#!/bin/bash
sudo apt-get update
sudo apt-get -y install python3 python3-dev python3-pip
sudo pip3 install --upgrade -r requirements/dev.txt
echo -e "\033[1mlogin: admin\033[0m";
echo -e "\033[1mpassword: 123456\033[0m";
sudo python3 manage.py runserver 0.0.0.0:80
