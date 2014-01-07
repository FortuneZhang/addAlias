#!/bin/bash
import getpass
import os
home_dir = "/home/{user}/".format(user=getpass.getuser())
"""
	readme 
	1st: check if .bashrc exist ,yes return 
	2st :check bash_alias has exist, yes return 
	3st: add source  bash_alias  to bashrc
	4st: add alias to bash_alias

"""

# add source bash_alias to bashrc
alias_file_exist = False
bashrc_file_dir = os.path.join(home_dir, '.bashrc')

if not os.path.exists(bashrc_file_dir):
	print('can not find bashrc file.')
	
#checking source file has exist
bashrc_file = open(bashrc_file_dir)
for line in bashrc_file:
	if line.find('[ -f ~/.bash_alias  ] && . ~/.bash_alias') != -1:
		alias_file_exist = True
		break
bashrc_file.close()

if not alias_file_exist:
	bashrc_file = open(bashrc_file_dir, 'a')
	print>> bashrc_file, '[ -f ~/.bash_alias  ] && . ~/.bash_alias'
	bashrc_file.close()

#add alias to bash_alias
bash_alias_file_path  = os.path.join(home_dir, '.bash_alias')

if  os.path.exists(bash_alias_file_path):
	bash_alias_file = open(bash_alias_file_path,'a')
	add_alias_path = os.path.join(os.path.abspath(os.getcwd()), 'addAlias.py')
	print >> bash_alias_file, ('alias addAlias=\'python {add_alias_path} && source ~/.bash_alias \''.format(add_alias_path=add_alias_path))
	bash_alias_file.close






