# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main_dialog(object):
    def setupUi(self, main_dialog):
        main_dialog.setObjectName(_fromUtf8("main_dialog"))
        main_dialog.resize(518, 505)
        self.verticalLayout_2 = QtGui.QVBoxLayout(main_dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(main_dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_img = QtGui.QLabel(self.frame)
        self.lbl_img.setMinimumSize(QtCore.QSize(120, 180))
        self.lbl_img.setFrameShape(QtGui.QFrame.Box)
        self.lbl_img.setMidLineWidth(0)
        self.lbl_img.setText(_fromUtf8(""))
        self.lbl_img.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Pictures/engrane7.png")))
        self.lbl_img.setScaledContents(False)
        self.lbl_img.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img.setWordWrap(False)
        self.lbl_img.setObjectName(_fromUtf8("lbl_img"))
        self.verticalLayout.addWidget(self.lbl_img)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.textBrowser = QtGui.QTextBrowser(self.frame_2)
        self.textBrowser.setMaximumSize(QtCore.QSize(1500, 120))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout.addWidget(self.textBrowser)
        spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_picker_1 = QtGui.QPushButton(self.frame_4)
        self.btn_picker_1.setObjectName(_fromUtf8("btn_picker_1"))
        self.horizontalLayout_2.addWidget(self.btn_picker_1)
        self.btn_picker_0 = QtGui.QPushButton(self.frame_4)
        self.btn_picker_0.setText(_fromUtf8(""))
        self.btn_picker_0.setObjectName(_fromUtf8("btn_picker_0"))
        self.horizontalLayout_2.addWidget(self.btn_picker_0)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(75, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_render = QtGui.QPushButton(self.frame_5)
        self.btn_render.setObjectName(_fromUtf8("btn_render"))
        self.horizontalLayout_3.addWidget(self.btn_render)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(main_dialog)
        QtCore.QMetaObject.connectSlotsByName(main_dialog)

    def retranslateUi(self, main_dialog):
        main_dialog.setWindowTitle(_translate("main_dialog", "Cinesite_RendererTest_FidelM", None))
        self.textBrowser.setHtml(_translate("main_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Hello Cinesite!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pick a color and Render</span></p></body></html>", None))
        self.btn_picker_1.setText(_translate("main_dialog", "Color Picker", None))
        self.btn_render.setText(_translate("main_dialog", "Render", None))

