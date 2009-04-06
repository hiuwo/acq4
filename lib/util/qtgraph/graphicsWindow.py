# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphicsWindow.ui'
#
# Created: Thu May  8 14:43:32 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from GraphicsView import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,659,514).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = GraphicsView(self.centralwidget)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(244,244,244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)
        self.graphicsView.setPalette(palette)
        self.graphicsView.setProperty("cursor",QtCore.QVariant(QtCore.Qt.ArrowCursor))
        self.graphicsView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.graphicsView.setFrameShape(QtGui.QFrame.NoFrame)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setTransformationAnchor(QtGui.QGraphicsView.NoAnchor)
        self.graphicsView.setResizeAnchor(QtGui.QGraphicsView.AnchorViewCenter)
        self.graphicsView.setViewportUpdateMode(QtGui.QGraphicsView.SmartViewportUpdate)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timeControlDock = QtGui.QDockWidget(MainWindow)
        self.timeControlDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.NoDockWidgetFeatures)
        self.timeControlDock.setObjectName("timeControlDock")

        self.dockWidgetContents_2 = QtGui.QWidget(self.timeControlDock)
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")

        self.hboxlayout = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.hboxlayout.setSpacing(0)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")

        self.spinBox = QtGui.QSpinBox(self.dockWidgetContents_2)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000)
        self.spinBox.setProperty("value",QtCore.QVariant(10))
        self.spinBox.setObjectName("spinBox")
        self.hboxlayout.addWidget(self.spinBox)

        self.timeSlider = QtGui.QSlider(self.dockWidgetContents_2)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.hboxlayout.addWidget(self.timeSlider)
        self.timeControlDock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.timeControlDock)

        self.ImageLUTDock = QtGui.QDockWidget(MainWindow)
        self.ImageLUTDock.setWindowModality(QtCore.Qt.NonModal)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLUTDock.sizePolicy().hasHeightForWidth())
        self.ImageLUTDock.setSizePolicy(sizePolicy)
        self.ImageLUTDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.NoDockWidgetFeatures)
        self.ImageLUTDock.setObjectName("ImageLUTDock")

        self.dockWidgetContents = QtGui.QWidget(self.ImageLUTDock)
        self.dockWidgetContents.setObjectName("dockWidgetContents")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.hboxlayout1.setSpacing(0)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.blackLevel = QtGui.QSlider(self.dockWidgetContents)
        self.blackLevel.setMaximum(2000)
        self.blackLevel.setOrientation(QtCore.Qt.Vertical)
        self.blackLevel.setObjectName("blackLevel")
        self.hboxlayout1.addWidget(self.blackLevel)

        self.whiteLevel = QtGui.QSlider(self.dockWidgetContents)
        self.whiteLevel.setMaximum(2000)
        self.whiteLevel.setOrientation(QtCore.Qt.Vertical)
        self.whiteLevel.setObjectName("whiteLevel")
        self.hboxlayout1.addWidget(self.whiteLevel)
        self.ImageLUTDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.ImageLUTDock)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox.setSuffix(QtGui.QApplication.translate("MainWindow", " fps", None, QtGui.QApplication.UnicodeUTF8))
        self.ImageLUTDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Image Options", None, QtGui.QApplication.UnicodeUTF8))

