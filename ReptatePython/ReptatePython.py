import sys
import os
from PyQt4.QtCore import *
from PyQt4.uic import loadUiType
from PyQt4.QtGui import *
import logging
import logging.handlers

sys.path.append('GUI')
sys.path.append('GUI/uifiles')
sys.path.append('console')
sys.path.append('applications')


from AboutReptate import *
from Console import *
    
from ApplicationTest import *
from ApplicationReact import *
from ApplicationMWD import *
from ApplicationTTS import *
from ApplicationLVE import *
from ApplicationNLVE import *
from ApplicationGt import *
from ApplicationCreep import *
from ApplicationSANS import *
    
Ui_MainWindow, QMainWindow = loadUiType(os.path.join(os.path.dirname(__file__), 'GUI/uifiles/ReptateMainWindow.ui'))          
    
class MainWindow(QMainWindow, Ui_MainWindow):
    count = 0
    reptatelogger = logging.getLogger('ReptateLogger')
    reptatelogger.setLevel(logging.DEBUG)
    appdict = {}
    
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
        # Hide console and project navigation
        self.ConsoledockWidget.hide()
        self.ProjectdockWidget.hide()
        
        # Connect actions
        self.actionTest.triggered.connect(self.newTestWindow)
        self.actionReact.triggered.connect(self.newReactWindow)
        self.actionMWD.triggered.connect(self.newMWDWindow)
        self.actionTTS.triggered.connect(self.newTTSWindow)
        self.actionLVE.triggered.connect(self.newLVEWindow)
        self.actionNLVE.triggered.connect(self.newNLVEWindow)
        self.actionGt.triggered.connect(self.newGtWindow)
        self.actionCreep.triggered.connect(self.newCreepWindow)
        self.actionSANS.triggered.connect(self.newSANSWindow)
        self.actionProject.triggered.connect(self.switchProjectViewHide)
        self.actionConsole.triggered.connect(self.switchConsoleViewHide)
        self.ApplicationtabWidget.tabCloseRequested.connect(self.closeTab)        
        self.ApplicationtabWidget.currentChanged.connect(self.tabChanged)
        #self.Projecttree.itemSelectionChanged.connect(self.treeChanged)
        
        self.actionAbout_Qt.triggered.connect(QApplication.aboutQt)
        self.actionAbout.triggered.connect(self.showAbout)

        LOG_FILENAME = 'reptate.log'
        handler = logging.handlers.RotatingFileHandler(
            LOG_FILENAME, maxBytes=20000, backupCount=2)
        MainWindow.reptatelogger.addHandler(handler)
        
        # CONSOLE WINDOW
        self.textEdit = Console(self)
        #this is how you pass in locals to the interpreter
        self.textEdit.initInterpreter(locals()) 
        self.verticalLayout.addWidget(self.textEdit)
       

    def showAbout(self):
        dlg = AboutWindow(self)
        dlg.show()        
        
    def newTestWindow(self):
        MainWindow.reptatelogger.debug("NEW Test Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationTest()
        appname = sub.name + '%d'%MainWindow.count
        #sub.windowTitle=appname
        
        ind=self.ApplicationtabWidget.addTab(sub, QIcon('Images/Clip.ico'), appname)
        self.ApplicationtabWidget.setCurrentIndex(ind)        
        
        root = QTreeWidgetItem(self.Projecttree, [appname])
        root.setIcon(0, QIcon('Images/Clip.ico'))
        sub.treeEntry = root

    def newReactWindow(self):
        MainWindow.reptatelogger.debug("NEW React Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationReact()

        ind=self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/react.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/react.ico'))

    def newMWDWindow(self):
        MainWindow.reptatelogger.debug("NEW MWD Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationMWD()

        ind=self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/Mw.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/Mw.ico'))

    def newTTSWindow(self):
        MainWindow.reptatelogger.debug("NEW TTS Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationTTS()

        ind=self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/TTS.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/TTS.ico'))

    def newLVEWindow(self):
        MainWindow.reptatelogger.debug("NEW LVE Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationLVE()

        ind=self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/LVE.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/LVE.ico'))
        
    def newNLVEWindow(self):
        MainWindow.reptatelogger.debug("NEW NLVE Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationNLVE()

        ind=self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/NLVE.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/NLVE.ico'))

    def newGtWindow(self):
        MainWindow.reptatelogger.debug("NEW Gt Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationGt()

        ind=self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/Gt.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/Gt.ico'))

    def newCreepWindow(self):
        MainWindow.reptatelogger.debug("NEW Creep Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationCreep()

        ind=self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/Creep.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/Creep.ico'))

    def newSANSWindow(self):
        MainWindow.reptatelogger.debug("NEW SANS Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationSANS()

        ind=self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/SANS.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/SANS.ico'))

    def switchProjectViewHide(self):
        if (self.ProjectdockWidget.isHidden()):
            self.ProjectdockWidget.show()
        else:
            self.ProjectdockWidget.hide()

    def switchConsoleViewHide(self):
        if (self.ConsoledockWidget.isHidden()):
            self.ConsoledockWidget.show()
            self.textEdit.setFocus()
        else:
            self.ConsoledockWidget.hide()

    def tabChanged(self, index):
        #appname = self.ApplicationtabWidget.widget(index).windowTitle
        #items = self.Projecttree.findItems(appname, Qt.MatchContains)
        #self.Projecttree.setCurrentItem(items[0])
        pass
            
    def treeChanged(self):
        #print("HELLO")
        #appname = self.Projecttree.currentItem.text(0)
        #print(index, appname)
        pass
    
    def closeTab(self, index):
        #appname = self.ApplicationtabWidget.widget(index).windowTitle
        #print(appname)
        #print(self.appdict[appname])
        #self.Projecttree.removeItemWidget(self.appdict[appname],0)
        
        self.ApplicationtabWidget.removeTab(index)
        
        
def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.showMaximized()

    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()