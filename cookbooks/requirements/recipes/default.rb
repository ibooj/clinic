#
# Cookbook Name:: requirements
# Recipe:: default
#

execute "pip3 install --upgrade -r /vagrant/requirements/dev.txt"
