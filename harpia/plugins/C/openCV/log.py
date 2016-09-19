#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.constants import *
import gettext
_ = gettext.gettext
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin

class Log(OpenCVPlugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.id = -1
        self.type = self.__class__.__module__

    # ----------------------------------------------------------------------
    def get_help(self):#Função que chama a help
        return "aplica a função logarítmica a uma imagem, ou seja,\
        calcula o logarítmo natural do valor de intensidade luminosa de cada ponto da imagem."

    # ----------------------------------------------------------------------
    def generate_vars(self):
        return \
            'IplImage * block$id$_img_i1 = NULL;\n' + \
            'IplImage * block$id$_img_o1 = NULL;\n' + \
            'IplImage * block$id$_img_t = NULL;\n'

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        return \
            '\nif(block$id$_img_i1){\n' + \
            'block$id$_img_t = cvCreateImage(cvGetSize(block$id$_img_i1), IPL_DEPTH_32F,block$id$_img_i1->nChannels);\n' + \
            'block$id$_img_o1 = cvCloneImage(block$id$_img_i1);\n' + \
            'cvConvertScale(block$id$_img_i1,block$id$_img_t,(1/93.8092),0);\n' + \
            'cvLog(block$id$_img_t, block$id$_img_t);\n' + \
            'cvConvertScale(block$id$_img_t,block$id$_img_o1,255.0,0);}\n'

    # ----------------------------------------------------------------------
    def generate_dealloc(self):
        return 'cvReleaseImage(&block$id$_img_o1);\n' + \
               'cvReleaseImage(&block$id$_img_i1);\n' + \
               'cvReleaseImage(&block$id$_img_t);\n'


    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
            "Label": _("Log"),
            "Icon": "images/log.png",
            "Color": "230:230:60:150",
            "InTypes": {0: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "Description": _("Return the image made from the neperian logarithm of each one of the image pixels."),
            "TreeGroup": _("Math Functions")
            }

    # ----------------------------------------------------------------------
    def get_properties(self):
        return {}

# ------------------------------------------------------------------------------
