# readme

这是我的第一个python小程序
用于抓取百度贴吧里的原创文章并存储为本地的txt文件
15/12/23开坑，预计一周完成，我会在这里记录下实现这个程序的全过程
也算给自己留下一些动力和回忆吧

12/23
项目正式开坑。
思路：
利用urllib类和re类抓取指定链接文章里的内容，将部分标签（如<br>）进行处理后，将其保存到txt文件里。
实现：
ver.1.0版，用户可以输入链接后的数字，抓取相应的文章，但是只能抓取第一页，且文章中的超链接部分无法处理，待后续完善


12/24
项目模块化。
思路：
将面向过程的程序改为面向对象的模块，增强复用性
抓取多页思路：
先提取首页的页码数，然后循环抓取每个页面的内容
删除标签思路：
先将标签统一转化为不带/的形式，例如<a>,<img>等，然后用re.sub方法将其替换成‘’

实现：完成了抓取多页和去标签的功能
初步了解了pyqt图形库。尚未开始模块化改造，待后续一并实现

12/25
项目图形化
思路：
利用pyqt库，先用desiner设计出界面，然后实例化该类即可
同时将进行逻辑处理的最初代码模块化