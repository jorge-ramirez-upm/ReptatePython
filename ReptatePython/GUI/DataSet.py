from PyQt4.QtGui import *
from PyQt4.uic import loadUiType
import itertools
import Symbols_rc
from PyQt4.QtCore import *

Ui_DataSet, QWidget = loadUiType('GUI/uifiles/DataSet.ui')

class DataSet(QWidget, Ui_DataSet):
    cbtheory=0
    numtheories=0
    def __init__(self, ):
        super(DataSet, self).__init__()
        self.setupUi(self)

        self.DataSettreeWidget.setIndentation(0)
        self.DataSettreeWidget.setHeaderItem(QTreeWidgetItem(["Tree","First","secondo"]))   
        hd=self.DataSettreeWidget.header()
        w=self.DataSettreeWidget.width()
        w/=hd.count()
        for i in range(hd.count()):
            hd.resizeSection(0, w)
        
        # Theory Toolbar
        tb = QToolBar()
        tb.setIconSize(QSize(24,24))
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

    def NewTheory(self):
        self.numtheories+=1
        thname = self.cbtheory.currentText()
        obj=QTreeWidget()
        self.TheorytabWidget.addTab(obj, thname+'%d'%self.numtheories)
        self.TheorytabWidget.setCurrentIndex(self.numtheories-1)
