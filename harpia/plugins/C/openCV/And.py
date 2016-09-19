#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin

class And(OpenCVPlugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.id = -1
        self.type = self.__class__.__module__

    # --------------------------Help Text--------------------------------------------
    def get_help(self):#Função que chama a help
        return "Permite a operação lógica 'E' entre as duas entradas. Para esse bloco há duas possibilidades.\
        Primeira: Executa a operação entre duas imagens ponto a ponto.\
        Segunda: Executa a operação entre um valor constante e cada ponto da imagem."

    # ----------------------------------------------------------------------
    def generate_header(self):
        return self.get_adjust_images_size()

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        return \
            '\nif(block$id$_img_i1 && block$id$_img_i2){\n' + \
            'block$id$_img_o1 = cvCloneImage(block$id$_img_i1);\n' + \
            'adjust_images_size(block$id$_img_i1, block$id$_img_i2, block$id$_img_o1);\n' + \
            'cvAnd(block$id$_img_i1, block$id$_img_i2, block$id$_img_o1,0);\n' + \
            'cvResetImageROI(block$id$_img_o1);\n' + \
            '}\n'

    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ------------------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
                "Label": "And",
                "Icon": "images/and.png",
                "Color": "10:180:10:150",
                "InTypes": {0: "HRP_IMAGE", 1: "HRP_IMAGE"},
                "OutTypes": {0: "HRP_IMAGE"},
                "Description": "Logical AND operation between two images.",
                "TreeGroup": "Arithmetic and logical operations"
                }

    # ------------------------------------------------------------------------------
    def get_properties(self):
        return {}

# ------------------------------------------------------------------------------