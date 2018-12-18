# -*- coding: utf-8 -*- 

"""
Methods that has nos direct relation
with the ui
"""
import os
from PyQt4 import QtGui, QtCore

from arnold import *
class CoreFunctions(QtCore.QThread):
    renderSignal = QtCore.pyqtSignal()
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.r = self.g = self.b = 100
        self.log=None 
        self.image_path = None

    def createSphere(self):
        # create a sphere geometric primitive
        self.sphere = AiNode("sphere")
        AiNodeSetStr(self.sphere, "name", "geo_sphere")
        AiNodeSetVec(self.sphere, "center", 0.0, 0.0, 0.0)
        AiNodeSetFlt(self.sphere, "radius", 6.0)

        # create a red standard shader
        self.shader = AiNode("standard")
        AiNodeSetStr(self.shader, "name", "ai_shader")
        AiNodeSetRGB(self.shader, 
            "Kd_color", self.r, 
            self.g, self.b)
        AiNodeSetFlt(self.shader, "Ks", 0.01)

        # assign the shaders to the geometric objects
        AiNodeSetPtr(self.sphere, "shader", self.shader)

    def createCamera(self):
        """
            Create camera
        """
        self.camera = AiNode("persp_camera")
        AiNodeSetStr(self.camera, "name", "cam")
        # Camera position
        AiNodeSetVec(self.camera, "position", 0.0, 0.0, 40.0)
        AiNodeSetVec(self.camera, "look_at", 0.0, 0.0, 0.0)
        AiNodeSetFlt(self.camera, "fov", 45.0)

    def createLights(self):
        """
        Create light
        """
        
        self.light = AiNode("point_light")
        AiNodeSetStr(self.light, "name", "light_01")

        #Light position
        AiNodeSetVec(self.light, "position", 0.0, 15.0, 45.0)
        AiNodeSetFlt(self.light, "exposure", 2.0)
        AiNodeSetFlt(self.light, "intensity", 8.0)

    def render_settings(self):
        """
        Set render settings
        """
        ops = AiUniverseGetOptions()
        AiNodeSetInt(ops, "AA_samples", 8)
        AiNodeSetInt(ops, "xres", 512)
        AiNodeSetInt(ops, "yres", 384)
        AiNodeSetInt(ops, "GI_diffuse_depth", 4)

        # create an output driver node
        driver = AiNode("driver_jpeg")
        AiNodeSetStr(driver, "name", "_driver")
        AiNodeSetStr(driver, "filename", self.image_path)
        AiNodeSetFlt(driver, "gamma", 2.2)

        # create a gaussian filter node
        filter = AiNode("gaussian_filter")
        AiNodeSetStr(filter, "name", "_filter")

        # assign the driver and filter to the main (beauty) AOV,
        # which is called "RGBA" and is of type RGBA
        outs_ = AiArrayAllocate(1, 1, AI_TYPE_STRING)
        AiArraySetStr(outs_, 0, "RGBA RGBA _filter _driver")
        AiNodeSetArray(ops, "outputs", outs_)

    def run(self):
        # Begin arnold process
        AiBegin()

        #Connecting log 
        AiMsgSetLogFileName(self.log)
        AiMsgSetConsoleFlags(AI_LOG_ALL)

        self.createSphere()
        self.createCamera()
        self.createLights()
        self.render_settings()

        AiRender(AI_RENDER_MODE_CAMERA)

        # End arnold process
        AiEnd()
        self.renderSignal.emit()

    def setColor(self, r, g, b):
        self.r = r * 255
        self.g = g * 255
        self.b = b * 255

