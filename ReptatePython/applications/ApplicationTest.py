from PyQt5.QtGui import *
from ApplicationWindow import *
from View import *
from DataFiles import *

class ApplicationTest(ApplicationWindow):
    def __init__(self, parent = None):
        super(ApplicationTest, self).__init__()
        self.name='Test'
        self.views.append(View("TestView1", "t", "r", False, False, self.view1, 1, ["lolo"]))
        self.views.append(View("TestView2", "t", "r2", False, False, self.view2, 1, ["lolo2"]))
        self.populateViews()
        ftype=TXTColumnFile("G(t) files", "gt", "Relaxation modulus", 0, 2, ['t','Gt'], [0], ['Mw','ncontri'], [])
        self.files[ftype.extension]=ftype
        self.logger.debug(self.files)

    def view1(self, vec, x, y, file_parameters):
        x[0]=vec[0]
        y[0]=vec[1]
        return True

    def view2(self, vec, x, y, file_parameters):
        x[0]=vec[0]
        y[0]=vec[1]**2
        return True
            
