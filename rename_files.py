import argparse
import os
import re

pwd = os.getcwd()

parser = argparse.ArgumentParser(description='批量地干活')
parser.add_argument('-r', '--rename', type=str, help='-r "test%%02d.jpg .*.jpg" ==> 将所有符合.*.jpg的文件名称修改为test开头的文件名，第一个文件为test001.jpg')
parser.add_argument('-p', '--path', default=pwd, help='文件夹路径, 默认为当前路径')
args = parser.parse_args()

rename = args.__dict__['rename']
if rename:
	rename_list = rename.split(' ')
	rename_list.append(r'.*')
else:
	rename_list = ['%d', r'.*']

def rename_file(target, pattern=r'.*'):
	for root, dirs, files in os.walk(args.__dict__['path']):
		for i, file in enumerate(files):
			abs_path = os.path.join(root, file)
			if abs_path==os.path.abspath(__file__):
				continue
			if re.match(pattern, file):
				os.rename(abs_path, os.path.join(root, target%i))
rename_file(rename_list[0], rename_list[1])

