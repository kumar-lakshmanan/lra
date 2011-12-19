#-------------------------------------------------------------------------------
# Name:        lra - Entry Module
# Purpose:
#
# Author:      AIAA
#
# Created:     11-12-2011
# Copyright:   (c) AIAA 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
import os

##Remove cached custom modules from memory except preloaded IDE modules
if __name__ == '__main__':
    if globals().has_key('InitialModules'):
         for CustomModule in [Module for Module in sys.modules.keys() if Module not in InitialModules]:
            del(sys.modules[CustomModule])
    else:
        InitialModules = sys.modules.keys()


#######Appending Module Search Path########
if __name__ == '__main__':
    currentFolder = os.getcwd()

####Adjust these Parent Folder to reach root folder####
    parentFolder1 = os.path.dirname(currentFolder)
    parentFolder2 = os.path.dirname(parentFolder1)

####Pass parentFolder Level to reach Root folder####
    rootFolder = os.path.dirname(parentFolder2)
    rootFolderParent = os.path.dirname(rootFolder)

####Module Pack folders that will be added to sys search path####
    modulePathList = [
                      parentFolder1 + '/lra',
                      parentFolder1 + '/lra/lib',
                      parentFolder1 + '/lra/uis',
                      parentFolder1 + '/lra/res',
                      parentFolder1 + '/opl',
                      ##'F:\PYTHON\LIB',
                     ]

    for modulePath in modulePathList:
        if os.path.abspath(modulePath) not in sys.path:
            if os.path.exists(modulePath):
                sys.path.append(os.path.abspath(modulePath))

#Main Modules
from PyQt4 import QtCore, QtGui
import sip

#Custom Modules
from winMain import Ui_MainWindow
import oplQtSupport
import oplQtConnection
import oplQtTable
import oplQtList
import mIcons
import mSettings
import mRenderTask
import mDatas

class AppStart(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        #Defaults - Setup 1

        #Initializes Variables/Objects
        self.mApp = mSettings.Configs()
        self.mIcon = mIcons.Configs()
        self.qsup = oplQtSupport.oplQtSupport(self,self.mApp.iconPath)
        self.qcon = oplQtConnection.oplQtConnection(self)
        self.qtbl = oplQtTable.oplQtTable(self)
        self.qlst = oplQtList.oplQtList(self)
        self.rtaskSupport=mRenderTask.RenderTaskSupport(self, self.mIcon)
        self.mData = mDatas.Datas(self)

        #Initialize
        self.initalize()

        #Defaults - Setup 2
        self.rtaskCols = self.rtaskSupport.getFlagNamesAndFixedNames()
        self.rtaskSupport.rcnt = int(self.mApp.rtcounter)

        #Initial Setups
        self.doConnections()
        self.doUIReDesigns()

    def initalize(self):
        self.groupedWidgets = {
                                self.frmPropFrameRange:[
                                                        self.lePropStartFrame,
                                                        self.lePropEndFrame
                                                       ],
                                self.frmPropProjPath:[
                                                        self.lePropProjPath
                                                     ]
                              }
        self.propWidgets = self.__allPropWidgets()
        self.rtaskSupport.initalizeFlags(self.propWidgets)

    def __allPropWidgets(self):
        ret = []
        for each in self.groupedWidgets.keys():
            ret = ret + self.groupedWidgets[each]
        return ret

    def getFlagParentWidget(self, widget):
        ret = None
        for each in self.groupedWidgets.keys():
            if widget in self.groupedWidgets[each]:
                ret = each
        return ret

    def doUIReDesigns(self):
        self.setWindowTitle(self.mApp.name)

        self.qsup.setIcon(self,self.mIcon.star)
        self.qsup.setIcon(self.btnStartRender, self.mIcon.home)
        self.qsup.setIcon(self.btnPropApply, self.mIcon.apply)
        self.qsup.setIcon(self.actionProperties, self.mIcon.female)
        self.qsup.setIcon(self.actionRenderTasks, self.mIcon.heart)
        self.qsup.setIcon(self.actionColumns, self.mIcon.apply)

        self.qtbl.initializing(self.tblMainList,self.rtaskCols)
        self.qtbl.formatting(self.tblMainList,sortingEnabled=True)

        #Inital Settings 1
        self.actionProperties.setChecked(False)
        self.actionColumns.setChecked(False)

        #Initial Populates
        self.mData.doPopulateColumnsList()
        self.mData.doPrepareColumns()

        #Load Layout
        self.qsup.uiLayoutRestore()

    def doConnections(self):
        self.qcon.sigConnect(self.btnStartRender, "clicked()", self.sigBtnActions)
        self.qcon.sigConnect(self.btnPropApply, "clicked()", self.sigBtnActions)
        self.qcon.sigConnect(self.tblMainList, "clicked(QModelIndex)", self.sigTblActions)
        self.qcon.sigConnect(self.lstColumns, "itemClicked(QListWidgetItem*)", self.sigLstActions)

        self.qcon.sigConnect(self.actionRenderTasks, "toggled(bool)", self.sigToolBarAction)
        self.qcon.sigConnect(self.actionProperties, "toggled(bool)", self.sigToolBarAction)
        self.qcon.sigConnect(self.actionColumns, "toggled(bool)", self.sigToolBarAction)

        self.qcon.sigConnect(self.dckRenderTasks, "visibilityChanged(bool)", self.sigDckVisibiltyChange)
        self.qcon.sigConnect(self.dckProperties, "visibilityChanged(bool)", self.sigDckVisibiltyChange)
        self.qcon.sigConnect(self.dckColumns, "visibilityChanged(bool)", self.sigDckVisibiltyChange)

        self.qcon.connectToDragDropEx(self.tblMainList,self.sigTblDragDrop)
        self.qcon.connectToKeyPress(self.tblMainList,self.sigTblKeyPress)
        self.qcon.connectToClose(self,self.sigWinClose)

    def sigDckVisibiltyChange(self, *arg):
        self.sigJammer(True)
        self.actionColumns.setChecked(self.dckColumns.isVisible())
        self.actionProperties.setChecked(self.dckProperties.isVisible())
        self.actionRenderTasks.setChecked(self.dckRenderTasks.isVisible())
        self.sigJammer(False)

    def sigToolBarAction(self, *arg):
        self.sigJammer(True)
        sender = self.sender()
        if sender == self.actionColumns:
            self.dckColumns.setVisible(self.actionColumns.isChecked())
        if sender == self.actionProperties:
            self.dckProperties.setVisible(self.actionProperties.isChecked())
        if sender == self.actionRenderTasks:
            self.dckRenderTasks.setVisible(self.actionRenderTasks.isChecked())
        self.sigJammer(False)

    def sigLstActions(self, *arg):
        self.sigJammer()
        sender = self.sender()
        if sender is self.lstColumns:
            self.mData.doPrepareColumns()
        self.sigJammer(False)

    def sigTblKeyPress(self, *arg):
        self.sigJammer()
        sender = self.sender()
        key = self.qcon.keyEventInfo(arg[0])
        if key=="Delete":
            self.doRTaskDelete()
        if key==16777237:
            self.sigTblActions(None)
        if key==16777235:
            self.sigTblActions(None)
        self.sigJammer(False)

    def sigTblActions(self, *arg):
        self.sigJammer()
        sender = self.sender()
        if sender is self.tblMainList:
            self.doRTaskSelected()
        self.sigJammer(False)

    def sigBtnActions(self, *arg):
        self.sigJammer()
        sender = self.sender()
        if sender == self.btnPropApply:
            self.doRTaskUpdate()
        self.sigJammer(False)

    def sigWinClose(self, *arg):
        self.mApp.rtcounter=self.rtaskSupport.rcnt
        self.qsup.uiLayoutSave()
        self.mApp.saveSettings()
        self.mIcon.saveSettings()

    def sigTblDragDrop(self, *arg):
        files = self.qcon.dropEventInfoEx(arg[0])
        for eachFile in files:
            self.doRTaskAdd(eachFile)

    def doRTaskSelected(self):
        rtask = self._getSelectedRTask()
        if rtask:
            self.doRTaskFlagPopulate(rtask)

    def doRTaskAdd(self, file):
        rt = mRenderTask.RenderTask(file)
        rtId = self.rtaskSupport.rcnt+1
        rtIcon = self.rtaskSupport.getIconForStatus(rt.status)
        rtStatus = self.rtaskSupport.getStatusNameForStatus(rt.status)
        rowData = [
                    str(rtId).zfill(4),     #ID
                    rtStatus,               #STATUS
                    rt.fileName,            #FILEPATH
                    rt.addedOn,             #ADDEDON
                    rt.completedOn,         #COMPLETEDON
                  ] + self.rtaskSupport.emptyFlags()
        rowItems = self.qtbl.addRow(self.tblMainList,rowData,1)
        self.qtbl.setTag(rowItems[0],'tag',rt)
        self.qsup.setIcon(rowItems[1],rtIcon)
        rowItems[2].setToolTip(rt.filePath)
        self.qtbl.resizeColumnsEx(self.tblMainList)
        self.rtaskSupport.rcnt=rtId


    def doRTaskUpdate(self):
        rtask = self._getSelectedRTask()
        rows = self.qtbl.getSelectedRowNo(self.tblMainList)

        if rtask:
            wdgts = self.__enabledFlags()

            #Flags of RTASK Got updated.
            self.rtaskSupport.rtaskUpdate(rtask, wdgts)
            #Now to update the UI columns.

            row = rows[0]
            #Clear First
            for widget in self.propWidgets:
                flagFullName,flagShortName = self.rtaskSupport.getFlagInfoCore(widget)
                col = self.qtbl.getHeaderColNo(self.tblMainList,flagFullName)
                item = self.tblMainList.item(row,col)
                if (item): item.setText('')

            #Populate First
            for eachFlag in rtask.flags:
                columnName = eachFlag['flagFullName']
                value = eachFlag['value']
                col = self.qtbl.getHeaderColNo(self.tblMainList,columnName)
                item = self.tblMainList.item(row,col)
                if (item): item.setText(value)

    def doRTaskFlagPopulate(self, rtask=None):
        rt = mRenderTask.RenderTask('') if not rtask else rtask
        self.lePropFileName.setText(rt.fileName)
        self.lePropFilePath.setText(rt.filePath)

        #Clear First
        for eachWidget in self.propWidgets:
            group = self.getFlagParentWidget(eachWidget)
            group.setChecked(False)
            self.qsup.setText(eachWidget,'')

        #PopulateNext
        for eachWidget in self.propWidgets:
            for eachFlag in rt.flags:
                flagFullName = eachFlag['flagFullName']
                flagShortName = eachFlag['flagShortName']
                value = eachFlag['value']
                widget = eachFlag['widget']
                if eachWidget == widget:
                    group = self.getFlagParentWidget(widget)
                    group.setChecked(True)
                    self.qsup.setText(widget,value)

    def doRTaskDelete(self):
        rows = self.qtbl.getSelectedRowNo(self.tblMainList)
        if rows:
            for eachRow in rows: self.tblMainList.removeRow(eachRow)

    def _getSelectedRTask(self, all=False):
        rows = self.qtbl.getSelectedRowNo(self.tblMainList)
        if rows:
            if all:
                ret = []
                for eachRow in rows:
                    items = self.qtbl.getRowItems(self.tblMainList, eachRow)
                    rtask = self.qtbl.getTag(items[0])
                    ret.append(rtask)
            else:
                ret = None
                items = self.qtbl.getRowItems(self.tblMainList, rows[0])
                ret = self.qtbl.getTag(items[0])

        return ret


    def __enabledFlags(self):
        wdgts = []
        for grp in self.groupedWidgets.keys():
            if grp.isChecked():
                for item in self.groupedWidgets[grp]:
                    wdgts.append(item)
        return wdgts

    def sigJammer(self,jam=True):
        self.dckRenderTasks.blockSignals(jam)
        self.dckProperties.blockSignals(jam)
        self.dckColumns.blockSignals(jam)
        self.actionRenderTasks.blockSignals(jam)
        self.actionProperties.blockSignals(jam)
        self.actionColumns.blockSignals(jam)

if '__main__' == __name__:
    try:
        sip.delete(app)
    except:
        try:
            del(app)
        except:
            pass

    inst = QtGui.QApplication.instance()
    if inst:
        inst.exit()
        inst.quit()
        del(inst)

    app = QtGui.QApplication(sys.argv)
    ui = AppStart()
    ui.show()
    ec = app.exec_()
    app.closeAllWindows()
    app.exit()
    app.quit()
    del(ui)
    del(app)
    sys.exit(ec)