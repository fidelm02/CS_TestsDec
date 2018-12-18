
import sys
import os
from PyQt4 import QtGui, QtCore


class UiActions():
    """
    Control of UI elements.
    """

    def __init__(self, win_dialog, core_func):
    	"""
    	"""
    	self.dialog = win_dialog
    	self.core = core_func

    	self.log = win_dialog.textBrowser
    	self.folder = self.createFolder()
    	self.log_path = os.path.join(self.folder,"fTest_log.txt")
    	self.img_name = os.path.join(self.folder,"fTest_render.jpg")
    	self.core.log = self.log_path
    	self.core.image_path = self.img_name

    	# Connetion core functions to UI elements
    	self.connectButtons()

    def createFolder(self):
    	home = os.path.expanduser("~")
    	final_path = os.path.join(home,".renderTest_fidelm")

    	if not os.access(final_path, os.F_OK):
            os.makedirs(final_path, 0777)
    	return final_path

    def connectButtons(self):
    	"""
    	"""
    	self.dialog.btn_picker_1.clicked.connect(self.color_picker)
    	self.dialog.btn_picker_0.clicked.connect(self.color_picker)
    	self.dialog.btn_render.clicked.connect(self.render_action)

    	self.core.renderSignal.connect(self.endRender)

    def render_action(self):
    	"""
    	"""
    	self.log.setPlainText("...Rendering...")

        self.dialog.btn_picker_1.setEnabled(False)
        self.dialog.btn_picker_0.setEnabled(False)
        self.dialog.btn_render.setEnabled(False)

        self.core.start()

    def endRender(self):
    	img_path = os.path.join(self.folder, self.img_name)
        img = QtGui.QPixmap(img_path)
        img = img.scaledToWidth(512)
        self.dialog.lbl_img.setPixmap(img)

    	self.dialog.btn_picker_1.setEnabled(True)
        self.dialog.btn_picker_0.setEnabled(True)
        self.dialog.btn_render.setEnabled(True)

        log_file = open(self.log_path, 'r')
        with log_file:
            text = log_file.read()
            self.log.setPlainText(text)

    def color_picker(self):
    	"""
    	Show color picker and change 
    	the button that display the color selected
    	"""
    	#self.log.setPlainText("{0}\nChanging color", self.log.text())
    	self.log.append("\tChanging color")
    	#self.dialog.btn_picker_0
    	color = QtGui.QColorDialog.getColor()

        red = color.redF()
        green = color.greenF()
        blue = color.blueF()

        self.core.setColor(red, green, blue)

        self.dialog.btn_picker_0.setStyleSheet(
        	"background-color:%s;" % color.name())



