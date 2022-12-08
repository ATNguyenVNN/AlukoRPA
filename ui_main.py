# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_report.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QDateEdit, QDateTimeEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import Aluko_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1048, 687)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1048, 687))
        icon = QIcon()
        icon.addFile(u":/icons/dist/IMG/aluko_logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(20, 20))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:rgb(33.43,51);\n"
"}	")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setStyleSheet(u"alternate-background-color: rgb(32, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_top = QFrame(self.frame)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 0))
        self.frame_top.setMaximumSize(QSize(16777215, 84))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.frame_top)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_2 = QLabel(self.frame_top)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"color: rgb(7, 64, 128);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cbx_ribbon = QCheckBox(self.frame_top)
        self.cbx_ribbon.setObjectName(u"cbx_ribbon")
        self.cbx_ribbon.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbx_ribbon.setStyleSheet(u"QCheckBox::indicator{\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image:url(IMG/show.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"	image:url(IMG/hide.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  30px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.cbx_ribbon.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.cbx_ribbon)

        self.cbx_parameter = QCheckBox(self.frame_top)
        self.cbx_parameter.setObjectName(u"cbx_parameter")
        self.cbx_parameter.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbx_parameter.setStyleSheet(u"QCheckBox::indicator{\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image:url(IMG/left.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"	image:url(IMG/right.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  30px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.cbx_parameter.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.cbx_parameter)

        self.horizontalSpacer_6 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.btn_sql = QPushButton(self.frame_top)
        self.btn_sql.setObjectName(u"btn_sql")
        self.btn_sql.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/dist/IMG/db.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sql.setIcon(icon1)
        self.btn_sql.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_sql)

        self.btn_update = QPushButton(self.frame_top)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Button/dist/IMG/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon2)
        self.btn_update.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_update)

        self.btn_toggle = QPushButton(self.frame_top)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  60px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Button/dist/IMG/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon3)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle)


        self.verticalLayout_5.addWidget(self.frame_top)

        self.bottom_frame = QFrame(self.frame)
        self.bottom_frame.setObjectName(u"bottom_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bottom_frame.sizePolicy().hasHeightForWidth())
        self.bottom_frame.setSizePolicy(sizePolicy1)
        self.bottom_frame.setMaximumSize(QSize(16777215, 157))
        self.bottom_frame.setStyleSheet(u"color: rgb(7, 64, 128);")
        self.bottom_frame.setFrameShape(QFrame.Panel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_transaction = QFrame(self.bottom_frame)
        self.frame_transaction.setObjectName(u"frame_transaction")
        self.frame_transaction.setMaximumSize(QSize(285, 16777215))
        self.frame_transaction.setFrameShape(QFrame.StyledPanel)
        self.frame_transaction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_transaction)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_transaction = QLabel(self.frame_transaction)
        self.label_transaction.setObjectName(u"label_transaction")
        font = QFont()
        font.setBold(True)
        self.label_transaction.setFont(font)

        self.verticalLayout_4.addWidget(self.label_transaction)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.cbx_transaction = QComboBox(self.frame_transaction)
        icon4 = QIcon()
        icon4.addFile(u":/icons/dist/IMG/sap-logo-269309.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbx_transaction.addItem(icon4, "")
        self.cbx_transaction.addItem(icon4, "")
        self.cbx_transaction.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/icons/dist/IMG/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbx_transaction.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/icons/dist/IMG/mes_ui.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbx_transaction.addItem(icon6, "")
        self.cbx_transaction.addItem(icon1, "")
        self.cbx_transaction.setObjectName(u"cbx_transaction")
        self.cbx_transaction.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cbx_transaction.sizePolicy().hasHeightForWidth())
        self.cbx_transaction.setSizePolicy(sizePolicy)
        self.cbx_transaction.setMinimumSize(QSize(0, 30))
        self.cbx_transaction.setMaximumSize(QSize(16777215, 30))
        self.cbx_transaction.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(8)
        self.cbx_transaction.setFont(font1)
        self.cbx_transaction.setAutoFillBackground(False)
        self.cbx_transaction.setEditable(False)
        self.cbx_transaction.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_11.addWidget(self.cbx_transaction)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.act_Create = QRadioButton(self.frame_transaction)
        self.act_Create.setObjectName(u"act_Create")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.act_Create.sizePolicy().hasHeightForWidth())
        self.act_Create.setSizePolicy(sizePolicy2)
        self.act_Create.setCursor(QCursor(Qt.PointingHandCursor))
        self.act_Create.setChecked(True)

        self.horizontalLayout_13.addWidget(self.act_Create)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.act_Change = QRadioButton(self.frame_transaction)
        self.act_Change.setObjectName(u"act_Change")
        sizePolicy2.setHeightForWidth(self.act_Change.sizePolicy().hasHeightForWidth())
        self.act_Change.setSizePolicy(sizePolicy2)
        self.act_Change.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.act_Change)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.act_Delete = QRadioButton(self.frame_transaction)
        self.act_Delete.setObjectName(u"act_Delete")
        self.act_Delete.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.act_Delete.sizePolicy().hasHeightForWidth())
        self.act_Delete.setSizePolicy(sizePolicy2)
        self.act_Delete.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.act_Delete)

        self.horizontalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_23)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_3.addWidget(self.frame_transaction)

        self.frame_action = QFrame(self.bottom_frame)
        self.frame_action.setObjectName(u"frame_action")
        self.frame_action.setMaximumSize(QSize(320, 16777215))
        self.frame_action.setFrameShape(QFrame.StyledPanel)
        self.frame_action.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_action)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_action = QLabel(self.frame_action)
        self.label_action.setObjectName(u"label_action")
        self.label_action.setFont(font)

        self.verticalLayout_11.addWidget(self.label_action)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btn_open = QPushButton(self.frame_action)
        self.btn_open.setObjectName(u"btn_open")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy3)
        self.btn_open.setMinimumSize(QSize(120, 20))
        self.btn_open.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(True)
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
"	border-radius:  0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"	border-radius:  0px;\n"
"\n"
"}")
        self.btn_open.setIcon(icon5)
        self.btn_open.setIconSize(QSize(20, 20))

        self.horizontalLayout_19.addWidget(self.btn_open)

        self.horizontalSpacer_5 = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_5)

        self.label_10 = QLabel(self.frame_action)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.label_10)

        self.cbx_client_3 = QComboBox(self.frame_action)
        self.cbx_client_3.addItem("")
        self.cbx_client_3.addItem("")
        self.cbx_client_3.addItem("")
        self.cbx_client_3.addItem("")
        self.cbx_client_3.addItem("")
        self.cbx_client_3.addItem("")
        self.cbx_client_3.addItem("")
        self.cbx_client_3.addItem("")
        self.cbx_client_3.addItem("")
        self.cbx_client_3.addItem("")
        self.cbx_client_3.setObjectName(u"cbx_client_3")
        self.cbx_client_3.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.cbx_client_3.sizePolicy().hasHeightForWidth())
        self.cbx_client_3.setSizePolicy(sizePolicy3)
        self.cbx_client_3.setMinimumSize(QSize(60, 20))
        self.cbx_client_3.setSizeIncrement(QSize(0, 30))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.cbx_client_3.setFont(font3)

        self.horizontalLayout_19.addWidget(self.cbx_client_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_13)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_start = QPushButton(self.frame_action)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy4)
        self.btn_start.setMinimumSize(QSize(0, 0))
        self.btn_start.setFont(font3)
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Button/dist/IMG/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start.setIcon(icon7)
        self.btn_start.setIconSize(QSize(25, 25))

        self.horizontalLayout_18.addWidget(self.btn_start)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)

        self.btn_pause = QPushButton(self.frame_action)
        self.btn_pause.setObjectName(u"btn_pause")
        self.btn_pause.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.btn_pause.sizePolicy().hasHeightForWidth())
        self.btn_pause.setSizePolicy(sizePolicy4)
        self.btn_pause.setMinimumSize(QSize(0, 0))
        self.btn_pause.setFont(font3)
        self.btn_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pause.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Button/dist/IMG/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pause.setIcon(icon8)
        self.btn_pause.setIconSize(QSize(25, 25))

        self.horizontalLayout_18.addWidget(self.btn_pause)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)

        self.btn_stop = QPushButton(self.frame_action)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy4)
        self.btn_stop.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.btn_stop.setFont(font4)
        self.btn_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop.setAutoFillBackground(False)
        self.btn_stop.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Button/dist/IMG/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stop.setIcon(icon9)
        self.btn_stop.setIconSize(QSize(25, 25))

        self.horizontalLayout_18.addWidget(self.btn_stop)

        self.horizontalSpacer_20 = QSpacerItem(15, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_20)


        self.verticalLayout_11.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_3.addWidget(self.frame_action)

        self.frame_sql = QFrame(self.bottom_frame)
        self.frame_sql.setObjectName(u"frame_sql")
        sizePolicy.setHeightForWidth(self.frame_sql.sizePolicy().hasHeightForWidth())
        self.frame_sql.setSizePolicy(sizePolicy)
        self.frame_sql.setMaximumSize(QSize(16777215, 0))
        self.frame_sql.setStyleSheet(u"color: rgb(7, 64, 128);")
        self.frame_sql.setFrameShape(QFrame.StyledPanel)
        self.frame_sql.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_sql)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_44 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_44)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_slq_get = QPushButton(self.frame_sql)
        self.btn_slq_get.setObjectName(u"btn_slq_get")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_slq_get.sizePolicy().hasHeightForWidth())
        self.btn_slq_get.setSizePolicy(sizePolicy5)
        self.btn_slq_get.setMinimumSize(QSize(0, 0))
        self.btn_slq_get.setMaximumSize(QSize(16777215, 16777215))
        self.btn_slq_get.setFont(font3)
        self.btn_slq_get.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_slq_get.setStyleSheet(u"")
        self.btn_slq_get.setIconSize(QSize(18, 18))

        self.horizontalLayout_9.addWidget(self.btn_slq_get)

        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.cbx_inteface = QComboBox(self.frame_sql)
        self.cbx_inteface.addItem("")
        self.cbx_inteface.addItem(icon1, "")
        self.cbx_inteface.addItem(icon1, "")
        self.cbx_inteface.setObjectName(u"cbx_inteface")
        self.cbx_inteface.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.cbx_inteface.sizePolicy().hasHeightForWidth())
        self.cbx_inteface.setSizePolicy(sizePolicy3)
        self.cbx_inteface.setMinimumSize(QSize(100, 25))
        self.cbx_inteface.setMaximumSize(QSize(150, 16777215))
        self.cbx_inteface.setSizeIncrement(QSize(0, 0))
        self.cbx_inteface.setFont(font1)
        self.cbx_inteface.setAutoFillBackground(False)
        self.cbx_inteface.setEditable(True)
        self.cbx_inteface.setIconSize(QSize(16, 16))
        self.cbx_inteface.setFrame(False)

        self.horizontalLayout_9.addWidget(self.cbx_inteface)

        self.btn_sql_2 = QPushButton(self.frame_sql)
        self.btn_sql_2.setObjectName(u"btn_sql_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_sql_2.sizePolicy().hasHeightForWidth())
        self.btn_sql_2.setSizePolicy(sizePolicy6)
        self.btn_sql_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Button/dist/IMG/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sql_2.setIcon(icon10)
        self.btn_sql_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.btn_sql_2)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.txt_sql_querry = QLineEdit(self.frame_sql)
        self.txt_sql_querry.setObjectName(u"txt_sql_querry")
        sizePolicy.setHeightForWidth(self.txt_sql_querry.sizePolicy().hasHeightForWidth())
        self.txt_sql_querry.setSizePolicy(sizePolicy)
        self.txt_sql_querry.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setStrikeOut(False)
        font5.setKerning(False)
        self.txt_sql_querry.setFont(font5)
        self.txt_sql_querry.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_sql_querry.setDragEnabled(False)
        self.txt_sql_querry.setClearButtonEnabled(True)

        self.verticalLayout_8.addWidget(self.txt_sql_querry)


        self.horizontalLayout_3.addWidget(self.frame_sql)


        self.verticalLayout_5.addWidget(self.bottom_frame)

#         self.tb_ledger = QTableWidget(self.frame)
#         if (self.tb_ledger.columnCount() < 20):
#             self.tb_ledger.setColumnCount(20)
#         if (self.tb_ledger.rowCount() < 20):
#             self.tb_ledger.setRowCount(20)
#         self.tb_ledger.setObjectName(u"tb_ledger")
#         self.tb_ledger.setEnabled(True)
#         self.tb_ledger.setMaximumSize(QSize(16777215, 16777215))
#         self.tb_ledger.setFont(font1)
#         self.tb_ledger.setAutoFillBackground(True)
#         self.tb_ledger.setStyleSheet(u"        QHeaderView::section{\n"
# "			font: 75 9pt;\n"
# "            border-top:0px solid #D8D8D8;\n"
# "            border-left:0px solid #D8D8D8;\n"
# "            border-right:1px solid #D8D8D8;\n"
# "            border-bottom: 2px solid #D8D8D8;\n"
# "            background-color:white;\n"
# "            padding:3px;\n"
# "        }\n"
# "    ")
#         self.tb_ledger.setFrameShape(QFrame.VLine)
#         self.tb_ledger.setFrameShadow(QFrame.Plain)
#         self.tb_ledger.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
#         self.tb_ledger.setAutoScrollMargin(10)
#         self.tb_ledger.setDragEnabled(False)
#         self.tb_ledger.setDragDropOverwriteMode(False)
#         self.tb_ledger.setDragDropMode(QAbstractItemView.NoDragDrop)
#         self.tb_ledger.setDefaultDropAction(Qt.IgnoreAction)
#         self.tb_ledger.setAlternatingRowColors(False)
#         self.tb_ledger.setGridStyle(Qt.SolidLine)
#         self.tb_ledger.setSortingEnabled(True)
#         self.tb_ledger.setCornerButtonEnabled(True)
#         self.tb_ledger.setRowCount(20)
#         self.tb_ledger.setColumnCount(20)

#         self.verticalLayout_5.addWidget(self.tb_ledger)

        self.verticalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.txt_msg = QLabel(self.frame)
        self.txt_msg.setObjectName(u"txt_msg")
        self.txt_msg.setStyleSheet(u"color: rgb(7, 64, 128);")

        self.verticalLayout_5.addWidget(self.txt_msg)


        self.horizontalLayout_4.addWidget(self.frame)

        self.menu_parameter = QFrame(self.centralwidget)
        self.menu_parameter.setObjectName(u"menu_parameter")
        sizePolicy6.setHeightForWidth(self.menu_parameter.sizePolicy().hasHeightForWidth())
        self.menu_parameter.setSizePolicy(sizePolicy6)
        self.menu_parameter.setMinimumSize(QSize(0, 0))
        self.menu_parameter.setMaximumSize(QSize(0, 16777215))
        self.menu_parameter.setStyleSheet(u"color: rgb(7, 64, 128);")
        self.menu_parameter.setFrameShape(QFrame.StyledPanel)
        self.menu_parameter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_parameter)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.menu_parameter)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 1))
        self.frame_6.setStyleSheet(u"background-color: rgb(189, 112, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")

        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.menu_parameter)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy7)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gb_parameter = QGroupBox(self.frame_7)
        self.gb_parameter.setObjectName(u"gb_parameter")
        sizePolicy.setHeightForWidth(self.gb_parameter.sizePolicy().hasHeightForWidth())
        self.gb_parameter.setSizePolicy(sizePolicy)
        self.gb_parameter.setFont(font4)
        self.verticalLayout_9 = QVBoxLayout(self.gb_parameter)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_10 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_10)

        self.fm_parameter1 = QFrame(self.gb_parameter)
        self.fm_parameter1.setObjectName(u"fm_parameter1")
        sizePolicy.setHeightForWidth(self.fm_parameter1.sizePolicy().hasHeightForWidth())
        self.fm_parameter1.setSizePolicy(sizePolicy)
        self.fm_parameter1.setMaximumSize(QSize(16777215, 16777215))
        self.fm_parameter1.setFrameShape(QFrame.StyledPanel)
        self.fm_parameter1.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.fm_parameter1)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btn_sql_10 = QPushButton(self.fm_parameter1)
        self.btn_sql_10.setObjectName(u"btn_sql_10")
        sizePolicy6.setHeightForWidth(self.btn_sql_10.sizePolicy().hasHeightForWidth())
        self.btn_sql_10.setSizePolicy(sizePolicy6)
        self.btn_sql_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql_10.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/dist/IMG/lookup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sql_10.setIcon(icon11)
        self.btn_sql_10.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.btn_sql_10, 12, 4, 1, 1)

        self.btn_sql_9 = QPushButton(self.fm_parameter1)
        self.btn_sql_9.setObjectName(u"btn_sql_9")
        sizePolicy6.setHeightForWidth(self.btn_sql_9.sizePolicy().hasHeightForWidth())
        self.btn_sql_9.setSizePolicy(sizePolicy6)
        self.btn_sql_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql_9.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.btn_sql_9.setIcon(icon11)
        self.btn_sql_9.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.btn_sql_9, 10, 4, 1, 1)

        self.btn_sql_8 = QPushButton(self.fm_parameter1)
        self.btn_sql_8.setObjectName(u"btn_sql_8")
        sizePolicy6.setHeightForWidth(self.btn_sql_8.sizePolicy().hasHeightForWidth())
        self.btn_sql_8.setSizePolicy(sizePolicy6)
        self.btn_sql_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql_8.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.btn_sql_8.setIcon(icon11)
        self.btn_sql_8.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.btn_sql_8, 8, 4, 1, 1)

        self.para_1 = QLabel(self.fm_parameter1)
        self.para_1.setObjectName(u"para_1")
        self.para_1.setMaximumSize(QSize(80, 16777215))
        font6 = QFont()
        font6.setBold(False)
        font6.setItalic(False)
        self.para_1.setFont(font6)

        self.gridLayout_6.addWidget(self.para_1, 0, 0, 1, 1)

        self.para2 = QLabel(self.fm_parameter1)
        self.para2.setObjectName(u"para2")
        self.para2.setMaximumSize(QSize(80, 16777215))
        self.para2.setFont(font6)

        self.gridLayout_6.addWidget(self.para2, 2, 0, 1, 1)

        self.txt_initial_9 = QLineEdit(self.fm_parameter1)
        self.txt_initial_9.setObjectName(u"txt_initial_9")
        self.txt_initial_9.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_9, 0, 1, 1, 1)

        self.to_1 = QLabel(self.fm_parameter1)
        self.to_1.setObjectName(u"to_1")
        sizePolicy.setHeightForWidth(self.to_1.sizePolicy().hasHeightForWidth())
        self.to_1.setSizePolicy(sizePolicy)
        self.to_1.setMaximumSize(QSize(20, 16777215))
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(False)
        self.to_1.setFont(font7)

        self.gridLayout_6.addWidget(self.to_1, 0, 2, 1, 1)

        self.para3 = QLabel(self.fm_parameter1)
        self.para3.setObjectName(u"para3")
        self.para3.setMaximumSize(QSize(80, 16777215))
        self.para3.setFont(font6)

        self.gridLayout_6.addWidget(self.para3, 4, 0, 1, 1)

        self.to_3 = QLabel(self.fm_parameter1)
        self.to_3.setObjectName(u"to_3")
        self.to_3.setFont(font7)

        self.gridLayout_6.addWidget(self.to_3, 4, 2, 1, 1)

        self.to_2 = QLabel(self.fm_parameter1)
        self.to_2.setObjectName(u"to_2")
        self.to_2.setFont(font7)

        self.gridLayout_6.addWidget(self.to_2, 2, 2, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_27, 3, 2, 1, 1)

        self.btn_sql_4 = QPushButton(self.fm_parameter1)
        self.btn_sql_4.setObjectName(u"btn_sql_4")
        sizePolicy6.setHeightForWidth(self.btn_sql_4.sizePolicy().hasHeightForWidth())
        self.btn_sql_4.setSizePolicy(sizePolicy6)
        self.btn_sql_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql_4.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.btn_sql_4.setIcon(icon11)
        self.btn_sql_4.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.btn_sql_4, 0, 4, 1, 1)

        self.txt_initial_10 = QLineEdit(self.fm_parameter1)
        self.txt_initial_10.setObjectName(u"txt_initial_10")
        self.txt_initial_10.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_10, 0, 3, 1, 1)

        self.txt_initial_12 = QLineEdit(self.fm_parameter1)
        self.txt_initial_12.setObjectName(u"txt_initial_12")
        self.txt_initial_12.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_12, 2, 3, 1, 1)

        self.txt_initial_11 = QLineEdit(self.fm_parameter1)
        self.txt_initial_11.setObjectName(u"txt_initial_11")
        self.txt_initial_11.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_11, 2, 1, 1, 1)

        self.txt_initial_14 = QLineEdit(self.fm_parameter1)
        self.txt_initial_14.setObjectName(u"txt_initial_14")
        self.txt_initial_14.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_14, 4, 1, 1, 1)

        self.txt_initial_15 = QLineEdit(self.fm_parameter1)
        self.txt_initial_15.setObjectName(u"txt_initial_15")
        self.txt_initial_15.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_15, 4, 3, 1, 1)

        self.verticalSpacer_37 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_37, 13, 2, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_36, 11, 2, 1, 1)

        self.btn_sql_7 = QPushButton(self.fm_parameter1)
        self.btn_sql_7.setObjectName(u"btn_sql_7")
        sizePolicy6.setHeightForWidth(self.btn_sql_7.sizePolicy().hasHeightForWidth())
        self.btn_sql_7.setSizePolicy(sizePolicy6)
        self.btn_sql_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql_7.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.btn_sql_7.setIcon(icon11)
        self.btn_sql_7.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.btn_sql_7, 6, 4, 1, 1)

        self.btn_sql_5 = QPushButton(self.fm_parameter1)
        self.btn_sql_5.setObjectName(u"btn_sql_5")
        sizePolicy6.setHeightForWidth(self.btn_sql_5.sizePolicy().hasHeightForWidth())
        self.btn_sql_5.setSizePolicy(sizePolicy6)
        self.btn_sql_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql_5.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.btn_sql_5.setIcon(icon11)
        self.btn_sql_5.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.btn_sql_5, 2, 4, 1, 1)

        self.txt_initial_18 = QLineEdit(self.fm_parameter1)
        self.txt_initial_18.setObjectName(u"txt_initial_18")
        self.txt_initial_18.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_18, 12, 3, 1, 1)

        self.label_26 = QLabel(self.fm_parameter1)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMaximumSize(QSize(20, 16777215))
        self.label_26.setFont(font7)

        self.gridLayout_6.addWidget(self.label_26, 12, 2, 1, 1)

        self.txt_initial_7 = QLineEdit(self.fm_parameter1)
        self.txt_initial_7.setObjectName(u"txt_initial_7")
        self.txt_initial_7.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_7, 8, 1, 1, 1)

        self.label_21 = QLabel(self.fm_parameter1)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font7)

        self.gridLayout_6.addWidget(self.label_21, 8, 2, 1, 1)

        self.txt_initial_16 = QLineEdit(self.fm_parameter1)
        self.txt_initial_16.setObjectName(u"txt_initial_16")
        self.txt_initial_16.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_16, 8, 3, 1, 1)

        self.label_20 = QLabel(self.fm_parameter1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(80, 16777215))
        self.label_20.setFont(font6)

        self.gridLayout_6.addWidget(self.label_20, 10, 0, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_33, 7, 2, 1, 1)

        self.txt_initial_8 = QLineEdit(self.fm_parameter1)
        self.txt_initial_8.setObjectName(u"txt_initial_8")
        self.txt_initial_8.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_8, 10, 1, 1, 1)

        self.label_22 = QLabel(self.fm_parameter1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font7)

        self.gridLayout_6.addWidget(self.label_22, 10, 2, 1, 1)

        self.verticalSpacer_35 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_35, 1, 2, 1, 1)

        self.txt_initial_13 = QLineEdit(self.fm_parameter1)
        self.txt_initial_13.setObjectName(u"txt_initial_13")
        self.txt_initial_13.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_13, 10, 3, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_34, 9, 2, 1, 1)

        self.txt_initial_5 = QLineEdit(self.fm_parameter1)
        self.txt_initial_5.setObjectName(u"txt_initial_5")
        self.txt_initial_5.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_5, 6, 1, 1, 1)

        self.label_18 = QLabel(self.fm_parameter1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(80, 16777215))
        self.label_18.setFont(font6)

        self.gridLayout_6.addWidget(self.label_18, 6, 0, 1, 1)

        self.label_5 = QLabel(self.fm_parameter1)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QSize(20, 16777215))
        self.label_5.setFont(font7)

        self.gridLayout_6.addWidget(self.label_5, 6, 2, 1, 1)

        self.txt_initial_6 = QLineEdit(self.fm_parameter1)
        self.txt_initial_6.setObjectName(u"txt_initial_6")
        sizePolicy1.setHeightForWidth(self.txt_initial_6.sizePolicy().hasHeightForWidth())
        self.txt_initial_6.setSizePolicy(sizePolicy1)
        self.txt_initial_6.setMinimumSize(QSize(0, 0))
        self.txt_initial_6.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_6, 6, 3, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_32, 5, 2, 1, 1)

        self.label_19 = QLabel(self.fm_parameter1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(80, 16777215))
        self.label_19.setFont(font6)

        self.gridLayout_6.addWidget(self.label_19, 8, 0, 1, 1)

        self.txt_initial_17 = QLineEdit(self.fm_parameter1)
        self.txt_initial_17.setObjectName(u"txt_initial_17")
        self.txt_initial_17.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.txt_initial_17, 12, 1, 1, 1)

        self.label_23 = QLabel(self.fm_parameter1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(80, 16777215))
        self.label_23.setFont(font6)

        self.gridLayout_6.addWidget(self.label_23, 12, 0, 1, 1)

        self.btn_sql_6 = QPushButton(self.fm_parameter1)
        self.btn_sql_6.setObjectName(u"btn_sql_6")
        sizePolicy6.setHeightForWidth(self.btn_sql_6.sizePolicy().hasHeightForWidth())
        self.btn_sql_6.setSizePolicy(sizePolicy6)
        self.btn_sql_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql_6.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.btn_sql_6.setIcon(icon11)
        self.btn_sql_6.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.btn_sql_6, 4, 4, 1, 1)


        self.verticalLayout_9.addWidget(self.fm_parameter1)

        self.gb_parameter_2 = QGroupBox(self.gb_parameter)
        self.gb_parameter_2.setObjectName(u"gb_parameter_2")
        sizePolicy.setHeightForWidth(self.gb_parameter_2.sizePolicy().hasHeightForWidth())
        self.gb_parameter_2.setSizePolicy(sizePolicy)
        self.gb_parameter_2.setFont(font4)
        self.verticalLayout_13 = QVBoxLayout(self.gb_parameter_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer_14 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_14)

        self.fm_parameter1_2 = QFrame(self.gb_parameter_2)
        self.fm_parameter1_2.setObjectName(u"fm_parameter1_2")
        sizePolicy.setHeightForWidth(self.fm_parameter1_2.sizePolicy().hasHeightForWidth())
        self.fm_parameter1_2.setSizePolicy(sizePolicy)
        self.fm_parameter1_2.setMaximumSize(QSize(16777215, 16777215))
        self.fm_parameter1_2.setFrameShape(QFrame.StyledPanel)
        self.fm_parameter1_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.fm_parameter1_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.dateEdit_10 = QDateEdit(self.fm_parameter1_2)
        self.dateEdit_10.setObjectName(u"dateEdit_10")
        self.dateEdit_10.setFont(font1)
        self.dateEdit_10.setMinimumDate(QDate(2018, 9, 1))
        self.dateEdit_10.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateEdit_10.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.dateEdit_10, 1, 1, 1, 1)

        self.dateEdit_9 = QDateEdit(self.fm_parameter1_2)
        self.dateEdit_9.setObjectName(u"dateEdit_9")
        self.dateEdit_9.setFont(font1)
        self.dateEdit_9.setMinimumDate(QDate(2018, 9, 1))
        self.dateEdit_9.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateEdit_9.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.dateEdit_9, 0, 3, 1, 1)

        self.dateEdit_11 = QDateEdit(self.fm_parameter1_2)
        self.dateEdit_11.setObjectName(u"dateEdit_11")
        self.dateEdit_11.setFont(font1)
        self.dateEdit_11.setMinimumDate(QDate(2018, 9, 1))
        self.dateEdit_11.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateEdit_11.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.dateEdit_11, 1, 3, 1, 1)

        self.label_41 = QLabel(self.fm_parameter1_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(80, 16777215))
        self.label_41.setFont(font6)

        self.gridLayout_9.addWidget(self.label_41, 1, 0, 1, 1)

        self.label_42 = QLabel(self.fm_parameter1_2)
        self.label_42.setObjectName(u"label_42")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy8)
        self.label_42.setFont(font7)

        self.gridLayout_9.addWidget(self.label_42, 1, 2, 1, 1)

        self.label_48 = QLabel(self.fm_parameter1_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(100, 16777215))
        self.label_48.setFont(font6)

        self.gridLayout_9.addWidget(self.label_48, 0, 0, 1, 1)

        self.label_40 = QLabel(self.fm_parameter1_2)
        self.label_40.setObjectName(u"label_40")
        sizePolicy8.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy8)
        self.label_40.setFont(font7)

        self.gridLayout_9.addWidget(self.label_40, 0, 2, 1, 1)

        self.dateEdit_12 = QDateEdit(self.fm_parameter1_2)
        self.dateEdit_12.setObjectName(u"dateEdit_12")
        self.dateEdit_12.setFont(font1)
        self.dateEdit_12.setWrapping(False)
        self.dateEdit_12.setFrame(True)
        self.dateEdit_12.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit_12.setProperty("showGroupSeparator", False)
        self.dateEdit_12.setMinimumDate(QDate(2018, 9, 1))
        self.dateEdit_12.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateEdit_12.setCalendarPopup(True)
        self.dateEdit_12.setCurrentSectionIndex(0)

        self.gridLayout_9.addWidget(self.dateEdit_12, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.fm_parameter1_2)


        self.verticalLayout_9.addWidget(self.gb_parameter_2)


        self.verticalLayout_6.addWidget(self.gb_parameter)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 1))
        self.frame_12.setStyleSheet(u"background-color: rgb(189, 112, 255);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")

        self.verticalLayout_6.addWidget(self.frame_12)

        self.verticalSpacer_23 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_23)

        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 1))
        self.frame_14.setStyleSheet(u"background-color: rgb(189, 112, 255);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")

        self.verticalLayout_6.addWidget(self.frame_14)

        self.label_introduce = QLabel(self.frame_7)
        self.label_introduce.setObjectName(u"label_introduce")
        self.label_introduce.setMinimumSize(QSize(200, 30))
        self.label_introduce.setMaximumSize(QSize(16777215, 13))
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(False)
        font8.setItalic(True)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        font8.setStyleStrategy(QFont.PreferDefault)
        self.label_introduce.setFont(font8)
        self.label_introduce.setStyleSheet(u"color: rgb(7, 64, 128);")
        self.label_introduce.setTextFormat(Qt.AutoText)
        self.label_introduce.setScaledContents(False)
        self.label_introduce.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_introduce)

        self.verticalSpacer_24 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_24)

        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 1))
        self.frame_15.setStyleSheet(u"background-color: rgb(189, 112, 255);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")

        self.verticalLayout_6.addWidget(self.frame_15)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_4.addWidget(self.menu_parameter)

        self.side_container = QFrame(self.centralwidget)
        self.side_container.setObjectName(u"side_container")
        sizePolicy.setHeightForWidth(self.side_container.sizePolicy().hasHeightForWidth())
        self.side_container.setSizePolicy(sizePolicy)
        self.side_container.setMinimumSize(QSize(0, 0))
        self.side_container.setMaximumSize(QSize(16777215, 16777215))
        self.side_container.setStyleSheet(u"color: rgb(7, 64, 128);")
        self.side_container.setFrameShape(QFrame.StyledPanel)
        self.side_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.side_container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 1))
        self.frame_3.setStyleSheet(u"background-color: rgb(189, 112, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.side_container)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_login = QGroupBox(self.frame_4)
        self.gb_login.setObjectName(u"gb_login")
        sizePolicy.setHeightForWidth(self.gb_login.sizePolicy().hasHeightForWidth())
        self.gb_login.setSizePolicy(sizePolicy)
        self.gb_login.setFont(font4)
        self.verticalLayout_7 = QVBoxLayout(self.gb_login)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.act_sap = QRadioButton(self.gb_login)
        self.act_sap.setObjectName(u"act_sap")
        sizePolicy2.setHeightForWidth(self.act_sap.sizePolicy().hasHeightForWidth())
        self.act_sap.setSizePolicy(sizePolicy2)
        self.act_sap.setCheckable(True)
        self.act_sap.setChecked(True)

        self.horizontalLayout_15.addWidget(self.act_sap)

        self.act_mes = QRadioButton(self.gb_login)
        self.act_mes.setObjectName(u"act_mes")
        sizePolicy2.setHeightForWidth(self.act_mes.sizePolicy().hasHeightForWidth())
        self.act_mes.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.act_mes)

        self.act_oracle_db = QRadioButton(self.gb_login)
        self.act_oracle_db.setObjectName(u"act_oracle_db")
        self.act_oracle_db.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.act_oracle_db.sizePolicy().hasHeightForWidth())
        self.act_oracle_db.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.act_oracle_db)

        self.act_gw = QRadioButton(self.gb_login)
        self.act_gw.setObjectName(u"act_gw")
        self.act_gw.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.act_gw.sizePolicy().hasHeightForWidth())
        self.act_gw.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.act_gw)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_17 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_17)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_sid = QLabel(self.gb_login)
        self.lb_sid.setObjectName(u"lb_sid")
        sizePolicy3.setHeightForWidth(self.lb_sid.sizePolicy().hasHeightForWidth())
        self.lb_sid.setSizePolicy(sizePolicy3)
        self.lb_sid.setMinimumSize(QSize(0, 30))
        self.lb_sid.setFont(font3)

        self.horizontalLayout_5.addWidget(self.lb_sid)

        self.cbx_sid = QComboBox(self.gb_login)
        self.cbx_sid.addItem("")
        self.cbx_sid.addItem("")
        self.cbx_sid.addItem("")
        self.cbx_sid.setObjectName(u"cbx_sid")
        sizePolicy3.setHeightForWidth(self.cbx_sid.sizePolicy().hasHeightForWidth())
        self.cbx_sid.setSizePolicy(sizePolicy3)
        self.cbx_sid.setMinimumSize(QSize(70, 0))
        self.cbx_sid.setSizeIncrement(QSize(0, 30))
        self.cbx_sid.setFont(font1)

        self.horizontalLayout_5.addWidget(self.cbx_sid)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.lb_clt = QLabel(self.gb_login)
        self.lb_clt.setObjectName(u"lb_clt")
        sizePolicy3.setHeightForWidth(self.lb_clt.sizePolicy().hasHeightForWidth())
        self.lb_clt.setSizePolicy(sizePolicy3)
        self.lb_clt.setMinimumSize(QSize(0, 30))
        self.lb_clt.setFont(font3)

        self.horizontalLayout_5.addWidget(self.lb_clt)

        self.cbx_client = QComboBox(self.gb_login)
        self.cbx_client.addItem("")
        self.cbx_client.addItem("")
        self.cbx_client.addItem("")
        self.cbx_client.addItem("")
        self.cbx_client.setObjectName(u"cbx_client")
        sizePolicy3.setHeightForWidth(self.cbx_client.sizePolicy().hasHeightForWidth())
        self.cbx_client.setSizePolicy(sizePolicy3)
        self.cbx_client.setMinimumSize(QSize(70, 0))
        self.cbx_client.setSizeIncrement(QSize(0, 30))
        self.cbx_client.setFont(font1)

        self.horizontalLayout_5.addWidget(self.cbx_client)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_7 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_usr = QLabel(self.gb_login)
        self.lb_usr.setObjectName(u"lb_usr")
        sizePolicy2.setHeightForWidth(self.lb_usr.sizePolicy().hasHeightForWidth())
        self.lb_usr.setSizePolicy(sizePolicy2)
        self.lb_usr.setMinimumSize(QSize(0, 0))
        self.lb_usr.setFont(font3)

        self.horizontalLayout_6.addWidget(self.lb_usr)

        self.txt_usr = QLineEdit(self.gb_login)
        self.txt_usr.setObjectName(u"txt_usr")
        sizePolicy2.setHeightForWidth(self.txt_usr.sizePolicy().hasHeightForWidth())
        self.txt_usr.setSizePolicy(sizePolicy2)
        self.txt_usr.setMinimumSize(QSize(0, 0))
        self.txt_usr.setFont(font1)
        self.txt_usr.setMaxLength(30)

        self.horizontalLayout_6.addWidget(self.txt_usr)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_15 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_15)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_pw = QLabel(self.gb_login)
        self.lb_pw.setObjectName(u"lb_pw")
        sizePolicy2.setHeightForWidth(self.lb_pw.sizePolicy().hasHeightForWidth())
        self.lb_pw.setSizePolicy(sizePolicy2)
        self.lb_pw.setMinimumSize(QSize(0, 0))
        self.lb_pw.setSizeIncrement(QSize(0, 0))
        self.lb_pw.setFont(font3)

        self.horizontalLayout_7.addWidget(self.lb_pw)

        self.txt_pw = QLineEdit(self.gb_login)
        self.txt_pw.setObjectName(u"txt_pw")
        self.txt_pw.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.txt_pw.sizePolicy().hasHeightForWidth())
        self.txt_pw.setSizePolicy(sizePolicy2)
        self.txt_pw.setMinimumSize(QSize(0, 0))
        self.txt_pw.setFont(font1)
        self.txt_pw.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_pw)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_9 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cbox_saveinfo = QCheckBox(self.gb_login)
        self.cbox_saveinfo.setObjectName(u"cbox_saveinfo")
        sizePolicy2.setHeightForWidth(self.cbox_saveinfo.sizePolicy().hasHeightForWidth())
        self.cbox_saveinfo.setSizePolicy(sizePolicy2)
        self.cbox_saveinfo.setFont(font1)
        self.cbox_saveinfo.setChecked(True)

        self.horizontalLayout_8.addWidget(self.cbox_saveinfo)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.btn_login = QPushButton(self.gb_login)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy2.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy2)
        self.btn_login.setMinimumSize(QSize(0, 0))
        self.btn_login.setFont(font4)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	color: rgb(85, 0, 127);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(159,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_login)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.frame_5 = QFrame(self.gb_login)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 1))
        self.frame_5.setStyleSheet(u"background-color: rgb(189, 112, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")

        self.verticalLayout_7.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.gb_login)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_usr_2 = QLabel(self.frame_4)
        self.lb_usr_2.setObjectName(u"lb_usr_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.lb_usr_2.sizePolicy().hasHeightForWidth())
        self.lb_usr_2.setSizePolicy(sizePolicy9)
        self.lb_usr_2.setMinimumSize(QSize(0, 0))
        self.lb_usr_2.setMaximumSize(QSize(60, 30))
        self.lb_usr_2.setFont(font7)

        self.horizontalLayout_12.addWidget(self.lb_usr_2)

        self.txt_usr_2 = QLineEdit(self.frame_4)
        self.txt_usr_2.setObjectName(u"txt_usr_2")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.txt_usr_2.sizePolicy().hasHeightForWidth())
        self.txt_usr_2.setSizePolicy(sizePolicy10)
        self.txt_usr_2.setMinimumSize(QSize(200, 0))
        self.txt_usr_2.setMaximumSize(QSize(16777215, 30))
        self.txt_usr_2.setFont(font1)
        self.txt_usr_2.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.txt_usr_2.setMaxLength(1000000)
        self.txt_usr_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_12.addWidget(self.txt_usr_2)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.groupBox_rpa_configure = QGroupBox(self.frame_4)
        self.groupBox_rpa_configure.setObjectName(u"groupBox_rpa_configure")
        sizePolicy.setHeightForWidth(self.groupBox_rpa_configure.sizePolicy().hasHeightForWidth())
        self.groupBox_rpa_configure.setSizePolicy(sizePolicy)
        self.groupBox_rpa_configure.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_rpa_configure.setFont(font4)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_rpa_configure)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_16)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_22 = QSpacerItem(10, 2, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_22)

        self.lb_usr_3 = QLabel(self.groupBox_rpa_configure)
        self.lb_usr_3.setObjectName(u"lb_usr_3")
        sizePolicy9.setHeightForWidth(self.lb_usr_3.sizePolicy().hasHeightForWidth())
        self.lb_usr_3.setSizePolicy(sizePolicy9)
        self.lb_usr_3.setMinimumSize(QSize(0, 0))
        self.lb_usr_3.setMaximumSize(QSize(1000, 30))
        self.lb_usr_3.setFont(font7)

        self.horizontalLayout_20.addWidget(self.lb_usr_3)

        self.horizontalSpacer_13 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)

        self.checkBox = QCheckBox(self.groupBox_rpa_configure)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy7.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy7)
        self.checkBox.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox.setStyleSheet(u"QCheckBox::indicator{\n"
"	width: 50px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image:url(IMG/on.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"	image:url(IMG/off.png);\n"
"}")
        self.checkBox.setChecked(False)

        self.horizontalLayout_20.addWidget(self.checkBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_20 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_20)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_24 = QSpacerItem(10, 2, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_24)

        self.lb_usr_5 = QLabel(self.groupBox_rpa_configure)
        self.lb_usr_5.setObjectName(u"lb_usr_5")
        sizePolicy9.setHeightForWidth(self.lb_usr_5.sizePolicy().hasHeightForWidth())
        self.lb_usr_5.setSizePolicy(sizePolicy9)
        self.lb_usr_5.setMinimumSize(QSize(0, 0))
        self.lb_usr_5.setMaximumSize(QSize(1000, 30))
        self.lb_usr_5.setFont(font7)

        self.horizontalLayout_23.addWidget(self.lb_usr_5)

        self.horizontalSpacer_15 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_15)

        self.checkBox_3 = QCheckBox(self.groupBox_rpa_configure)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy7)
        self.checkBox_3.setStyleSheet(u"QCheckBox::indicator{\n"
"	width: 50px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image:url(IMG/on.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"	image:url(IMG/off.png);\n"
"}")
        self.checkBox_3.setChecked(True)

        self.horizontalLayout_23.addWidget(self.checkBox_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_46 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_46)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_26 = QSpacerItem(10, 2, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_26)

        self.lb_usr_6 = QLabel(self.groupBox_rpa_configure)
        self.lb_usr_6.setObjectName(u"lb_usr_6")
        sizePolicy9.setHeightForWidth(self.lb_usr_6.sizePolicy().hasHeightForWidth())
        self.lb_usr_6.setSizePolicy(sizePolicy9)
        self.lb_usr_6.setMinimumSize(QSize(0, 0))
        self.lb_usr_6.setMaximumSize(QSize(1000, 30))
        self.lb_usr_6.setFont(font7)

        self.horizontalLayout_24.addWidget(self.lb_usr_6)

        self.horizontalSpacer_16 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_16)

        self.checkBox_4 = QCheckBox(self.groupBox_rpa_configure)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy7)
        self.checkBox_4.setStyleSheet(u"QCheckBox::indicator{\n"
"	width: 50px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image:url(IMG/on.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"	image:url(IMG/off.png);\n"
"}")
        self.checkBox_4.setChecked(True)

        self.horizontalLayout_24.addWidget(self.checkBox_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_47 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_47)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_25 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_25)

        self.lb_usr_7 = QLabel(self.groupBox_rpa_configure)
        self.lb_usr_7.setObjectName(u"lb_usr_7")
        sizePolicy9.setHeightForWidth(self.lb_usr_7.sizePolicy().hasHeightForWidth())
        self.lb_usr_7.setSizePolicy(sizePolicy9)
        self.lb_usr_7.setMinimumSize(QSize(0, 0))
        self.lb_usr_7.setMaximumSize(QSize(1000, 30))
        self.lb_usr_7.setFont(font7)

        self.horizontalLayout_25.addWidget(self.lb_usr_7)

        self.horizontalSpacer_17 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_17)

        self.checkBox_5 = QCheckBox(self.groupBox_rpa_configure)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy7.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy7)
        self.checkBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_5.setStyleSheet(u"QCheckBox::indicator{\n"
"	width: 50px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image:url(IMG/on.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"	image:url(IMG/off.png);\n"
"}")
        self.checkBox_5.setChecked(True)

        self.horizontalLayout_25.addWidget(self.checkBox_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_5 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)


        self.verticalLayout.addWidget(self.groupBox_rpa_configure)

        self.verticalSpacer_29 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_29)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 1))
        self.frame_8.setStyleSheet(u"background-color: rgb(189, 112, 255);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.verticalLayout.addWidget(self.frame_8)

        self.groupBox_rpa_configure_2 = QGroupBox(self.frame_4)
        self.groupBox_rpa_configure_2.setObjectName(u"groupBox_rpa_configure_2")
        sizePolicy.setHeightForWidth(self.groupBox_rpa_configure_2.sizePolicy().hasHeightForWidth())
        self.groupBox_rpa_configure_2.setSizePolicy(sizePolicy)
        self.groupBox_rpa_configure_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_rpa_configure_2.setFont(font4)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_rpa_configure_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cbx_transaction_2 = QComboBox(self.groupBox_rpa_configure_2)
        icon12 = QIcon()
        icon12.addFile(u":/icons/dist/IMG/email.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbx_transaction_2.addItem(icon12, "")
        self.cbx_transaction_2.setObjectName(u"cbx_transaction_2")
        self.cbx_transaction_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cbx_transaction_2.sizePolicy().hasHeightForWidth())
        self.cbx_transaction_2.setSizePolicy(sizePolicy)
        self.cbx_transaction_2.setMinimumSize(QSize(0, 20))
        self.cbx_transaction_2.setMaximumSize(QSize(16777215, 30))
        self.cbx_transaction_2.setSizeIncrement(QSize(0, 0))
        self.cbx_transaction_2.setFont(font1)
        self.cbx_transaction_2.setAutoFillBackground(False)
        self.cbx_transaction_2.setEditable(True)
        self.cbx_transaction_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cbx_transaction_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_10.addWidget(self.cbx_transaction_2)

        self.btn_sql_3 = QPushButton(self.groupBox_rpa_configure_2)
        self.btn_sql_3.setObjectName(u"btn_sql_3")
        sizePolicy6.setHeightForWidth(self.btn_sql_3.sizePolicy().hasHeightForWidth())
        self.btn_sql_3.setSizePolicy(sizePolicy6)
        self.btn_sql_3.setMaximumSize(QSize(20, 20))
        self.btn_sql_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sql_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(7, 64, 128);\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.btn_sql_3.setIcon(icon10)
        self.btn_sql_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.btn_sql_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_18 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_18)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")

        self.verticalLayout_12.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_ledger = QPushButton(self.groupBox_rpa_configure_2)
        self.btn_ledger.setObjectName(u"btn_ledger")
        self.btn_ledger.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ledger.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/dist/IMG/ledger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ledger.setIcon(icon13)
        self.btn_ledger.setIconSize(QSize(20, 20))

        self.horizontalLayout_21.addWidget(self.btn_ledger)

        self.btn_excel = QPushButton(self.groupBox_rpa_configure_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        self.btn_excel.setIcon(icon5)
        self.btn_excel.setIconSize(QSize(20, 20))

        self.horizontalLayout_21.addWidget(self.btn_excel)

        self.btn_email = QPushButton(self.groupBox_rpa_configure_2)
        self.btn_email.setObjectName(u"btn_email")
        self.btn_email.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_email.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/dist/IMG/mail.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_email.setIcon(icon14)
        self.btn_email.setIconSize(QSize(20, 20))

        self.horizontalLayout_21.addWidget(self.btn_email)


        self.verticalLayout_12.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_19 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_19)


        self.verticalLayout.addWidget(self.groupBox_rpa_configure_2)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 3))
        self.frame_10.setStyleSheet(u"background-color: rgb(189, 112, 255);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")

        self.verticalLayout.addWidget(self.frame_10)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_reset_data = QPushButton(self.frame_4)
        self.btn_reset_data.setObjectName(u"btn_reset_data")
        self.btn_reset_data.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"	border-radius:  15px;\n"
"\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_reset_data)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_12)

        self.btn_close_sap = QPushButton(self.frame_4)
        self.btn_close_sap.setObjectName(u"btn_close_sap")
        self.btn_close_sap.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius:  15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(238,238,238);\n"
"	color: rgb(47,47,47);\n"
"	border-radius:  15px;\n"
"\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/Button/dist/IMG/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_sap.setIcon(icon15)

        self.horizontalLayout_17.addWidget(self.btn_close_sap)


        self.verticalLayout.addLayout(self.horizontalLayout_17)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout_4.addWidget(self.side_container)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\"font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/dist/IMG/Aluko_Group.png\" width=\"100\" height=\"70\" /></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#55007f;\">ALUKO ROBOTIC PROCESS AUTOMATION</span></p></body></html>", None))
        self.cbx_ribbon.setText(QCoreApplication.translate("MainWindow", u"Ribbon", None))
        self.cbx_parameter.setText(QCoreApplication.translate("MainWindow", u"Parameter", None))
        self.btn_sql.setText("")
        self.btn_update.setText("")
        self.btn_toggle.setText("")
        self.label_transaction.setText(QCoreApplication.translate("MainWindow", u"Transaction*", None))
        self.cbx_transaction.setItemText(0, QCoreApplication.translate("MainWindow", u"Material Master Data", None))
        self.cbx_transaction.setItemText(1, QCoreApplication.translate("MainWindow", u"Purchase Info Record", None))
        self.cbx_transaction.setItemText(2, QCoreApplication.translate("MainWindow", u"Direct Delivery", None))
        self.cbx_transaction.setItemText(3, QCoreApplication.translate("MainWindow", u"Business Partner", None))
        self.cbx_transaction.setItemText(4, QCoreApplication.translate("MainWindow", u"Good Receipt from Vendor", None))
        self.cbx_transaction.setItemText(5, QCoreApplication.translate("MainWindow", u"Interface Table", None))

        self.act_Create.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.act_Change.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.act_Delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_action.setText(QCoreApplication.translate("MainWindow", u"Action*", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"  Chosse Excel File ....", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Thread:", None))
        self.cbx_client_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.cbx_client_3.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.cbx_client_3.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.cbx_client_3.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.cbx_client_3.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.cbx_client_3.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.cbx_client_3.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.cbx_client_3.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.cbx_client_3.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.cbx_client_3.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start   ", None))
        self.btn_pause.setText(QCoreApplication.translate("MainWindow", u"Pause   ", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Stop   ", None))
        self.btn_slq_get.setText(QCoreApplication.translate("MainWindow", u"SQL Querry:", None))
        self.cbx_inteface.setItemText(0, "")
        self.cbx_inteface.setItemText(1, QCoreApplication.translate("MainWindow", u"IF0021", None))
        self.cbx_inteface.setItemText(2, QCoreApplication.translate("MainWindow", u"IF0023", None))

        self.btn_sql_2.setText("")
        self.txt_sql_querry.setText(QCoreApplication.translate("MainWindow", u"SELECT * FROM IINVDLVRCV WHERE BWART = 'F21' ORDER BY zsequen DESC", None))
        self.txt_msg.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2022-2030 PI Team - Aluko Viet Nam. All Rights Reserved.", None))
        self.gb_parameter.setTitle(QCoreApplication.translate("MainWindow", u"Selection Option", None))
        self.btn_sql_10.setText("")
        self.btn_sql_9.setText("")
        self.btn_sql_8.setText("")
        self.para_1.setText(QCoreApplication.translate("MainWindow", u"Company:", None))
        self.para2.setText(QCoreApplication.translate("MainWindow", u"Plant:", None))
        self.txt_initial_9.setText("")
        self.to_1.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.para3.setText(QCoreApplication.translate("MainWindow", u"S.Location:", None))
        self.to_3.setText(QCoreApplication.translate("MainWindow", u"to ", None))
        self.to_2.setText(QCoreApplication.translate("MainWindow", u"to ", None))
        self.btn_sql_4.setText("")
        self.txt_initial_10.setText("")
        self.txt_initial_12.setText("")
        self.txt_initial_11.setText("")
        self.txt_initial_14.setText("")
        self.txt_initial_15.setText("")
        self.btn_sql_7.setText("")
        self.btn_sql_5.setText("")
        self.txt_initial_18.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.txt_initial_7.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"to ", None))
        self.txt_initial_16.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Material:", None))
        self.txt_initial_8.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"to ", None))
        self.txt_initial_13.setText("")
        self.txt_initial_5.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"PO Number:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.txt_initial_6.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Inbound:", None))
        self.txt_initial_17.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Interface:", None))
        self.btn_sql_6.setText("")
        self.gb_parameter_2.setTitle(QCoreApplication.translate("MainWindow", u"Time Option", None))
        self.dateEdit_10.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy.MM.dd", None))
        self.dateEdit_9.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy.MM.dd", None))
        self.dateEdit_11.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy.MM.dd", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Entry Date", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"to ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"to ", None))
        self.dateEdit_12.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy.MM.dd", None))
        self.label_introduce.setText(QCoreApplication.translate("MainWindow", u"If you have any question or new request, please ask me know via: sic@aluko.com", None))
        self.gb_login.setTitle(QCoreApplication.translate("MainWindow", u"Login Infomation", None))
        self.act_sap.setText(QCoreApplication.translate("MainWindow", u"SAP", None))
        self.act_mes.setText(QCoreApplication.translate("MainWindow", u"MES", None))
        self.act_oracle_db.setText(QCoreApplication.translate("MainWindow", u"ODB", None))
        self.act_gw.setText(QCoreApplication.translate("MainWindow", u"Groupware", None))
        self.lb_sid.setText(QCoreApplication.translate("MainWindow", u"SID: ", None))
        self.cbx_sid.setItemText(0, QCoreApplication.translate("MainWindow", u"PSA", None))
        self.cbx_sid.setItemText(1, QCoreApplication.translate("MainWindow", u"QAS", None))
        self.cbx_sid.setItemText(2, QCoreApplication.translate("MainWindow", u"DEV", None))

        self.lb_clt.setText(QCoreApplication.translate("MainWindow", u"Client:", None))
        self.cbx_client.setItemText(0, QCoreApplication.translate("MainWindow", u"100", None))
        self.cbx_client.setItemText(1, QCoreApplication.translate("MainWindow", u"200", None))
        self.cbx_client.setItemText(2, QCoreApplication.translate("MainWindow", u"300", None))
        self.cbx_client.setItemText(3, QCoreApplication.translate("MainWindow", u"500", None))

        self.lb_usr.setText(QCoreApplication.translate("MainWindow", u"User Name:", None))
        self.txt_usr.setText(QCoreApplication.translate("MainWindow", u"AMMP35", None))
        self.lb_pw.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.txt_pw.setText(QCoreApplication.translate("MainWindow", u"ALT147852369", None))
        self.cbox_saveinfo.setText(QCoreApplication.translate("MainWindow", u"Saved", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.lb_usr_2.setText(QCoreApplication.translate("MainWindow", u"Token:", None))
        self.txt_usr_2.setText(QCoreApplication.translate("MainWindow", u"5616553456:AAEco-vBsBwYgDNi_H-l8PD9P59oK_yAfQk'", None))
        self.groupBox_rpa_configure.setTitle(QCoreApplication.translate("MainWindow", u"Function", None))
        self.lb_usr_3.setText(QCoreApplication.translate("MainWindow", u"AI ChatBot Enable", None))
        self.checkBox.setText("")
        self.lb_usr_5.setText(QCoreApplication.translate("MainWindow", u"Automatic Connect SAP", None))
        self.checkBox_3.setText("")
        self.lb_usr_6.setText(QCoreApplication.translate("MainWindow", u"Automatic Connect MESDB", None))
        self.checkBox_4.setText("")
        self.lb_usr_7.setText(QCoreApplication.translate("MainWindow", u"Automatic Export to Excel", None))
        self.checkBox_5.setText("")
        self.groupBox_rpa_configure_2.setTitle(QCoreApplication.translate("MainWindow", u"Mail To", None))
        self.cbx_transaction_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Tu.Nguyen.Anh@aluko.com", None))

        self.btn_sql_3.setText("")
        self.btn_ledger.setText(QCoreApplication.translate("MainWindow", u" Ledger", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.btn_email.setText(QCoreApplication.translate("MainWindow", u" Email", None))
#if QT_CONFIG(shortcut)
        self.btn_email.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_reset_data.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_close_sap.setText(QCoreApplication.translate("MainWindow", u"Close SAP", None))
    # retranslateUi

