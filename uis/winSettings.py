# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Kumaresan\Dev\Python\lra\uis\winSettings.ui'
#
# Created: Wed Dec 21 23:17:51 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(435, 361)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.toolBox = QtGui.QToolBox(Dialog)
        self.toolBox.setFrameShape(QtGui.QFrame.Panel)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 433, 272))
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_3 = QtGui.QGridLayout(self.page)
        self.gridLayout_3.setMargin(7)
        self.gridLayout_3.setSpacing(7)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.scrollArea = QtGui.QScrollArea(self.page)
        self.scrollArea.setFrameShape(QtGui.QFrame.Panel)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 417, 256))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.leMayaFolder = QtGui.QLineEdit(self.groupBox_2)
        self.leMayaFolder.setObjectName(_fromUtf8("leMayaFolder"))
        self.gridLayout_6.addWidget(self.leMayaFolder, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.leMayaBinFolder = QtGui.QLineEdit(self.groupBox_2)
        self.leMayaBinFolder.setObjectName(_fromUtf8("leMayaBinFolder"))
        self.gridLayout_6.addWidget(self.leMayaBinFolder, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)
        self.leMayaBatchExeFile = QtGui.QLineEdit(self.groupBox_2)
        self.leMayaBatchExeFile.setObjectName(_fromUtf8("leMayaBatchExeFile"))
        self.gridLayout_6.addWidget(self.leMayaBatchExeFile, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 4, 0, 1, 1)
        self.leMayaRenderExeFile = QtGui.QLineEdit(self.groupBox_2)
        self.leMayaRenderExeFile.setObjectName(_fromUtf8("leMayaRenderExeFile"))
        self.gridLayout_6.addWidget(self.leMayaRenderExeFile, 4, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 433, 272))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_4.setMargin(7)
        self.gridLayout_4.setSpacing(7)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea_2 = QtGui.QScrollArea(self.page_2)
        self.scrollArea_2.setFrameShape(QtGui.QFrame.Panel)
        self.scrollArea_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 417, 256))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setMargin(4)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.btnCancel = QtGui.QToolButton(self.groupBox)
        self.btnCancel.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnCancel.setAutoRaise(True)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.gridLayout_2.addWidget(self.btnCancel, 0, 3, 1, 1)
        self.btnApply = QtGui.QToolButton(self.groupBox)
        self.btnApply.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnApply.setAutoRaise(True)
        self.btnApply.setObjectName(_fromUtf8("btnApply"))
        self.gridLayout_2.addWidget(self.btnApply, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Setttings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Maya Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.leMayaFolder.setText(QtGui.QApplication.translate("Dialog", "E:\\adm\\Maya2012", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Maya folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.leMayaBinFolder.setText(QtGui.QApplication.translate("Dialog", "[MAYA_FOLDER]\\bin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Maya bin folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Maya batch exe file:", None, QtGui.QApplication.UnicodeUTF8))
        self.leMayaBatchExeFile.setText(QtGui.QApplication.translate("Dialog", "[MAYA_BIN_FOLDER]\\mayabatch.exe", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Maya render exe file:", None, QtGui.QApplication.UnicodeUTF8))
        self.leMayaRenderExeFile.setText(QtGui.QApplication.translate("Dialog", "[MAYA_BIN_FOLDER]\\render.exe", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("Dialog", "Basic Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Dialog", "Advanced Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnApply.setText(QtGui.QApplication.translate("Dialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))

