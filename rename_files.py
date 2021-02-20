# coding:utf-8

"""files operations
1、可以批量的修改文件夹下的所有文件名称
2、可以批量替换文件名称中的一些字符
3、可以指定符合正则匹配的文件进行操作
4、可以指定操作文件夹，默认是只操作文件
"""

__author__ = '共产主义接班人'
__version__ = '1.0'

import argparse
import os
import re
import platform

platform_name = platform.system().lower()
pwd = os.getcwd()

parser = argparse.ArgumentParser(description='批量地干活')
parser.add_argument('-r', '--rename', type=str,
					help='-r "test%%02d.jpg .*.jpg" ==> 将所有符合.*.jpg的文件名称修改为test开头的文件名，第一个文件为test00.jpg')
parser.add_argument('-R', '--replace', help='替换文件名称中的一些字符，例：-R "x y" 将名称中的x替换成y')
parser.add_argument('-m', '--match', help='匹配符合的文件进行操作')
parser.add_argument('-i', '--ignore-case', default=True, help='匹配忽略大小写')
parser.add_argument('-p', '--path', default=pwd, help='操作文件夹的路径, 默认为当前路径')
parser.add_argument('-c', '--create-dir', help='创建一个新的文件夹作为存储路径，也可以指定已存在的文件夹进行存放，默认当前文件夹')
args = parser.parse_args()
parser.print_help()

rename = args.__dict__['rename'].strip()
replace = args.__dict__['replace'].strip()
path = args.__dict__['path']
ignore_case = args.__dict__['ignore_case']
create_dir = args.__dict__['create_dir']
if ignore_case:
	flags=re.IGNORECASE
if create_dir:
	if not os.path.exists(create_dir):
		os.mkdir(create_dir)
else:
	create_dir=path

def rename_files(target, pattern=r'.*'):
	if platform_name in ['linux','unix']:
		for root, dirs, files in os.walk(path):
			for i, file in enumerate(files):
				abs_path = os.path.join(root, file)
				if abs_path == os.path.abspath(__file__) or file.startswith('.'):  # 避免修改自己和隐藏文件(目前只支持linux隐藏文件)
					continue
				if re.match(pattern, file, flags=flags):
					os.rename(abs_path, os.path.join(create_dir, target%(i+1)))
	else:
		for root, dirs, files in os.walk(path):
			for i, file in enumerate(files):
				abs_path = os.path.join(root, file)
				if abs_path == os.path.abspath(__file__):  # 避免修改自己
					continue
				if re.match(pattern, file, flags=flags):
					os.rename(abs_path, os.path.join(create_dir, target%(i+1)))

def replace_files(old_replace, new_replace, pattern=r'.*'):
	if platform_name in ['linux','unix']:
		for root, dirs, files in os.walk(path):
				for file in files:
					abs_path = os.path.join(root, file)
					if abs_path == os.path.abspath(__file__) or file.startswith('.'):
						continue
					if re.match(pattern, file, flags=flags) and re.match(new_replace, file, flags=flags):
						os.rename(abs_path, os.path.join(create_dir, file.replace(old_replace, new_replace)))
	else:
		for root, dirs, files in os.walk(path):
				for file in files:
					abs_path = os.path.join(root, file)
					if abs_path == os.path.abspath(__file__):
						continue
					if re.match(pattern, file, flags=flags) and re.match(new_replace, file, flags=flags):
						os.rename(abs_path, os.path.join(create_dir, file.replace(old_replace, new_replace)))

if rename:
	rename_list = rename.split(' ')
	if len(rename_list)==1:
		rename_list.append(r'.*')
	rename_files(rename_list[0], rename_list[1])
elif replace:
	replace_list = replace.split(' ')
	replace_files(replace_list[0], replace_list[1])
else:
	rename_list = ['%d', r'.*']
	rename_files(rename_list[0], rename_list[1])
