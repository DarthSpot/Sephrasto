# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankEditManoever.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_manDialog(object):
    def setupUi(self, manDialog):
        manDialog.setObjectName("manDialog")
        manDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        manDialog.resize(440, 550)
        self.gridLayout_2 = QtWidgets.QGridLayout(manDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(manDialog)
        self.label_4.setMinimumSize(QtCore.QSize(110, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QPlainTextEdit(manDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(manDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.voraussetzungenEdit = QtWidgets.QPlainTextEdit(manDialog)
        self.voraussetzungenEdit.setObjectName("voraussetzungenEdit")
        self.gridLayout.addWidget(self.voraussetzungenEdit, 4, 1, 1, 1)
        self.probeEdit = QtWidgets.QLineEdit(manDialog)
        self.probeEdit.setObjectName("probeEdit")
        self.gridLayout.addWidget(self.probeEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(manDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(manDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(manDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(manDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gegenEdit = QtWidgets.QLineEdit(manDialog)
        self.gegenEdit.setObjectName("gegenEdit")
        self.gridLayout.addWidget(self.gegenEdit, 2, 1, 1, 1)
        self.comboTyp = QtWidgets.QComboBox(manDialog)
        self.comboTyp.setObjectName("comboTyp")
        self.comboTyp.addItem("")
        self.comboTyp.addItem("")
        self.comboTyp.addItem("")
        self.comboTyp.addItem("")
        self.gridLayout.addWidget(self.comboTyp, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(manDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(manDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(manDialog)
        self.buttonBox.accepted.connect(manDialog.accept)
        self.buttonBox.rejected.connect(manDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(manDialog)
        manDialog.setTabOrder(self.nameEdit, self.gegenEdit)
        manDialog.setTabOrder(self.gegenEdit, self.textEdit)

    def retranslateUi(self, manDialog):
        _translate = QtCore.QCoreApplication.translate
        manDialog.setWindowTitle(_translate("manDialog", "Sephrasto - Manöver / Modifikation bearbeiten..."))
        self.label_4.setText(_translate("manDialog", "Voraussetzungen"))
        self.label_3.setText(_translate("manDialog", "Gegenprobe"))
        self.label_2.setText(_translate("manDialog", "Probe"))
        self.label_5.setText(_translate("manDialog", "Beschreibung"))
        self.label.setText(_translate("manDialog", "Name"))
        self.comboTyp.setItemText(0, _translate("manDialog", "Nahkampfmanöver"))
        self.comboTyp.setItemText(1, _translate("manDialog", "Fernkampfmanöver"))
        self.comboTyp.setItemText(2, _translate("manDialog", "Magische Modifikation"))
        self.comboTyp.setItemText(3, _translate("manDialog", "Karmale Modifikation"))
        self.label_6.setText(_translate("manDialog", "Typ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manDialog = QtWidgets.QDialog()
    ui = Ui_manDialog()
    ui.setupUi(manDialog)
    manDialog.show()
    sys.exit(app.exec_())

