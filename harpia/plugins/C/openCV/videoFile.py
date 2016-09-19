#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.constants import *
import gettext
_ = gettext.gettext
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin

class VideoFile(OpenCVPlugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.id = -1
        self.type = self.__class__.__module__
        self.filename = "/usr/share/harpia/images/vLeft.mpg"

    # ----------------------------------------------------------------------
    def get_help(self):
        return "Realiza a aquisição de uma imagem a partir de algum dispositivo,\
        seja este uma mídia ou um dispositivo de aquisição de imagens (câmera, scanner)."

    # ----------------------------------------------------------------------
    def generate_vars(self):
        return \
            'CvCapture * block$id$_capture = NULL;\n'+ \
            'IplImage * block$id$_frame = NULL;\n' + \
            'block$id$_capture = cvCreateFileCapture("$filename$");\n' + \
            'IplImage * block$id$_img_o1 = NULL; //Capture\n'

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        return \
                '// Video Mode \n' + \
                'cvGrabFrame(block$id$_capture);\n' + \
                'block$id$_frame = cvRetrieveFrame (block$id$_capture);\n' + \
                'if(!block$id$_frame){\n'+\
                'cvSetCaptureProperty(block$id$_capture, CV_CAP_PROP_POS_AVI_RATIO , 0);\n' + \
                'continue;\n' + \
                '}\n' + \
                'block$id$_img_o1 = cvCloneImage(block$id$_frame);\n'

    # ----------------------------------------------------------------------
    def generate_out_dealloc(self):
        return 'cvReleaseCapture(&block$id$_capture);\n'


    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
         "Label":_("Video File"),
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