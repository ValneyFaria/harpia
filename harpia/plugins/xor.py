#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.constants import *
import gettext
_ = gettext.gettext
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)

from harpia.GUI.fieldtypes import *
from harpia.model.plugin import Plugin

class Xor(Plugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        self.id = -1
        self.type = "43"

    # ----------------------------------------------------------------------
    def get_help(self):#Função que chama a help
        return "Realiza a operação lógica XOR entre duas imagens."

    # ----------------------------------------------------------------------
    def generate(self, blockTemplate):
        import harpia.gerador
        blockTemplate.header += harpia.gerador.adjust_images_size()

        blockTemplate.imagesIO = \
            'IplImage * block$$_img_i1 = NULL;\n' + \
            'IplImage * block$$_img_i2 = NULL;\n' + \
            'IplImage * block$$_img_o1 = NULL;\n'
        blockTemplate.functionCall = '\nif(block$$_img_i1){\n' + \
                                     'block$$_img_o1 = cvCreateImage(cvSize(block$$' + \
                                     '_img_i1->width,block$$_img_i1->height),block$$' + \
                                     '_img_i1->depth,block$$_img_i1->nChannels);\n' + \
                                     'adjust_images_size(block$$_img_i1, block$$_img_i2, block$$_img_o1);\n' + \
                                      'cvXor(block$$_img_i1, block$$_img_i2, block$$' + \
                                     '_img_o1,0);\ncvResetImageROI(block$$_img_o1);}\n'
        blockTemplate.dealloc = 'cvReleaseImage(&block$$_img_o1);\n' + \
                                'cvReleaseImage(&block$$_img_i1);\n' + \
                                'cvReleaseImage(&block$$_img_i2);\n'


    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
            "Label": _("Xor"),
            "Icon": "images/xor.png",
            "Color": "10:180:10:150",
            "InTypes": {0: "HRP_IMAGE", 1: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "Description": _("Logical XOR (exclusive-or) operation between two images."),
            "TreeGroup": _("Arithmetic and logical operations")
            }

    # ----------------------------------------------------------------------
    def get_properties(self):
        return {}

# ------------------------------------------------------------------------------
