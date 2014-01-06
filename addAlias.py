#!/bin/bash
import os
import getpass
home_dir = "/home/{user}/".format(user=getpass.getuser())

print('this is an example! if you want add alias like \"alias me=\'I\'m fortune\'\"  ')
print('input alias :me')
print('input alias detail : I\'m fortune')
print

alias_shortening=raw_input('input alias :')
alias_detail=raw_input('input alias detail :')
alias_info = "alias {shortening}='{detail}'".format(shortening=alias_shortening.strip(), detail=alias_detail.strip())
print(alias_info)

alias_file_path = os.path.join(home_dir, '.bash_alias')
if not os.path.exists(alias_file_path):
	print('.bash_alias file not exist, you can do \' python setup.py \' in your clone floder')
	return 
else:
	alias_file = open(alias_file_path, 'a')
	print >> alias_file, alias_info
	alias_file.close

