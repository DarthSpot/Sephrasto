# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterBeschreibung.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_formBeschreibung(object):
    def setupUi(self, formBeschreibung):
        formBeschreibung.setObjectName("formBeschreibung")
        formBeschreibung.resize(872, 460)
        self.gridLayout_3 = QtWidgets.QGridLayout(formBeschreibung)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(formBeschreibung)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)
        self.editKurzbeschreibung = QtWidgets.QLineEdit(formBeschreibung)
        self.editKurzbeschreibung.setObjectName("editKurzbeschreibung")
        self.gridLayout.addWidget(self.editKurzbeschreibung, 6, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(formBeschreibung)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(formBeschreibung)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(formBeschreibung)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.editName = QtWidgets.QLineEdit(formBeschreibung)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(formBeschreibung)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.comboFinanzen = QtWidgets.QComboBox(formBeschreibung)
        self.comboFinanzen.setMaxVisibleItems(5)
        self.comboFinanzen.setObjectName("comboFinanzen")
        self.comboFinanzen.addItem("")
        self.comboFinanzen.addItem("")
        self.comboFinanzen.addItem("")
        self.comboFinanzen.addItem("")
        self.comboFinanzen.addItem("")
        self.gridLayout.addWidget(self.comboFinanzen, 4, 2, 1, 1)
        self.comboStatus = QtWidgets.QComboBox(formBeschreibung)
        self.comboStatus.setMaxVisibleItems(5)
        self.comboStatus.setMinimumContentsLength(0)
        self.comboStatus.setObjectName("comboStatus")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.gridLayout.addWidget(self.comboStatus, 3, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.editEig1 = QtWidgets.QLineEdit(formBeschreibung)
        self.editEig1.setMinimumSize(QtCore.QSize(200, 0))
        self.editEig1.setObjectName("editEig1")
        self.gridLayout_2.addWidget(self.editEig1, 0, 0, 1, 1)
        self.editEig6 = QtWidgets.QLineEdit(formBeschreibung)
        self.editEig6.setMinimumSize(QtCore.QSize(200, 0))
        self.editEig6.setObjectName("editEig6")
        self.gridLayout_2.addWidget(self.editEig6, 2, 1, 1, 1)
        self.editEig3 = QtWidgets.QLineEdit(formBeschreibung)
        self.editEig3.setMinimumSize(QtCore.QSize(200, 0))
        self.editEig3.setObjectName("editEig3")
        self.gridLayout_2.addWidget(self.editEig3, 1, 0, 1, 1)
        self.editEig5 = QtWidgets.QLineEdit(formBeschreibung)
        self.editEig5.setMinimumSize(QtCore.QSize(200, 0))
        self.editEig5.setObjectName("editEig5")
        self.gridLayout_2.addWidget(self.editEig5, 2, 0, 1, 1)
        self.editEig4 = QtWidgets.QLineEdit(formBeschreibung)
        self.editEig4.setMinimumSize(QtCore.QSize(200, 0))
        self.editEig4.setObjectName("editEig4")
        self.gridLayout_2.addWidget(self.editEig4, 1, 1, 1, 1)
        self.editEig2 = QtWidgets.QLineEdit(formBeschreibung)
        self.editEig2.setMinimumSize(QtCore.QSize(200, 0))
        self.editEig2.setObjectName("editEig2")
        self.gridLayout_2.addWidget(self.editEig2, 0, 1, 1, 1)
        self.editEig7 = QtWidgets.QLineEdit(formBeschreibung)
        self.editEig7.setMinimumSize(QtCore.QSize(200, 0))
        self.editEig7.setObjectName("editEig7")
        self.gridLayout_2.addWidget(self.editEig7, 3, 0, 1, 1)
        self.editEig8 = QtWidgets.QLineEdit(formBeschreibung)
        self.editEig8.setMinimumSize(QtCore.QSize(200, 0))
        self.editEig8.setObjectName("editEig8")
        self.gridLayout_2.addWidget(self.editEig8, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 7, 2, 1, 1)
        self.editRasse = QtWidgets.QLineEdit(formBeschreibung)
        self.editRasse.setObjectName("editRasse")
        self.gridLayout.addWidget(self.editRasse, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(formBeschreibung)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(formBeschreibung)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 1, 1, 1)
        self.comboHeimat = QtWidgets.QComboBox(formBeschreibung)
        self.comboHeimat.setObjectName("comboHeimat")
        self.comboHeimat.addItem("")
        self.comboHeimat.addItem("")
        self.comboHeimat.addItem("")
        self.comboHeimat.addItem("")
        self.comboHeimat.addItem("")
        self.comboHeimat.addItem("")
        self.comboHeimat.addItem("")
        self.comboHeimat.addItem("")
        self.comboHeimat.addItem("")
        self.gridLayout.addWidget(self.comboHeimat, 5, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(formBeschreibung)
        self.comboFinanzen.setCurrentIndex(2)
        self.comboStatus.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(formBeschreibung)
        formBeschreibung.setTabOrder(self.editName, self.editRasse)
        formBeschreibung.setTabOrder(self.editRasse, self.comboStatus)
        formBeschreibung.setTabOrder(self.comboStatus, self.comboFinanzen)
        formBeschreibung.setTabOrder(self.comboFinanzen, self.comboHeimat)
        formBeschreibung.setTabOrder(self.comboHeimat, self.editKurzbeschreibung)
        formBeschreibung.setTabOrder(self.editKurzbeschreibung, self.editEig1)
        formBeschreibung.setTabOrder(self.editEig1, self.editEig2)
        formBeschreibung.setTabOrder(self.editEig2, self.editEig3)
        formBeschreibung.setTabOrder(self.editEig3, self.editEig4)
        formBeschreibung.setTabOrder(self.editEig4, self.editEig5)
        formBeschreibung.setTabOrder(self.editEig5, self.editEig6)
        formBeschreibung.setTabOrder(self.editEig6, self.editEig7)
        formBeschreibung.setTabOrder(self.editEig7, self.editEig8)

    def retranslateUi(self, formBeschreibung):
        _translate = QtCore.QCoreApplication.translate
        formBeschreibung.setWindowTitle(_translate("formBeschreibung", "Beschreibung"))
        self.label_4.setText(_translate("formBeschreibung", "Kurzbeschreibung"))
        self.label_6.setText(_translate("formBeschreibung", "Eigenheiten"))
        self.label.setText(_translate("formBeschreibung", "Name"))
        self.label_2.setText(_translate("formBeschreibung", "Rasse"))
        self.label_3.setText(_translate("formBeschreibung", "Status"))
        self.comboFinanzen.setItemText(0, _translate("formBeschreibung", "Sehr Reich"))
        self.comboFinanzen.setItemText(1, _translate("formBeschreibung", "Reich"))
        self.comboFinanzen.setItemText(2, _translate("formBeschreibung", "Normal"))
        self.comboFinanzen.setItemText(3, _translate("formBeschreibung", "Arm"))
        self.comboFinanzen.setItemText(4, _translate("formBeschreibung", "Sehr Arm"))
        self.comboStatus.setItemText(0, _translate("formBeschreibung", "Elite"))
        self.comboStatus.setItemText(1, _translate("formBeschreibung", "Oberschicht"))
        self.comboStatus.setItemText(2, _translate("formBeschreibung", "Mittelschicht"))
        self.comboStatus.setItemText(3, _translate("formBeschreibung", "Unterschicht"))
        self.comboStatus.setItemText(4, _translate("formBeschreibung", "Abschaum"))
        self.label_5.setText(_translate("formBeschreibung", "Finanzen"))
        self.label_7.setText(_translate("formBeschreibung", "Heimatgebiet"))
        self.comboHeimat.setItemText(0, _translate("formBeschreibung", "Mittelreich"))
        self.comboHeimat.setItemText(1, _translate("formBeschreibung", "Tulamidenlande"))
        self.comboHeimat.setItemText(2, _translate("formBeschreibung", "Horasreich"))
        self.comboHeimat.setItemText(3, _translate("formBeschreibung", "Südaventurien"))
        self.comboHeimat.setItemText(4, _translate("formBeschreibung", "Bornland"))
        self.comboHeimat.setItemText(5, _translate("formBeschreibung", "Thorwal"))
        self.comboHeimat.setItemText(6, _translate("formBeschreibung", "Maraskan"))
        self.comboHeimat.setItemText(7, _translate("formBeschreibung", "Elfen"))
        self.comboHeimat.setItemText(8, _translate("formBeschreibung", "Zwerge"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formBeschreibung = QtWidgets.QWidget()
    ui = Ui_formBeschreibung()
    ui.setupUi(formBeschreibung)
    formBeschreibung.show()
    sys.exit(app.exec_())

