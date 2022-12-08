# -Begin-----------------------------------------------------------------
    # Main App MES RPA in ALUKO Project.
# -Includes--------------------------------------------------------------
from PySide2.QtWidgets import (QApplication, QMainWindow, QFileDialog)
from  ui_mes import Ui_MainWindow
import sys
#from sql import MES_DB
# -SUB Main--------------------------------------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('MES RPA V0.1 20220921')
        # SYSTEM PAGES
        # self.btn_sap_pir.clicked.connect(
        #     lambda: self.Pages.setCurrentWidget(self.pg_sap))
        # self.btn_back.clicked.connect(
        #     lambda: self.Pages.setCurrentWidget(self.pg_home))
        # LOGIN INTO SAP SYSTEM
        self.btn_login.clicked.connect(self.fnc_login)
        # OPEN FILE BUTTON
        self.btn_open.clicked.connect(self.open_file)
        # CREATE
        self.btn_create.clicked.connect(self.fnc_button_create)
        # CHANGE
        self.btn_change.clicked.connect(self.fnc_button_change)

    # Trả kết quả ra thanh trạng thái
    def fnc_notice(self,msg):
        self.txt_file.setText(msg)
        
    def fnc_button_create(self):
        if self.cbx_transaction.currentText() == "GR_MM_101":
            self.MDM_CREATE = MES_DB.sapCreateMaterial(str(self.file[0]))
            self.fnc_notice(' Xuất file thành công.')

    def fnc_button_change(self):
        if self.cbx_transaction.currentText() == "Purchase Info Record":
            self.txt_file.setText(MES_DB.sapChangePIR(str(self.file[0])))
        # Change Business Partner
        if self.cbx_transaction.currentText() == "Business Partner":
            self.txt_file.setText(MES_DB.sapChangeBP(str(self.file[0])))

    def fnc_login(self):
        # Truyền dữ liệu đăng nhập SAP.
        self.sapLogin = MES_DB.sapLogin(self, self.cbx_sid.currentText(
        ), self.cbx_client.currentText(), self.txt_usr.text(), self.txt_pw.text())

        # Trả kết quả ra ngoài màn hình.
        self.fnc_notice(' Kết Nối SAP Thành Công....')

        # Save Login infomation
        MainWindow.saveinfo(self)


    def saveinfo(self):
        file_usr = open(r'ALK_App\dist\IMG\user.txt','w')
        info = [self.cbx_sid.currentText(),
                self.cbx_client.currentText(),
                self.txt_usr.text(),
                self.txt_pw.text()
                ]
        file_usr.write(str(info))

    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Select Save Location")
        self.fnc_notice(str(self.file[0]))


# -Main------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
# #-End-------------------------------------------------------------------
