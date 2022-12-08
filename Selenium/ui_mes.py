# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Aluko_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(558, 218)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(558, 218))
        icon = QIcon()
        icon.addFile(u":/IMG/dist/IMG/aluko_logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(5.000000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindows{\n"
"background-color: rgb(255, 255, 255)\n"
"}")
        MainWindow.setIconSize(QSize(15, 8))
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_file = QLabel(self.centralwidget)
        self.txt_file.setObjectName(u"txt_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_file.sizePolicy().hasHeightForWidth())
        self.txt_file.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(8)
        self.txt_file.setFont(font)
        self.txt_file.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.txt_file, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cbx_transaction = QComboBox(self.groupBox)
        self.cbx_transaction.addItem("")
        self.cbx_transaction.addItem("")
        self.cbx_transaction.addItem("")
        self.cbx_transaction.addItem("")
        self.cbx_transaction.addItem("")
        self.cbx_transaction.setObjectName(u"cbx_transaction")
        sizePolicy1.setHeightForWidth(self.cbx_transaction.sizePolicy().hasHeightForWidth())
        self.cbx_transaction.setSizePolicy(sizePolicy1)
        self.cbx_transaction.setMinimumSize(QSize(0, 0))
        self.cbx_transaction.setSizeIncrement(QSize(0, 0))
        self.cbx_transaction.setFont(font)

        self.verticalLayout_3.addWidget(self.cbx_transaction)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.btn_open = QPushButton(self.groupBox)
        self.btn_open.setObjectName(u"btn_open")
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        self.btn_open.setMinimumSize(QSize(100, 20))
        self.btn_open.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setWeight(50)
        font2.setKerning(False)
        self.btn_open.setFont(font2)
        self.btn_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open.setMouseTracking(False)
        self.btn_open.setTabletTracking(False)
        self.btn_open.setContextMenuPolicy(Qt.NoContextMenu)
        self.btn_open.setAcceptDrops(False)
        self.btn_open.setLayoutDirection(Qt.LeftToRight)
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius: 12  px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(159,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/IMG/dist/IMG/OIP.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open.setIcon(icon1)
        self.btn_open.setIconSize(QSize(15, 15))

        self.verticalLayout_3.addWidget(self.btn_open)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.groupBox_2.setFont(font3)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_create = QPushButton(self.groupBox_2)
        self.btn_create.setObjectName(u"btn_create")
        sizePolicy1.setHeightForWidth(self.btn_create.sizePolicy().hasHeightForWidth())
        self.btn_create.setSizePolicy(sizePolicy1)
        self.btn_create.setMinimumSize(QSize(0, 0))
        self.btn_create.setFont(font1)
        self.btn_create.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(159,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_create)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.btn_change = QPushButton(self.groupBox_2)
        self.btn_change.setObjectName(u"btn_change")
        sizePolicy1.setHeightForWidth(self.btn_change.sizePolicy().hasHeightForWidth())
        self.btn_change.setSizePolicy(sizePolicy1)
        self.btn_change.setMinimumSize(QSize(0, 0))
        self.btn_change.setFont(font1)
        self.btn_change.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_change.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(159,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_change)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.groupBox_2)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 3, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.lb_sid = QLabel(self.centralwidget)
        self.lb_sid.setObjectName(u"lb_sid")
        sizePolicy.setHeightForWidth(self.lb_sid.sizePolicy().hasHeightForWidth())
        self.lb_sid.setSizePolicy(sizePolicy)
        self.lb_sid.setMinimumSize(QSize(0, 30))
        self.lb_sid.setFont(font1)

        self.horizontalLayout_4.addWidget(self.lb_sid)

        self.cbx_sid = QComboBox(self.centralwidget)
        self.cbx_sid.addItem("")
        self.cbx_sid.addItem("")
        self.cbx_sid.addItem("")
        self.cbx_sid.setObjectName(u"cbx_sid")
        sizePolicy.setHeightForWidth(self.cbx_sid.sizePolicy().hasHeightForWidth())
        self.cbx_sid.setSizePolicy(sizePolicy)
        self.cbx_sid.setMinimumSize(QSize(0, 0))
        self.cbx_sid.setSizeIncrement(QSize(0, 30))
        self.cbx_sid.setFont(font)

        self.horizontalLayout_4.addWidget(self.cbx_sid)

        self.lb_clt = QLabel(self.centralwidget)
        self.lb_clt.setObjectName(u"lb_clt")
        sizePolicy.setHeightForWidth(self.lb_clt.sizePolicy().hasHeightForWidth())
        self.lb_clt.setSizePolicy(sizePolicy)
        self.lb_clt.setMinimumSize(QSize(0, 30))
        self.lb_clt.setFont(font1)

        self.horizontalLayout_4.addWidget(self.lb_clt)

        self.cbx_client = QComboBox(self.centralwidget)
        self.cbx_client.addItem("")
        self.cbx_client.addItem("")
        self.cbx_client.addItem("")
        self.cbx_client.addItem("")
        self.cbx_client.setObjectName(u"cbx_client")
        sizePolicy.setHeightForWidth(self.cbx_client.sizePolicy().hasHeightForWidth())
        self.cbx_client.setSizePolicy(sizePolicy)
        self.cbx_client.setMinimumSize(QSize(0, 0))
        self.cbx_client.setSizeIncrement(QSize(0, 30))
        self.cbx_client.setFont(font)

        self.horizontalLayout_4.addWidget(self.cbx_client)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_usr = QLabel(self.centralwidget)
        self.lb_usr.setObjectName(u"lb_usr")
        sizePolicy1.setHeightForWidth(self.lb_usr.sizePolicy().hasHeightForWidth())
        self.lb_usr.setSizePolicy(sizePolicy1)
        self.lb_usr.setMinimumSize(QSize(0, 0))
        self.lb_usr.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lb_usr)

        self.txt_usr = QLineEdit(self.centralwidget)
        self.txt_usr.setObjectName(u"txt_usr")
        sizePolicy1.setHeightForWidth(self.txt_usr.sizePolicy().hasHeightForWidth())
        self.txt_usr.setSizePolicy(sizePolicy1)
        self.txt_usr.setMinimumSize(QSize(0, 0))
        self.txt_usr.setFont(font)
        self.txt_usr.setMaxLength(6)

        self.horizontalLayout_5.addWidget(self.txt_usr)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_pw = QLabel(self.centralwidget)
        self.lb_pw.setObjectName(u"lb_pw")
        sizePolicy1.setHeightForWidth(self.lb_pw.sizePolicy().hasHeightForWidth())
        self.lb_pw.setSizePolicy(sizePolicy1)
        self.lb_pw.setMinimumSize(QSize(0, 0))
        self.lb_pw.setSizeIncrement(QSize(0, 0))
        self.lb_pw.setFont(font1)

        self.horizontalLayout_6.addWidget(self.lb_pw)

        self.txt_pw = QLineEdit(self.centralwidget)
        self.txt_pw.setObjectName(u"txt_pw")
        self.txt_pw.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.txt_pw.sizePolicy().hasHeightForWidth())
        self.txt_pw.setSizePolicy(sizePolicy1)
        self.txt_pw.setMinimumSize(QSize(0, 0))
        self.txt_pw.setFont(font)
        self.txt_pw.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_pw)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cbox_saveinfo = QCheckBox(self.centralwidget)
        self.cbox_saveinfo.setObjectName(u"cbox_saveinfo")
        sizePolicy1.setHeightForWidth(self.cbox_saveinfo.sizePolicy().hasHeightForWidth())
        self.cbox_saveinfo.setSizePolicy(sizePolicy1)
        self.cbox_saveinfo.setFont(font)
        self.cbox_saveinfo.setChecked(True)

        self.horizontalLayout_7.addWidget(self.cbox_saveinfo)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.btn_login = QPushButton(self.centralwidget)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy1.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy1)
        self.btn_login.setMinimumSize(QSize(0, 0))
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(159,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_login)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_file.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://alukovn-my.sharepoint.com/:x:/g/personal/tu_nguyen_anh_ialu_vn/Ee20I94bKbRBooHTwGcw0ukBRnWYl13nDcm4RXJzr_Ij8A?e=NjT3bN\"><span style=\" font-weight:600; color:#0000ff;\">Aluko Robotic Process Automation</span></a></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Transaction", None))
        self.cbx_transaction.setItemText(0, QCoreApplication.translate("MainWindow", u"Material Master Data", None))
        self.cbx_transaction.setItemText(1, QCoreApplication.translate("MainWindow", u"Direct Delivery", None))
        self.cbx_transaction.setItemText(2, QCoreApplication.translate("MainWindow", u"Business Partner", None))
        self.cbx_transaction.setItemText(3, QCoreApplication.translate("MainWindow", u"Purchase Info Record", None))
        self.cbx_transaction.setItemText(4, QCoreApplication.translate("MainWindow", u"GR Subcontracting", None))

        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Chose Excel File...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"CREATE", None))
        self.btn_change.setText(QCoreApplication.translate("MainWindow", u"CHANGE", None))
        self.lb_sid.setText(QCoreApplication.translate("MainWindow", u"SID: ", None))
        self.cbx_sid.setItemText(0, QCoreApplication.translate("MainWindow", u"PSA", None))
        self.cbx_sid.setItemText(1, QCoreApplication.translate("MainWindow", u"QSA", None))
        self.cbx_sid.setItemText(2, QCoreApplication.translate("MainWindow", u"DSA", None))

        self.lb_clt.setText(QCoreApplication.translate("MainWindow", u"Client:", None))
        self.cbx_client.setItemText(0, QCoreApplication.translate("MainWindow", u"100", None))
        self.cbx_client.setItemText(1, QCoreApplication.translate("MainWindow", u"200", None))
        self.cbx_client.setItemText(2, QCoreApplication.translate("MainWindow", u"300", None))
        self.cbx_client.setItemText(3, QCoreApplication.translate("MainWindow", u"500", None))

        self.lb_usr.setText(QCoreApplication.translate("MainWindow", u"User Name:", None))
        self.txt_usr.setText(QCoreApplication.translate("MainWindow", u"AMMP35", None))
        self.lb_pw.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.txt_pw.setText(QCoreApplication.translate("MainWindow", u"ALT147852369", None))
        self.cbox_saveinfo.setText(QCoreApplication.translate("MainWindow", u"Save Infomation", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/IMG/dist/IMG/Aluko_Group.png\" width=\"100\" height=\"70\" /></p></body></html>", None))
    # retranslateUi

