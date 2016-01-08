#-*- coding:utf-8 -*-

from distutils.core import setup 
import py2exe
import sys
import baiduBug


#允许程序以双击的形式打开
sys.argv.append('py2exe')


p2yexe_options = {
	'includes':['sip','baiduBug'],
	'dll_excludes':['MSVCP90.dll'],
	'compressed':1,
	'optimize':2,
	'ascii':0,
	'bundle_files':1
}

setup(
	name = 'PyQt Demo',
	version ='1.0',
	windows = ['e:/baiduBug/ui.py'],
	zipfile = None,
	options = {'py2exe':p2yexe_options}
	)

# setup(console=[r'e://baiduBug/ui.py'])
 