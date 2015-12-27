# coding=utf-8

import urllib
import re

#读取相应网站
def getHtml(url):
	html = urllib.urlopen(url)
	page = html.read()
	return page

#提取文章标题
def getTitle(page):
	reg = r'<title>(.+?)_.+?</title>'
	reg = re.compile(reg)
	title = reg.findall(page)
	title = title[0]
	return title

#获得文章总页数
def getCount(page):
	reg = compile(r'<span class="red">(\d+)</span>')
	count = reg.findall(page)
	count = int(count[0])
	return count

#提取相关文本html代码
def getContent(page):
	reg = r'class="d_post_content j_d_post_content ">(.+?)</div>'
	reg = re.compile(reg)
	contentlist = reg.findall(page)
	return contentlist

#对html代码进行处理（去除空格，替换部分html标记）
def getTxt(post_id):
	#获得标题，页面数等相关信息
	url = 'http://tieba.baidu.com/p/'+post_id+'?see_lz=1'
	page = getHtml(url)
	title = getTitle(page)
	count = getCount(page)
	title = (title+'.txt').decode('utf-8')
	f = open(title,'w')
	#从第一页开始抓取文章
	for i in rank(1,count+1):
		url = 'http://tieba.baidu.com/p/'+post_id+'?see_lz='+i
		content = getCount(getHtml(url))
		for p in content:
			#将标签统一为不带/的形式，如<a>
			string = p.replace('</','<')
			#替换<bn>为换行
			string = string.replace('<br>','\n')
			#清除图片<img>和超链接<a>
			reg = re.compile(r'<a.*?>|<img.*?>')
			string = reg.sub('',string)
			f.write(string)
	f.close()
	print u'创建《%s》成功！' %title

print u'请输入要抓取文章的数字链接：'
post_id = raw_input('http://tieba.baidu.com/p/')
getTxt(post_id)
