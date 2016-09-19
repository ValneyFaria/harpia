#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.constants import *
import gettext
_ = gettext.gettext
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin

class ImageFile(OpenCVPlugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.id = -1
        self.type = self.__class__.__module__
        self.filename = "/usr/share/harpia/images/lenna.png"

    # ----------------------------------------------------------------------
    def get_help(self):
        return "Realiza a aquisição de uma imagem a partir de algum dispositivo,\
        seja este uma mídia ou um dispositivo de aquisição de imagens (câmera, scanner)."

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        return \
            'block$id$_img_o1 = cvLoadImage("$filename$",-1);\n'

    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
         "Label":_("Image File"),
         "Icon":"images/acquisition.png",
         "Color":"50:100:200:150",
         "InTypes":"",
         "OutTypes":{0:"HRP_IMAGE"},
         "Description":_("Create a new image or load image from a source, such as file, camera, frame grabber."),
         "TreeGroup":_("Image Source"),
         "IsSource":True
         }


    # ----------------------------------------------------------------------
    def get_properties(self):
        return {"filename":{"name": "File Name",
                            "type": HARPIA_OPEN_FILE,
                            "value": self.filename}
                }
# ------------------------------------------------------------------------------