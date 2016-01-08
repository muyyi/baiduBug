# -*- coding: utf-8 -*-
import urllib
import re

class BdBug(object):
	#读取相应网站
	def __init__(self,post_id):
		self.myID = post_id
		self.title = u'暂无标题.txt'
		self.page_count = 1
		print u'程序开始启动'

	def getHtml(self,url):
		html = urllib.urlopen(url)
		page = html.read()
		return page

	#提取文章标题
	def getTitle(self,page):
		reg = r'<title>(.+?)_.+?</title>'
		reg = re.compile(reg)
		title = reg.findall(page)
		title = title[0]
		return title

	#获得文章总页数
	def getCount(self,page):
		reg = re.compile(r'<span class="red">(\d+)</span>')
		count = reg.findall(page)
		count = int(count[0])
		return count

	#提取相关文本html代码
	def getContent(self,page):
		reg = r'class="d_post_content j_d_post_content ">(.+?)</div>'
		reg = re.compile(reg)
		contentlist = reg.findall(page)
		return contentlist

	#对html代码进行处理（去除空格，替换部分html标记）
	def getTxt(self,minlen=100):
		#获得标题，页面数等相关信息(调用函数内部方法或属性加上self)
		url = 'http://tieba.baidu.com/p/'+self.myID+'?see_lz=1'
		page = self.getHtml(url)
		title = self.getTitle(page).decode('utf-8')
		title = re.sub(r'[\\\/:\*\?"<>\||]',' ',title)
		print title
		self.page_count = self.getCount(page)
		self.title = title+'.txt'
		#将标题里的\ / : * ? " < > 等非法字符替换为一个空格
		f = open(self.title,'w')
		#从第一页开始抓取文章
		for i in range(1,self.page_count+1):
			#这里的i必须转化为str，不然无法连接
			url = 'http://tieba.baidu.com/p/'+self.myID+'?see_lz=1&pn='+str(i)
			page = self.getHtml(url)
			content = self.getContent(page)
			for p in content:
				string = p.replace('</','<')
				#替换<bn>为换行
				string = string.replace('<br>','\n')
				#清除图片<img>和超链接<a>及其他一些标签
				# reg = re.compile(r'<a.*?>|<img.*?>|<strong.*?>|<span.*?>')
				reg = re.compile(r'<.*?>')
				string = reg.sub('',string)
				#去掉百度贴吧每个帖子前的特殊空格
				string = string.replace('            ','')
				#对抓取的字符串进行转码，并去掉异常字符
				string = string.decode('utf-8','ignore')
				string = re.sub(r'&\w+?;',' ',string)
				#统计字数代码（调试)
				# string = '\n'+str(len(string))+'\n'+string
				#非智能筛选模式(调试)
				# minlen = 0
				if len(string)>=minlen:
					string = string.encode('utf-8')
					f.write(string)
			print u'成功抓取第%s页' %i
		f.close()
		print u'创建《%s》成功！共%s页' %(self.title,self.page_count)
		return self

def main():
	print u'请输入要抓取文章的数字链接：'
	post_id = raw_input('http://tieba.baidu.com/p/')
	myBdBug = BdBug(post_id)
	myBdBug.getTxt()

if __name__=='__main__':
	main()



