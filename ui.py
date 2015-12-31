# -*- coding: utf-8 -*-
# import baiduBug.py
from PyQt4 import QtGui,QtCore
from ui_baiduBug import Ui_test
from baiduBug import BdBug
#Ui_test为Designer生成的类名
 
class UI(QtGui.QWidget, Ui_test):
    """QtGui.QWidget和界面设计时选择的类型一致"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self) # Ui_test.setupUi

    @QtCore.pyqtSignature("")
    def on_btn_submit_clicked(self):
        """btn_submit和界面设计时的objectName一致"""
        #获得贴吧文章ID
        post_id = self.txt_postID.text()
        post_id = str(post_id)
        myBdBug = BdBug(post_id)
        myBdBug.getTxt()
 
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = UI()
    widget.show()
    sys.exit(app.exec_())