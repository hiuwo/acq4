# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/util/DirTreeWidget/DirTreeTemplate.ui'
#
# Created: Wed May 18 20:44:18 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(282, 285)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.titleLabel = QtGui.QLabel(Form)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 2)
        self.newBtn = QtGui.QPushButton(Form)
        self.newBtn.setObjectName(_fromUtf8("newBtn"))
        self.gridLayout.addWidget(self.newBtn, 0, 2, 1, 1)
        self.loadBtn = QtGui.QPushButton(Form)
        self.loadBtn.setObjectName(_fromUtf8("loadBtn"))
        self.gridLayout.addWidget(self.loadBtn, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(88, 77, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.saveBtn = QtGui.QPushButton(Form)
        self.saveBtn.setEnabled(False)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.gridLayout.addWidget(self.saveBtn, 3, 2, 1, 1)
        self.saveAsBtn = QtGui.QPushButton(Form)
        self.saveAsBtn.setEnabled(True)
        self.saveAsBtn.setObjectName(_fromUtf8("saveAsBtn"))
        self.gridLayout.addWidget(self.saveAsBtn, 4, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(88, 47, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        self.deleteBtn = QtGui.QPushButton(Form)
        self.deleteBtn.setEnabled(True)
        self.deleteBtn.setObjectName(_fromUtf8("deleteBtn"))
        self.gridLayout.addWidget(self.deleteBtn, 7, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.currentTitleLabel = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTitleLabel.sizePolicy().hasHeightForWidth())
        self.currentTitleLabel.setSizePolicy(sizePolicy)
        self.currentTitleLabel.setObjectName(_fromUtf8("currentTitleLabel"))
        self.horizontalLayout.addWidget(self.currentTitleLabel)
        self.currentLabel = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentLabel.sizePolicy().hasHeightForWidth())
        self.currentLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.currentLabel.setFont(font)
        self.currentLabel.setText(_fromUtf8(""))
        self.currentLabel.setObjectName(_fromUtf8("currentLabel"))
        self.horizontalLayout.addWidget(self.currentLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 3)
        self.newDirBtn = QtGui.QPushButton(Form)
        self.newDirBtn.setObjectName(_fromUtf8("newDirBtn"))
        self.gridLayout.addWidget(self.newDirBtn, 5, 2, 1, 1)
        self.fileTree = DirTreeWidget(Form)
        self.fileTree.setAcceptDrops(True)
        self.fileTree.setHeaderHidden(True)
        self.fileTree.setObjectName(_fromUtf8("fileTree"))
        self.fileTree.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout.addWidget(self.fileTree, 1, 1, 7, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("Form", "Protocols", None, QtGui.QApplication.UnicodeUTF8))
        self.newBtn.setText(QtGui.QApplication.translate("Form", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.loadBtn.setText(QtGui.QApplication.translate("Form", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.saveBtn.setText(QtGui.QApplication.translate("Form", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsBtn.setText(QtGui.QApplication.translate("Form", "Save As..", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBtn.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.currentTitleLabel.setText(QtGui.QApplication.translate("Form", "Current Protocol:", None, QtGui.QApplication.UnicodeUTF8))
        self.newDirBtn.setText(QtGui.QApplication.translate("Form", "New Dir", None, QtGui.QApplication.UnicodeUTF8))

from acq4.util.DirTreeWidget import DirTreeWidget
