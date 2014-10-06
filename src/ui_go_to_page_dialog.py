# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/go_to_page_dialog.ui'
#
# Created: Mon Oct  6 08:08:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GoPageDialog(object):
    def setupUi(self, GoPageDialog):
        GoPageDialog.setObjectName("GoPageDialog")
        GoPageDialog.resize(283, 513)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/forest.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GoPageDialog.setWindowIcon(icon)
        GoPageDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(GoPageDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(GoPageDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtGui.QScrollArea(self.groupBox)
        self.scrollArea.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 259, 354))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_icon = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_icon.setText("")
        self.label_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout.addWidget(self.label_icon)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_num_pages = QtGui.QLabel(GoPageDialog)
        self.label_num_pages.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_num_pages.setObjectName("label_num_pages")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_num_pages)
        self.lineEdit_num_page = QtGui.QLineEdit(GoPageDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_num_page.sizePolicy().hasHeightForWidth())
        self.lineEdit_num_page.setSizePolicy(sizePolicy)
        self.lineEdit_num_page.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.lineEdit_num_page.setFrame(True)
        self.lineEdit_num_page.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_num_page.setReadOnly(True)
        self.lineEdit_num_page.setObjectName("lineEdit_num_page")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_num_page)
        self.label_current_page = QtGui.QLabel(GoPageDialog)
        self.label_current_page.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_current_page.setObjectName("label_current_page")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_current_page)
        self.lineEdit_current_page = QtGui.QLineEdit(GoPageDialog)
        self.lineEdit_current_page.setFrame(True)
        self.lineEdit_current_page.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_current_page.setReadOnly(True)
        self.lineEdit_current_page.setObjectName("lineEdit_current_page")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_current_page)
        self.label_go_page = QtGui.QLabel(GoPageDialog)
        self.label_go_page.setObjectName("label_go_page")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_go_page)
        self.spinBox_go_page = QtGui.QSpinBox(GoPageDialog)
        self.spinBox_go_page.setWrapping(False)
        self.spinBox_go_page.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_go_page.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spinBox_go_page.setAccelerated(True)
        self.spinBox_go_page.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox_go_page.setSuffix("")
        self.spinBox_go_page.setMinimum(1)
        self.spinBox_go_page.setObjectName("spinBox_go_page")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox_go_page)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(GoPageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(GoPageDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), GoPageDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), GoPageDialog.reject)
        QtCore.QObject.connect(self.spinBox_go_page, QtCore.SIGNAL("valueChanged(int)"), GoPageDialog.update)
        QtCore.QMetaObject.connectSlotsByName(GoPageDialog)

    def retranslateUi(self, GoPageDialog):
        GoPageDialog.setWindowTitle(QtGui.QApplication.translate("GoPageDialog", "Go to Page", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("GoPageDialog", "Page Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_num_pages.setText(QtGui.QApplication.translate("GoPageDialog", "Number of pages: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_current_page.setText(QtGui.QApplication.translate("GoPageDialog", "Current page:        ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_go_page.setText(QtGui.QApplication.translate("GoPageDialog", "Go to page:           ", None, QtGui.QApplication.UnicodeUTF8))
