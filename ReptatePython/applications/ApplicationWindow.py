from PyQt4.QtGui import *
from PyQt4.uic import loadUiType
import seaborn as sns   
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_pdf import PdfPages
import itertools
import numpy as np
import Symbols_rc
from PyQt4 import QtCore
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

from DataSet import *
    
Ui_AppWindow, QMainWindow = loadUiType('GUI/uifiles/ApplicationWindow.ui')

class ApplicationWindow(QMainWindow, Ui_AppWindow):
    name='Application Template'
    fig=0
    ax=0
    canvas=0
    def __init__(self, ):
        super(ApplicationWindow, self).__init__()
        self.setupUi(self)

        ################
        # SETUP TOOLBARS
        # Data Inspector Toolbar
        tb = QToolBar()
        tb.setIconSize(QtCore.QSize(24,24))
        tb.addAction(self.actionCopy)
        tb.addAction(self.actionPaste)
        tb.addAction(self.actionShiftVertically)
        tb.addAction(self.actionShiftHorizontally)
        self.LayoutDataInspector.insertWidget(0, tb)
        
        # Dataset Toolbar
        tb = QToolBar()
        tb.setIconSize(QtCore.QSize(24,24))
        tb.addAction(self.actionNew_Empty_Dataset)
        tb.addAction(self.actionView_All_Sets)
        #tb.addAction(self.actionData_Representation)
        tbut = QToolButton()
        tbut.setPopupMode(QToolButton.MenuButtonPopup)
        tbut.setDefaultAction(self.actionData_Representation)
        menu=QMenu()
        menu.addAction(self.actionShow_Small_Symbols)
        menu.addAction(self.actionShow_Large_Symbols)
        tbut.setMenu(menu)
        tb.addWidget(tbut)
        #
        tb.addAction(self.actionReload_Data)
        #tb.addAction(self.actionShow_Limits)
        tbut = QToolButton()
        tbut.setPopupMode(QToolButton.MenuButtonPopup)
        tbut.setDefaultAction(self.actionShow_Limits)
        menu=QMenu()
        menu.addAction(self.actionNo_Limits)
        menu.addAction(self.actionVertical_Limits)
        menu.addAction(self.actionHorizontal_Limits)
        menu.addAction(self.actionBoth_Limits)
        tbut.setMenu(menu)
        tb.addWidget(tbut)
        #
        tb.addAction(self.actionInspect_Data)
        tb.addAction(self.actionPrint)
        self.ViewDataTheoryLayout.insertWidget(1, tb)
        self.ViewDataTheorydockWidget.Width=500
                
        # Tests TableWidget
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(['x','y','z','a','b','c','d','e','f','g'])
                
        # Hide Data Inspector
        self.DataInspectordockWidget.hide()

        # PLOT Style
        sns.set_style("white")
        sns.set_style("ticks")
        #plt.style.use('seaborn-talk')
        #plt.style.use('seaborn-paper')
        plt.style.use('seaborn-poster')
        self.fig=plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        sns.despine() # Remove up and right side of plot box
                
        # EVENT HANDLING
        #connection_id = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        connection_id = self.fig.canvas.mpl_connect('resize_event', self.resizeplot)
        #connection_id = self.fig.canvas.mpl_connect('motion_notify_event', self.on_plot_hover)   
        connection_id = self.actionPrint.triggered.connect(self.printPlot)
        connection_id = self.actionInspect_Data.triggered.connect(self.showDataInspector)
        connection_id = self.actionNew_Empty_Dataset.triggered.connect(self.createNew_Empty_Dataset)
        connection_id = self.actionShow_Small_Symbols.triggered.connect(self.Small_Symbols)
        connection_id = self.actionShow_Large_Symbols.triggered.connect(self.Large_Symbols)

        connection_id = self.actionNo_Limits.triggered.connect(self.No_Limits)
        connection_id = self.actionVertical_Limits.triggered.connect(self.Vertical_Limits)
        connection_id = self.actionHorizontal_Limits.triggered.connect(self.Horizontal_Limits)
        connection_id = self.actionBoth_Limits.triggered.connect(self.Both_Limits)
            
        # TEST GET CLICKABLE OBJECTS ON THE X AXIS
        #xaxis = self.ax.get_xticklabels()
        #print (xaxis)

    def No_Limits(self):
        self.actionShow_Limits.setIcon(self.actionNo_Limits.icon())

    def Vertical_Limits(self):
        self.actionShow_Limits.setIcon(self.actionVertical_Limits.icon())

    def Horizontal_Limits(self):
        self.actionShow_Limits.setIcon(self.actionHorizontal_Limits.icon())

    def Both_Limits(self):
        self.actionShow_Limits.setIcon(self.actionBoth_Limits.icon())
        
    def Small_Symbols(self):
        self.actionData_Representation.setIcon(self.actionShow_Small_Symbols.icon())
    
    def Large_Symbols(self):
        self.actionData_Representation.setIcon(self.actionShow_Large_Symbols.icon())
    
        
    def createNew_Empty_Dataset(self):
        # Plot some random walks
        num_lines=10
        num_points=200
        #palette = itertools.cycle(sns.color_palette("Set1",n_colors=num_lines, desat=.5)) 
        #palette = itertools.cycle(sns.color_palette("Blues_d",n_colors=num_lines)) 
        pname="default" # nipy_spectral gist_ncar gist_rainbow Dark2 cool, afmhot, hsl, husl, deep, muted, bright, pastel, dark, colorblind, viridis
        #palette = itertools.cycle(sns.color_palette(pname,num_lines)) 
        palette=itertools.cycle(((0,0,0),(1.0,0,0),(0,1.0,0),(0,0,1.0),(1.0,1.0,0),(1.0,0,1.0),(0,1.0,1.0),(0.5,0,0),(0,0.5,0),(0,0,0.5),(0.5,0.5,0),(0.5,0,0.5),(0,0.5,0.5),(0.25,0,0),(0,0.25,0),(0,0,0.25),(0.25,0.25,0),(0.25,0,0.25),(0,0.25,0.25)))
        markerlst = itertools.cycle(('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd')) 
        linelst = itertools.cycle((':', '-', '-.', '--'))

        # Add New tab to DataSettabWidget
        ind=self.DataSettabWidget.count()+1
        ds = DataSet()
        self.DataSettabWidget.addTab(ds, 'DataSet'+'%d'%ind)
        self.DataSettabWidget.setCurrentIndex(ind-1)
        
        hd=ds.DataSettreeWidget.header()
        w=ds.DataSettreeWidget.width()
        w/=hd.count()
        for i in range(hd.count()):
            hd.resizeSection(0, w)

        for i in range(num_lines):
            x=np.arange(num_points)
            y=np.cumsum(np.random.randn(num_points))
            # DIFFERENT STYLES
            # JUST LINES
            #self.ax.plot(y, color=next(palette), label='Line %d'%i)
            # LINES with DIFFERENT STYLES, BLACK
            #self.ax.plot(y, linestyle=next(linelst), color='black', label='Line %d'%i)
            # LINES with DIFFERENT STYLES, DIFFERENT COLORS
            #self.ax.plot(y, linestyle=next(linelst), color=next(palette), label='Line %d'%i)
            # LINES WITH FILLED SYMBOLS
            #self.ax.plot(y, color=next(palette), marker=next(markerlst), label='Line %d'%i)
            # LINES WITH FILLED SYMBOLS WITH BLACK BORDERS
            #c=next(palette)
            #self.ax.plot(y, color=c, marker=next(markerlst), ms=12, markerfacecolor=c, markeredgewidth=1, markeredgecolor='black', label='Line %d'%i)
            # EMPTY SYMBOLS 
            self.ax.scatter(x, y, marker=next(markerlst), s=120, facecolors='none', edgecolors=next(palette), linewidths=1, label='Line %d'%i)
            # EMPTY BLACK AND WHITE SYMBOLS 
            #self.ax.scatter(x, y, marker=next(markerlst), s=120, facecolors='none', edgecolors='black', label='Line %d'%i)
            # FILLED SYMBOLS with Black borders
            #self.ax.scatter(x, y, marker=next(markerlst), s=120, facecolors=next(palette), edgecolors='black', label='Line %d'%i)

            root = QTreeWidgetItem(ds.DataSettreeWidget, ['Line %d'%i, "hello", "it's me"])
            root.setCheckState(0, 2)
            root.setIcon(0, QIcon('Images/symbols/'+pname+str(i+1)+'.ico'))
                        
        # LEGEND STUFF
        leg=plt.legend(loc='upper left', frameon=True, ncol=2)
        if leg:
            leg.draggable()
            
        # LIMITS AND AXIS LABELS
        # TODO: Need to define a Units module to handle this!!!
        self.ax.set_xlim(0, num_points)
        self.ax.set_xlabel("t (s)")
        self.ax.set_ylabel("r (m)")
    
        plt.tight_layout(pad=1.2)
        self.canvas.draw()

    def showDataInspector(self):
        if self.DataInspectordockWidget.isHidden():
            self.DataInspectordockWidget.show()
        else:
            self.DataInspectordockWidget.hide()
        
    def printPlot(self):
        #pp = PdfPages('multipage.pdf')
        #pp.savefig()
        #pp.close()
        #fig.set_size_inches(6.5, 5.5, forward=True)
        plt.savefig("locus.pdf")
        #plt.savefig("locus.png")    
        
    def on_plot_hover(self, event):
        pass
        
    def onclick(self, event):
        if event.dblclick:
            pickedtick = event.artist
            print(event)
            print(pickedtick)

    def resizeplot(self, event):
        # TIGHT LAYOUT in order to view axes and everything
        plt.tight_layout(pad=1.2)
