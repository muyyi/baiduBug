# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baiduBug.ui'
#
# Created: Sun Dec 27 19:04:02 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName(_fromUtf8("test"))
        test.resize(400, 265)
        self.label = QtGui.QLabel(test)
        self.label.setGeometry(QtCore.QRect(60, 80, 151, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.txt_postID = QtGui.QLineEdit(test)
        self.txt_postID.setGeometry(QtCore.QRect(220, 80, 113, 20))
        self.txt_postID.setObjectName(_fromUtf8("txt_postID"))
        self.ckb_fifter = QtGui.QCheckBox(test)
        self.ckb_fifter.setGeometry(QtCore.QRect(60, 130, 71, 16))
        self.ckb_fifter.setChecked(True)
        self.ckb_fifter.setObjectName(_fromUtf8("ckb_fifter"))
        self.btn_submit = QtGui.QPushButton(test)
        self.btn_submit.setGeometry(QtCore.QRect(90, 210, 75, 23))
        self.btn_submit.setObjectName(_fromUtf8("btn_submit"))
        self.btn_exit = QtGui.QPushButton(test)
        self.btn_exit.setGeometry(QtCore.QRect(220, 210, 75, 23))
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.label_2 = QtGui.QLabel(test)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 231, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lab_message = QtGui.QLabel(test)
        self.lab_message.setGeometry(QtCore.QRect(90, 170, 231, 16))
        self.lab_message.setText(_fromUtf8(""))
        self.lab_message.setObjectName(_fromUtf8("lab_message"))
        self.txt_minCount = QtGui.QLineEdit(test)
        self.txt_minCount.setGeometry(QtCore.QRect(170, 130, 41, 20))
        self.txt_minCount.setObjectName(_fromUtf8("txt_minCount"))
        self.label_4 = QtGui.QLabel(test)
        self.label_4.setGeometry(QtCore.QRect(140, 130, 31, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(test)
        self.label_5.setGeometry(QtCore.QRect(220, 130, 121, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(test)
        QtCore.QObject.connect(self.ckb_fifter, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.txt_minCount.setEnabled)
        QtCore.QObject.connect(self.btn_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), test.close)
        QtCore.QMetaObject.connectSlotsByName(test)

    def retranslateUi(self, test):
        test.setWindowTitle(_translate("test", "百度贴吧爬虫 by muyyi ver.1.0", None))
        self.label.setText(_translate("test", "http://tieba.baidu.com/p/", None))
        self.ckb_fifter.setText(_translate("test", "智能筛选：", None))
        self.btn_submit.setText(_translate("test", "确定", None))
        self.btn_exit.setText(_translate("test", "退出", None))
        self.label_2.setText(_translate("test", "请输入贴吧的地址最后的数字串：", None))
        self.txt_minCount.setText(_translate("test", "100", None))
        self.label_4.setText(_translate("test", "少于", None))
        self.label_5.setText(_translate("test", "字的主题帖将被过滤", None))

