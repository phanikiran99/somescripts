# -*- coding: utf-8 -*-
"""
Script to search for a file pattern and print its path in console 
@ Version - Init V1.0
@ Author: Phani
@ Pyton version : 3+ 
"""

import os
from fnmatch import fnmatch

root = 'c://phani//'   #Change the Path as Desired
pattern = '*111*que*.txt' #Change the patter to desired 

for path,subdirs,files in os.walk(root):
	for name in files:
		if fnmatch(name,pattern):
			print(os.path.join(name))

#End of Script
