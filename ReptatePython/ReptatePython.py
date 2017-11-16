"""Main RepTate source code"""
import sys
import os
import logging
import logging.handlers
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

sys.path.append('GUI')
sys.path.append('GUI/uifiles')
sys.path.append('console')
sys.path.append('applications')
sys.path.append('theories')
sys.path.append('core')

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

Ui_MainWindow, QMainWindow = loadUiType(os.path.join(os.path.dirname(__file__),
                                        'GUI/uifiles/ReptateMainWindow.ui'))          

class MainWindow(QMainWindow, Ui_MainWindow):
    """ Main Reptate window and application manager"""    
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
        self.actionTest.triggered.connect(self.new_test_window)
        self.actionReact.triggered.connect(self.new_react_window)
        self.actionMWD.triggered.connect(self.new_mwd_window)
        self.actionTTS.triggered.connect(self.new_tts_window)
        self.actionLVE.triggered.connect(self.new_lve_window)
        self.actionNLVE.triggered.connect(self.new_nlve_window)
        self.actionGt.triggered.connect(self.new_gt_window)
        self.actionCreep.triggered.connect(self.new_creep_window)
        self.actionSANS.triggered.connect(self.new_sans_window)
        self.actionProject.triggered.connect(self.switch_project_view_hide)
        self.actionConsole.triggered.connect(self.switch_console_vie_hide)
        self.ApplicationtabWidget.tabCloseRequested.connect(self.close_tab)        
        self.ApplicationtabWidget.currentChanged.connect(self.tab_changed)
        #self.Projecttree.itemSelectionChanged.connect(self.treeChanged)
        
        self.actionAbout_Qt.triggered.connect(QApplication.aboutQt)
        self.actionAbout.triggered.connect(self.show_about)

        log_file_name = 'reptate.log'
        handler = logging.handlers.RotatingFileHandler(
            log_file_name, maxBytes=20000, backupCount=2)
        MainWindow.reptatelogger.addHandler(handler)
        
        # CONSOLE WINDOW
        self.text_edit = Console(self)
        #this is how you pass in locals to the interpreter
        self.text_edit.initInterpreter(locals()) 
        self.verticalLayout.addWidget(self.text_edit)
       
    def show_about(self):
        """ Show about window"""
        dlg = AboutWindow(self)
        dlg.show()        
        
    def new_test_window(self):
        """ Open a new Test application window"""
        MainWindow.reptatelogger.debug("NEW Test Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationTest()
        appname = sub.name + '%d'%MainWindow.count
        #sub.windowTitle=appname
        
        ind = self.ApplicationtabWidget.addTab(sub, QIcon(':Icons/Images/Clip.ico'), appname)
        self.ApplicationtabWidget.setCurrentIndex(ind)        
        
        root = QTreeWidgetItem(self.Projecttree, [appname])
        root.setIcon(0, QIcon(':Icons/Images/Clip.ico'))
        sub.treeEntry = root

    def new_react_window(self):
        """ Open a new React application window"""
        MainWindow.reptatelogger.debug("NEW React Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationReact()

        ind = self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/react.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/react.ico'))

    def new_mwd_window(self):
        """ Open a new MWD application window"""
        MainWindow.reptatelogger.debug("NEW MWD Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationMWD()

        ind = self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/Mw.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/Mw.ico'))

    def new_tts_window(self):
        """ Open a new TTS application window"""
        MainWindow.reptatelogger.debug("NEW TTS Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationTTS()

        ind = self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/TTS.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/TTS.ico'))

    def new_lve_window(self):
        """ Open a new LVE application window"""
        MainWindow.reptatelogger.debug("NEW LVE Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationLVE()

        ind = self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/LVE.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/LVE.ico'))
        
    def new_nlve_window(self):
        """ Open a new NLVE application window"""
        MainWindow.reptatelogger.debug("NEW NLVE Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationNLVE()

        ind = self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/NLVE.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/NLVE.ico'))

    def new_gt_window(self):
        """ Open a new G(t) application window"""
        MainWindow.reptatelogger.debug("NEW Gt Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationGt()

        ind = self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/Gt.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/Gt.ico'))

    def new_creep_window(self):
        """ Open a new Creep application window"""
        MainWindow.reptatelogger.debug("NEW Creep Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationCreep()

        ind = self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/Creep.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/Creep.ico'))

    def new_sans_window(self):
        """ Open a new SANS application window"""
        MainWindow.reptatelogger.debug("NEW SANS Window")
        MainWindow.count = MainWindow.count+1
        sub = ApplicationSANS()

        ind = self.ApplicationtabWidget.addTab(sub, QIcon(':/Icons/Images/SANS.ico'), sub.name)
        self.ApplicationtabWidget.setCurrentIndex(ind)

        root = QTreeWidgetItem(self.Projecttree, [sub.name])
        root.setIcon(0, QIcon(':/Icons/Images/SANS.ico'))

    def switch_project_view_hide(self):
        """View or hide the project navigation window """
        if (self.ProjectdockWidget.isHidden()):
            self.ProjectdockWidget.show()
        else:
            self.ProjectdockWidget.hide()

    def switch_console_vie_hide(self):
       """Show or hide the console window"""
       if (self.ConsoledockWidget.isHidden()):
            self.ConsoledockWidget.show()
            self.text_edit.setFocus()
       else:
            self.ConsoledockWidget.hide()

    def tab_changed(self, index):
        """Capture when the active application has changed"""
        #appname = self.ApplicationtabWidget.widget(index).windowTitle
        #items = self.Projecttree.findItems(appname, Qt.MatchContains)
        #self.Projecttree.setCurrentItem(items[0])
        pass
            
    def tree_changed(self):
        """Capture when the active application has changed in the application navigator"""
        #print("HELLO")
        #appname = self.Projecttree.currentItem.text(0)
        #print(index, appname)
        pass
    
    def close_tab(self, index):
        #appname = self.ApplicationtabWidget.widget(index).windowTitle
        #print(appname)
        #print(self.appdict[appname])
        #self.Projecttree.removeItemWidget(self.appdict[appname],0)
        
        self.ApplicationtabWidget.removeTab(index)
        
def main():
    """ main """        
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.showMaximized()

    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()
