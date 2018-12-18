import os
import sys
import ctypes
from os import listdir, path
from os.path import isfile
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# Before using arnold!
# I have to load dll manually
#    Problem using dlls
s_path = "C:/solidangle/arnold/Arnold-5.2.2.0-windows/bin"
if os.access(s_path, os.F_OK):
    dlls = [dll for dll in listdir(s_path) if isfile(path.join(s_path, dll)) and 
    	('.dll' in dll)]
    for dll in dlls:
    	print "{0}/{1}".format(s_path, dll)
    	ctypes.WinDLL ("{0}/{1}".format(s_path, dll))
# End of loading dlls

from UI import main_dialog, bridge_function
from Core import app_PyQtArnold_core

modules = [main_dialog, bridge_function, app_PyQtArnold_core]
[reload (xi) for xi in modules]


class MyApplication(QDialog, main_dialog.Ui_main_dialog):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)

def main():
    if QCoreApplication.instance() is not None:
        app = QCoreApplication.instance()
    else:
        app = QApplication(sys.argv)

    app.aboutToQuit.connect(app.quit)
    window = MyApplication()

    core = app_PyQtArnold_core.CoreFunctions()
    bridge = bridge_function.UiActions(
        win_dialog=window, core_func = core)

    window.show()
    try:
        sys.exit(app.exec_())
    except:
        pass

main()