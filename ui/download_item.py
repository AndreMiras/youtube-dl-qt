# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/download_item.ui'
#
# Created: Sun Feb 16 20:06:27 2014
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_DownloadItem(object):
    def setupUi(self, DownloadItem):
        DownloadItem.setObjectName(_fromUtf8("DownloadItem"))
        DownloadItem.resize(670, 48)
        self.gridLayout = QtGui.QGridLayout(DownloadItem)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.progressBar = QtGui.QProgressBar(DownloadItem)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.urlLabel = QtGui.QLabel(DownloadItem)
        self.urlLabel.setText(_fromUtf8(""))
        self.urlLabel.setObjectName(_fromUtf8("urlLabel"))
        self.gridLayout.addWidget(self.urlLabel, 0, 0, 1, 1)

        self.retranslateUi(DownloadItem)
        QtCore.QMetaObject.connectSlotsByName(DownloadItem)

    def retranslateUi(self, DownloadItem):
        DownloadItem.setWindowTitle(_translate("DownloadItem", "Form", None))

