#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      AIAA
#
# Created:     14-12-2011
# Copyright:   (c) AIAA 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import configobj
import oplPyUtilities
import os

class settings():
    def __init__(self):
        self.name="Render Assistant"
        self.iconPath="F:/Kumaresan/Dev/Python/lra/res/icons"
        self.rtcounter=0
        self.mayafolder="E:/adm/Maya2012"
        self.mayabinfolder="E:/adm/Maya2012/bin"
        self.mayabatchexefile="E:/adm/Maya2012/bin/mayabatch.exe"
        self.mayarenderexefile="E:/adm/Maya2012/bin/render.exe"
        self.renderLogsFolder= os.path.join(os.getcwd(),"renderlogs")
        self.appLogsFolder= os.path.join(os.getcwd(),"applogs")
        self.consoleLogsFolder =  os.path.join(os.getcwd(),"consolelogs")
        self.colVis=""


class Configs(settings):
    def __init__(self, file="settings.ini", autoLoad=True):
        settings.__init__(self)
        self._muti = oplPyUtilities.oplPyUtilities()
        self._cfg = configobj.ConfigObj(file)
        if autoLoad: self.loadSettings()

    def loadSettings(self):
        attribs = self._muti.getAttributes(self)
        for eachAttrib in attribs:
            if (self._cfg.dict().has_key(eachAttrib[0])):
                setattr(self,eachAttrib[0],self._cfg[eachAttrib[0]])
            else:
                self._cfg[eachAttrib[0]]=getattr(self,eachAttrib[0])
                self._cfg.write()

    def saveSettings(self):
        attribs = self._muti.getAttributes(self)
        for eachAttrib in attribs:
            self._cfg[eachAttrib[0]]=getattr(self,eachAttrib[0])
        self._cfg.write()

if '__main__' == __name__:
    cfg = Configs()
    #cfg.appName="newName"
    #cfg.saveSettings()
    print cfg.saveSettings()

