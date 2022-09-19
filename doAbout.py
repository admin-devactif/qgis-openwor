from __future__ import absolute_import

from qgis.PyQt.QtWidgets import QDialog

from .about import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
