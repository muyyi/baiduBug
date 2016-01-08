# -*- coding: utf-8 -*-
from PyQt4 import QtGui,QtCore
from ui_baiduBug import Ui_test
from baiduBug import BdBug
# __import__('baiduBug')
# m = sys.modules['baiduBug']
# baiduBug_base_path = m.__path__[0]
import sip 
#Ui_test为Designer生成的类名
 
class UI(QtGui.QWidget, Ui_test ,QThread):
    """QtGui.QWidget和界面设计时选择的类型一致"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self) # Ui_test.setupUi

    @QtCore.pyqtSignature("")
    def on_btn_submit_clicked(self):
        """btn_submit和界面设计时的objectName一致"""
        self.lab_message.setText(u'程序开始启动，请稍后...')
        # 获得贴吧文章ID
        post_id = self.txt_postID.text()
        post_id = str(post_id)
        workThread.trigger[str].connect(timeStop) 
        # myBdBug = BdBug(post_id)
        # if self.ckb_fifter.isChecked():
        #     try:
        #         minlen = int(self.txt_minCount.text())
        #     except:
        #         minlen = 100
        #     txt = myBdBug.getTxt(minlen)
        # else:    
        #     txt = myBdBug.getTxt()
        # str_message = u'创建《'+txt.title+u'》成功！共'+txt.page_count+u'页'
        # self.lab_message.setText(str_message)

class WorkThread(QThread):  
    trigger = QtCore.pyqtSignal(str)  #定义一个信号(字符串参数)
    def __int__(self):  
        super(WorkThread,self).__init__()  
  
    def run(self,post_id):  #定义一个槽(要执行的跨线程事件)
        myBdBug = BdBug(post_id)
        if self.ckb_fifter.isChecked():
            try:
                minlen = int(self.txt_minCount.text())
            except:
                minlen = 100
            txt = myBdBug.getTxt(minlen)
        else:    
            txt = myBdBug.getTxt(0)
        str_message = u'创建《'+txt.title+u'》成功！共'+txt.page_count+u'页'
        self.lab_message.setText(str_message)



 
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = UI()
    widget.show()
    sys.exit(app.exec_())