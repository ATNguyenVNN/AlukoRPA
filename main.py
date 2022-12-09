# -Begin-----------------------------------------------------------------
# Main App ALUKO RPA 2022.11.01
# -Includes--------------------------------------------------------------
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtCore
from ui_main import Ui_MainWindow
import sys
import os
import pandas as pd
from func_sap import SapGui
from func_sql import MES_DB
from datetime import time, datetime
# -SUB Main--------------------------------------------------------------
# Class Table Widget

class MainWindow(QMainWindow, Ui_MainWindow, QTableWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # TuNA_221121 Set GUI in center the screen.
        centerPoint = QGuiApplication.screens()[0].geometry().center()
        self.move(centerPoint - self.frameGeometry().center())
        # TuNA_22112 Set Windows Title.
        self.setWindowTitle('Aluko RPA V0.0.2 20221208')
        # TuNA_221207 Set Table Widget in GUI Screen
        # TuNA_221121 End Set GUI in center the screen.

        self.sap = SapGui()
        # SYSTEM PAGES
        # LOGIN INTO SAP SYSTEM
        self.btn_login.clicked.connect(self.fnc_login)
        # OPEN FILE BUTTON
        self.btn_open.clicked.connect(self.open_file)
        # CREATE
        self.btn_start.clicked.connect(self.fnc_button_create)
        # CHANGE
        self.btn_pause.clicked.connect(self.fnc_button_change)
        # STOP
        self.btn_stop.clicked.connect(self.fnc_button_stop)
        # TOGGLE BUTTON.
        self.btn_toggle.clicked.connect(self.right_menu)
        # RIBBON BUTTON.
        self.cbx_ribbon.clicked.connect(self.ribbon_menu)
        # PARAMETER BUTTON
        self.btn_parameter.clicked.connect(self.parameter_menu)
        # SQL BUTTON.
        self.btn_sql.clicked.connect(self.sql_frame)
        # ToExcel BUTTON
        self.btn_excel.clicked.connect(self.exportToExcel)
        # Close System
        self.btn_close_sap.clicked.connect(self.fnc_close_system)
        # Table Widget Setup

    # TuNA 221117 _ Update logic for right menu.

    def right_menu(self):
        self.label_2.setText("")
        width = self.side_container.width()
        if width == 0:
            newWidth = 400
            self.label_2.setText("")
        else:
            newWidth = 0
            self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#55007f;\">ALUKO ROBOTIC PROCESS AUTOMATION</span></p></body></html>", None))
        self.animation = QtCore.QPropertyAnimation(
            self.side_container, b'maximumWidth')
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    # TuNA 221117_ End Update logic for right menu.

    # TuNA 221117 _ Update logic for parameter menu.

    def parameter_menu(self):
        
        width = self.menu_parameter.width()
        if width == 0:
            newWidth = 350
            self.label_2.setText("")
        else:
            newWidth = 0
            self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#55007f;\">ALUKO ROBOTIC PROCESS AUTOMATION</span></p></body></html>", None))
        self.animation = QtCore.QPropertyAnimation(
            self.menu_parameter, b'maximumWidth')
        self.animation.setDuration(320)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    # TuNA 221117_ End Update logic for parameter menu.

    # TuNA 221117 _ Update logic for ribbon menu.
    def ribbon_menu(self):
        height = self.bottom_frame.height()
        if height == 0:
            newHeight = 180
        else:
            newHeight = 0
        # changing style sheet code of check box
        # adding skin to checked indicator
        self.animation = QtCore.QPropertyAnimation(
            self.bottom_frame, b'maximumHeight')
        self.animation.setDuration(100)
        self.animation.setStartValue(height)
        self.animation.setEndValue(newHeight)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    # TuNA 221117_ End Update logic for ribbon menu.

    # TuNA 221117 _ Update logic for ribbon menu.

    def sql_frame(self):
        self.act_oracle_db.setChecked(True)
        height = self.frame_sql.height()
        self.cbx_transaction.setCurrentText("Interface Table")
        if height == 0:
            newHeight = 100
        else:
            newHeight = 0
        self.animation = QtCore.QPropertyAnimation(
            self.frame_sql, b'maximumHeight')
        self.animation.setDuration(2)
        self.animation.setStartValue(height)
        self.animation.setEndValue(newHeight)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # TuNA 221117_ End Update logic for ribbon menu.

    # Trả kết quả ra thanh trạng thái
    def fnc_notice(self, msg):
        print(msg)
        self.txt_msg.setText(msg)

    # TuNA 221118_ Add MessageBox.
    def fnc_msg_box(self, msg):
        box_msg = QMessageBox()
        box_msg.setWindowTitle('Aluko RPA Message.')
        icon = QIcon()
        icon.addFile(u":/icons/dist/IMG/aluko_logo.ico",
                     QSize(), QIcon.Normal, QIcon.On)
        box_msg.setWindowIcon(icon)
        box_msg.setText(msg)
        box_msg.exec()
    # TuNA 221118_ End Add MessageBox

    def fnc_button_create(self):
        if self.cbx_transaction.currentText() == "Material Master Data" and self.act_Create.isChecked() == True:
            if self.sap.sapConnect() == 'Connection successful.':
                MDM_CREATE = self.sap.sapCreateMaterial(str(self.file[0]))
                print(MDM_CREATE)
                self.load_excel(str(MDM_CREATE))
            else:
                self.fnc_notice(self.sap.sapConnect())

        elif self.cbx_transaction.currentText() == "Purchase Info Record" and self.act_Create.isChecked() == True:
            if self.sap.sapConnect() == 'Connection successful.':
                PIR_CREATE = self.sap.sapCreatePIR(str(self.file[0]))
                print(PIR_CREATE[0])
                self.load_excel(PIR_CREATE[0])

        elif self.cbx_transaction.currentText() == "Interface Table" and self.txt_sql_querry.text() != "":
            self.fnc_get_db()

    def fnc_button_change(self):
        if self.cbx_transaction.currentText() == "Purchase Info Record":
            self.txt_msg.setText(self.sap.sapChangePIR(str(self.file[0])))
        # Change Business Partner
        if self.cbx_transaction.currentText() == "Business Partner":
            self.txt_msg.setText(self.sap.sapChangeBP(str(self.file[0])))

    def fnc_button_stop(self):
        return 'New features are developing...'

    # TuNA 20221123_ Start Load data from MESDB.
    def fnc_get_db(self):
        self.tb_ledger.clear()
        try:
            self.db = MES_DB()
            if self.cbx_sid.currentText() == "PSA":
                ip = "113.160.134.244"
            elif self.cbx_sid.currentText() == "DEV":
                ip = '113.160.161.188'
            self.db.DB_connect(ip, "1521")
        except Exception as err:
            self.fnc_notice(str(err))
            # sys.exit(1);  Automatic close application.
        db_querry = self.txt_sql_querry.text().replace("\n", " ")
        new_querry = db_querry.replace("     ", " ")
        self.txt_sql_querry.setText(new_querry)
        print(new_querry)
        self.load_df(self.db.DB_query(new_querry))
        if self.checkBox_5.isChecked() == True:
            self.db.DB_export()

    # TuNA _ End Load data from MESDB.

    def fnc_login(self):
        # Truyền dữ liệu đăng nhập SAP.
        if self.act_sap.isChecked() == True:
            # Trả kết quả ra ngoài màn hình.
            self.fnc_notice(str(self.sap.sapLogin(self.cbx_sid.currentText(
            ), self.cbx_client.currentText(), self.txt_usr.text(), self.txt_pw.text())))
            # Save Login infomation
            self.saveinfo()

    def fnc_close_system(self):
        self.fnc_notice(str(self.sap.sapLogout()))

    def saveinfo(self):
        file_usr = open(r'user.txt', 'w')
        info = [self.cbx_sid.currentText(),
                self.cbx_client.currentText(),
                self.txt_usr.text(),
                self.txt_pw.text()
                ]
        file_usr.write(str(info))

    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Select spreadsheet.")
        self.load_excel(str(self.file[0]))

    def load_excel(self, ex_path):
        self.tb_ledger.clear()
        # TuNA 20221118_ Start Show Excel to QTable Widget.
        if self.cbx_transaction.currentText() == "Material Master Data":
            df = pd.read_excel(ex_path, na_filter="",
                               skiprows=[1, 2, 3]).astype(str)
        else:
            df = pd.read_excel(ex_path, na_filter="").astype(str)
        if df.size == 0:
            return
        self.tb_ledger.setRowCount(df.shape[0])
        self.tb_ledger.setColumnCount(df.shape[1])
        header = self.tb_ledger.setHorizontalHeaderLabels(df.columns)
        # Returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tb_ledger.setItem(row[0], col_index, tableItem)

        # Set StyleSheet for QTable
        self.tb_ledger.resizeColumnsToContents()
        self.tb_ledger.setStyleSheet(u"QHeaderView::section{\n"
                                     "			font: 75 8pt;\n"
                                     "            border-top:0px solid #D8D8D8;\n"
                                     "            border-left:0px solid #D8D8D8;\n"
                                     "            border-right:1px solid #D8D8D8;\n"
                                     "            border-bottom: 2px solid #D8D8D8;\n"
                                     "            background-color:white;\n"
                                     "            padding:4px;\n"
                                     "        }\n")
        self.fnc_notice(ex_path)

        # TuNA 20221118_ End Show Dataframe to QTable Widget.

    def load_df(self, df):
        self.tb_ledger.clear()
        self.tb_ledger.setRowCount(df.shape[0])
        self.tb_ledger.setColumnCount(df.shape[1])
        header = self.tb_ledger.setHorizontalHeaderLabels(df.columns)
        # Returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tb_ledger.setItem(row[0], col_index, tableItem)

        # Set StyleSheet for QTable
        self.tb_ledger.resizeColumnsToContents()
        self.tb_ledger.setStyleSheet(u"QHeaderView::section{\n"
                                     "			font: 75 8pt;\n"
                                     "            border-top:0px solid #D8D8D8;\n"
                                     "            border-left:0px solid #D8D8D8;\n"
                                     "            border-right:1px solid #D8D8D8;\n"
                                     "            border-bottom: 2px solid #D8D8D8;\n"
                                     "            background-color:white;\n"
                                     "            padding:4px;\n"
                                     "        }\n")
        self.fnc_notice("Completed....")
    # TuNA 20221118_ End Load DF to QTable Widget.

    # TuNA 20221207_ Export Dataframe to Excel
    def exportToExcel(self):
        self.columnHeaders = []
        # create column header list
        for j in range(self.tb_ledger.model().columnCount()):
            self.columnHeaders.append(
                self.tb_ledger.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=self.columnHeaders)

        # create dataframe object recordset
        for row in range(self.tb_ledger.rowCount()):
            for col in range(self.tb_ledger.columnCount()):
                df.at[row, self.columnHeaders[col]
                      ] = self.tb_ledger.item(row, col).text()
                dt = datetime.now()
                file_name = '\ALK_Export' + '_' + \
                    str(self.cbx_transaction.currentText())+'_' + \
                    dt.strftime('%Y%m%d-%H%M%S') + '.xlsx'
                path = os.getcwd()+file_name
        df.to_excel(path, index=False)
        self.fnc_notice(path)


# -Main------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# #-End-------------------------------------------------------------------
