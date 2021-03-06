from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import itertools
import Symbols_rc
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QTreeWidget, QTabWidget, QHeaderView, QToolBar, QComboBox
from DataSetItem import *

Ui_DataSet, QWidget = loadUiType('GUI/uifiles/DataSet.ui')

class DataSet(QWidget, Ui_DataSet):
    def __init__(self, ):
        super(DataSet, self).__init__()
        self.setupUi(self)

        self.DataSettreeWidget.setIndentation(0)
        self.DataSettreeWidget.setHeaderItem(QTreeWidgetItem([""]))   
        hd=self.DataSettreeWidget.header()
        hd.setSectionsMovable(False)
        w=self.DataSettreeWidget.width()
        w/=hd.count()
        for i in range(hd.count()):
            hd.resizeSection(0, w)
        
        # Theory Toolbar
        tb = QToolBar()
        tb.setIconSize(QSize(24,24))
        self.numtheories=0
        self.cbtheory = QComboBox()
        self.cbtheory.setToolTip("Hello")
        self.cbtheory.addItem("ThA")
        self.cbtheory.addItem("ThB")
        self.cbtheory.addItem("ThC")
        tb.addWidget(self.cbtheory)
        tb.addAction(self.actionNew_Theory)
        tb.addAction(self.actionCalculate_Theory)
        tb.addAction(self.actionMinimize_Error)
        tb.addAction(self.actionTheory_Options)
        self.TheoryLayout.insertWidget(0, tb)

        connection_id = self.actionNew_Theory.triggered.connect(self.NewTheory)
        connection_id = self.DataSettreeWidget.itemChanged.connect(self.handle_item_changed)

    def handle_item_changed(self, item, column):
        if (item.series):
            item.series.set_visible(item.checkState(0)==Qt.Checked)
            item.series.figure.canvas.draw()

    def resizeEvent(self, evt=None):
        hd=self.DataSettreeWidget.header()
        w=self.DataSettreeWidget.width()
        w/=hd.count()
        for i in range(hd.count()):
            hd.resizeSection(i, w)        
            #hd.setTextAlignment(i, Qt.AlignHCenter)

    def NewTheory(self):
        self.numtheories+=1
        thname = self.cbtheory.currentText()
        obj=QTreeWidget()
        obj.setIndentation(0)
        obj.setHeaderItem(QTreeWidgetItem(["Parameter","Value"]))
        obj.setAlternatingRowColors(True)
        obj.setFrameShape(QFrame.NoFrame)
        obj.setFrameShadow(QFrame.Plain)
        #obj.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        obj.setEditTriggers(obj.NoEditTriggers) 
        connection_id = obj.itemDoubleClicked.connect(self.onTreeWidgetItemDoubleClicked)
        self.actionNew_Theory.triggered.connect(self.NewTheory)
        #obj.setStyleSheet(QStyle("QTreeWidget::item { border: 0.5px ; border-style: solid ; border-color: lightgray ;}"))
        ##obj.styleSheet="QTreeWidget::item { border: 0.5px ; border-style: solid ; border-color: lightgray ;}\n"
        self.TheorytabWidget.addTab(obj, thname+'%d'%self.numtheories)
        self.TheorytabWidget.setCurrentIndex(self.numtheories-1)
        item = QTreeWidgetItem(obj, ['Param1', "%g"%4.345])
        item.setCheckState(0,2)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        item = QTreeWidgetItem(obj, ['Param2', "%g"%2.365])
        item.setCheckState(0,2)
        item.setFlags(item.flags() | Qt.ItemIsEditable)

    def onTreeWidgetItemDoubleClicked(self, item, column):
        if (column==1):
            thcurrent = self.TheorytabWidget.currentWidget()
            thcurrent.editItem(item, column)
            