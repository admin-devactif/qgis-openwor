# -*- coding: iso-8859-1 -*-

from __future__ import absolute_import
from builtins import object
from imp import reload
from qgis.PyQt import QtCore
from qgis.PyQt.QtCore import QObject
from qgis.PyQt.QtWidgets import QMenu, QAction

import sys
from . import doAbout
from . import doFOpenWor


class MainPlugin(object):
  def __init__(self, iface):
    self.name = "OpenWor"
    self.iface = iface
    
  def startRender(self, context):
    pass

  def stopRender(self, context):
    pass    

  def initGui(self):
    self.menu=QMenu("OpenWor 1.9")

    self.fopenwor = QAction("Charger des documents ...",self.iface.mainWindow())
    self.fopenwor.setText(QtCore.QCoreApplication.translate("main", "Charger des documents ..."))
    self.fopenwor.triggered.connect(self.clickFOpenWor)

    self.about = QAction("A propos ...",self.iface.mainWindow())
    self.about.setText(QtCore.QCoreApplication.translate("main", "A propos ..."))
    self.about.triggered.connect(self.clickAbout)

    self.menu.addAction(self.fopenwor)
    self.menu.addSeparator()
    self.menu.addAction(self.about)

    menuBar = self.iface.mainWindow().menuBar()
    menuBar.addMenu(self.menu)

    reload(sys)
    sys.setdefaultencoding( "iso-8859-1" )

  def clickAbout(self):
    d = doAbout.Dialog()
    d.exec_()

  def clickFOpenWor(self):
    d = doFOpenWor.Dialog(self.iface)
    d.exec_()  
  
  def unload(self):
    pass    

