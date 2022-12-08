# -Begin-----------------------------------------------------------------
# Fnc SAP Scripting
# -Includes--------------------------------------------------------------
import subprocess
import win32com.client as win32
import sys
import os
import time
import pandas as pd
from datetime import datetime
# -SUB Main--------------------------------------------------------------


class SapGui():
    def __init__(self) -> None:
        super().__init__()
        # self.sapConnect()
    # TuNA 2211118 _ Define Open SAP GUI.
    def open_sap(self):
        self.path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(self.path)
    # Login SAPGUI function.
    def sapLogin(self, sid, clt, usr, pwd):
        # KHAI BÁO DỮ LIỆU SAP
        self.sid = sid
        self.clt = clt
        self.usr = usr
        self.pwd = pwd
        # Connect SAP GUI
        self.open_sap()
        time.sleep(1)
        self.SapGuiAuto = win32.GetObject("SAPGUI")
        application = self.SapGuiAuto.GetScriptingEngine
        self.connection = application.OpenConnection(self.sid, True)
        time.sleep(1)
        self.session = self.connection.Children(0)
        try:
            # THE CLIENT
            self.session.findById("wnd[0]/usr/txtRSYST-MANDT").Text = self.clt
            # USERNAME
            self.session.findById("wnd[0]/usr/txtRSYST-BNAME").Text = self.usr
            # PASSWORD
            self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").Text = self.pwd
            # LANGUAGE
            self.session.findById("wnd[0]/usr/txtRSYST-LANGU").Text = 'EN'
            # ENTER
            self.session.findById("wnd[0]").sendVKey(0)
            if self.session.findById("wnd[0]/sbar").Text != "":
                msg = self.session.findById("wnd[0]/sbar").Text
            else:
                msg = 'Đăng nhập SAP thành công ....'
        except Exception as e:
            msg = e
        finally:
            return msg

    # Logout SAPGUI function.
    def sapLogout(self):
        self.connection.CloseSession('ses[0]')
        return 'Logout SAP Completed.'
    
    # Count by character in string.
    def count_char(self, dict, keys):
        count = 0
        for char in dict:
            count = count + char.count(keys, 1)
        return (count)

    # Connect Python with SAPGUI via Script.
    def sapConnect(self):
        try:
            self.SapGuiAuto = win32.GetObject("SAPGUI")
            application = self.SapGuiAuto.GetScriptingEngine
            #self.connection = application.OpenConnection(self.sid,True)
            self.connection = application.Children(0)
            self.session = self.connection.Children(0)
            msg = 'Connection successful.'
        except:
            msg = 'Require to login to SAP before starting this function.'
        finally:
            return msg

    # Auto generate Material Code from self.

    def sapCreatePIR(self, file_path):
        data = pd.read_excel(file_path)
        print(data)
        data.columns = data.columns.str.replace(" ", "_")
        info_record = []
        pir_time = []
        sap_msg = []
        try:
            for index, row in data.iterrows():
                self.session.findById(
                    "wnd[0]/tbar[0]/okcd").Text = "/nme11"
                self.session.findById("wnd[0]").sendVKey(0)
                # Subcontract
                self.session.findById("wnd[0]/usr/radRM06I-LOHNB").Select()
                self.session.findById(
                    "wnd[0]/usr/ctxtEINA-LIFNR").Text = row.VENDOR   # Vendor
                self.session.findById(
                    "wnd[0]/usr/ctxtEINA-MATNR").Text = row.MATERIAL  # Material
                self.session.findById(
                    "wnd[0]/usr/ctxtEINE-EKORG").Text = row.PLANT     # Plant
                self.session.findById(
                    "wnd[0]/usr/ctxtEINE-WERKS").Text = row.PUR_ORG   # Pur.Org
                self.session.findById(
                    "wnd[0]/usr/ctxtEINA-INFNR").Text = ""   # Info Record
                self.session.findById("wnd[0]").sendVKey(0)
                try:
                    self.session.findById("wnd[0]").sendVKey(0)
                    sap_messages = str(
                        self.session.findById("wnd[0]/sbar").Text)
                    print(sap_messages)
                    if 'exists' in sap_messages:
                        info_record.append(sap_messages[23:33])
                        sap_msg.append(sap_messages)
                        gettime = datetime.now()
                        pir_time.append(gettime.strftime('%Y%m%d-%H%M%S'))
                        continue
                except:
                    continue
                self.session.findById("wnd[0]").sendVKey(0)
                self.session.findById(
                    "wnd[0]/usr/txtEINE-APLFZ").Text = "1"
                self.session.findById(
                    "wnd[0]/usr/txtEINE-UNTTO").Text = "0"
                self.session.findById(
                    "wnd[0]/usr/ctxtEINE-EKGRP").Text = "105"
                self.session.findById(
                    "wnd[0]/usr/txtEINE-NORBM").Text = "1"
                self.session.findById(
                    "wnd[0]/usr/chkEINE-WEBRE").Selected = True
                self.session.findById(
                    "wnd[0]/usr/ctxtEINE-MWSKZ").Text = "VA"
                self.session.findById(
                    "wnd[0]/usr/ctxtEINE-BWTAR").Text = "EX"
                self.session.findById(
                    "wnd[0]/usr/txtEINE-UNTTO").Text = "0"
                self.session.findById(
                    "wnd[0]/usr/txtEINE-UEBTO").Text = "0"
                self.session.findById(
                    "wnd[0]/usr/chkEINE-UEBTK").Selected = True
                self.session.findById(
                    "wnd[0]/usr/ctxtEINE-BSTAE").Text = "0004"
                self.session.findById(
                    "wnd[0]/usr/txtEINE-NETPR").Text = row.NET_PRICE  # Price
                self.session.findById(
                    "wnd[0]/usr/txtEINE-PEINH").Text = row.PER  # Per
                self.session.findById(
                    "wnd[0]/usr/ctxtEINE-BPRME").Text = row.OUP  # OUP
                if row.OUN != row.OUP:
                    self.session.findById("wnd[0]").sendVKey(0)
                    self.session.findById(
                        "wnd[0]/usr/txtEINE-BPUMN").Text = int(row.NUME)
                    self.session.findById(
                        "wnd[0]/usr/txtEINE-BPUMZ").Text = row.DENO
                self.session.findById("wnd[0]").sendVKey(0)
                self.session.findById("wnd[0]").sendVKey(0)
                self.session.findById("wnd[0]").sendVKey(0)
                self.session.findById("wnd[0]").sendVKey(8)
                self.session.findById(
                    "wnd[0]/usr/ctxtRV13A-DATAB").Text = row.VAILD_FROM  # Vaid From
                self.session.findById(
                    "wnd[0]/usr/ctxtRV13A-DATBI").Text = row.VAILD_TO  # Vaid To
                self.session.findById("wnd[0]/tbar[0]/btn[11]").press()
                sap_messages = self.session.findById("wnd[0]/sbar").Text
                print(index, sap_messages)
                sap_msg.append(sap_messages)
                info_record.append(sap_messages[23:33])
                gettime = datetime.now()
                pir_time.append(gettime.strftime('%Y%m%d-%H%M%S'))
        except:
            return ("*** Lỗi, cần check lại ***")
        finally:
            tmp = pd.DataFrame({
                'INFO_RECORD': info_record,
                'TIME': pir_time,
                'MSG': sap_msg,
            })
            df = pd.concat([data, tmp], axis=1)
            dt = datetime.now()
            row.TIME = dt.strftime('%Y%m%d-%H%M%S')
            f_combied = 'Aluko_Info Record' + \
                '_' + dt.strftime('%Y%m%d-%H%M%S') + '.xlsx'
            df.to_excel(f_combied, sheet_name='PIR', index=False)
            self.count_char(sap_msg, "exits")
        err = "Exist: " + str(self.count_char(sap_msg, "exists")
                                ) + "/" + str(data.shape[0])
        ok = "Created: " + \
            str(self.count_char(sap_msg, "created")) + \
            "/" + str(data.shape[0])
        msg = str(err) + " " + str(ok) + "        " + str(f_combied)
        result = msg = ("{0}\{1}".format(os.getcwd(), f_combied))
        return msg, result

    def sapChangePIR(self, file_path):
        data = pd.read_excel(file_path)
        data.columns = data.columns.str.replace(" ", "_")
        info_record = []
        pir_time = []
        try:
            for index, row in data.iterrows():
                self.session.findById("wnd[0]/tbar[0]/okcd").Text = "/nme12"
                self.session.findById("wnd[0]").sendVKey(0)
                # Subcontract
                self.session.findById("wnd[0]/usr/radRM06I-LOHNB").Select()
                self.session.findById(
                    "wnd[0]/usr/ctxtEINA-LIFNR").Text = row.VENDOR   # Vendor
                self.session.findById(
                    "wnd[0]/usr/ctxtEINA-MATNR").Text = row.MATERIAL  # Material
                self.session.findById(
                    "wnd[0]/usr/ctxtEINE-EKORG").Text = row.PLANT     # Plant
                self.session.findById(
                    "wnd[0]/usr/ctxtEINE-WERKS").Text = row.PUR_ORG   # Pur.Org
                self.session.findById(
                    "wnd[0]/usr/ctxtEINA-INFNR").Text = ""  # Info Record
                self.session.findById("wnd[0]").sendVKey(0)
                try:
                    # Change Order Unit
                    if row.OUN != self.session.findById("wnd[0]/usr/ctxtEINA-MEINS").Text:
                        self.session.findById(
                            "wnd[0]/usr/ctxtEINA-MEINS").Text = row.OUN
                        self.session.findById(
                            "wnd[0]/usr/txtEINA-UMREN").Text = row.NUME
                        self.session.findById(
                            "wnd[0]/usr/txtEINA-UMREZ").Text = row.DENO
                        self.session.findById("wnd[0]").sendVKey(0)
                    self.session.findById("wnd[0]").sendVKey(0)
                    self.session.findById(
                        "wnd[0]/usr/txtEINE-APLFZ").Text = "1"
                    self.session.findById(
                        "wnd[0]/usr/txtEINE-UNTTO").Text = "0"
                    self.session.findById(
                        "wnd[0]/usr/ctxtEINE-EKGRP").Text = "105"
                    self.session.findById(
                        "wnd[0]/usr/txtEINE-NORBM").Text = "1"
                    self.session.findById(
                        "wnd[0]/usr/chkEINE-WEBRE").Selected = True
                    self.session.findById(
                        "wnd[0]/usr/ctxtEINE-MWSKZ").Text = "VA"
                    self.session.findById(
                        "wnd[0]/usr/ctxtEINE-BWTAR").Text = "EX"
                    self.session.findById(
                        "wnd[0]/usr/txtEINE-UNTTO").Text = "0"
                    self.session.findById(
                        "wnd[0]/usr/txtEINE-UEBTO").Text = "0"
                    self.session.findById(
                        "wnd[0]/usr/chkEINE-UEBTK").Selected = True
                    self.session.findById(
                        "wnd[0]/usr/ctxtEINE-BSTAE").Text = "0004"
                    self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
                    try:
                        self.session.findById("wnd[1]/tbar[0]/btn[7]").press()
                    except:
                        pass
                    self.session.findById(
                        "wnd[0]/usr/ctxtRV13A-DATAB").Text = row.VAILD_FROM  # Vaid F
                    self.session.findById(
                        "wnd[0]/usr/ctxtRV13A-DATBI").Text = row.VAILD_TO  # Vaid T

                    self.session.findById(
                        "wnd[0]/usr/tblSAPMV13ATCTRL_D0201").getAbsoluteRow(0).selected = True
                    self.session.findById(
                        "wnd[0]/usr/tblSAPMV13ATCTRL_D0201/txtKONP-KBETR[2,0]").Text = row.NET_PRICE
                    self.session.findById(
                        "wnd[0]/usr/tblSAPMV13ATCTRL_D0201/txtKONP-KPEIN[4,0]").Text = row.PER
                    self.session.findById(
                        "wnd[0]/usr/tblSAPMV13ATCTRL_D0201/ctxtKONP-KMEIN[5,0]").Text = row.OUP
                    if row.OUN != row.OUP:
                        self.session.findById(
                            "wnd[0]/mbar/menu[2]/menu[7]").select()
                        self.session.findById("wnd[0]/tbar[1]/btn[13]").press()
                        self.session.findById(
                            "wnd[1]/usr/txtKONP-KUMNE").Text = row.DENO
                        self.session.findById(
                            "wnd[1]/usr/txtKONP-KUMZA").Text = row.NUME
                        self.session.findById("wnd[1]/tbar[0]/btn[0]").press()

                    self.session.findById("wnd[0]/tbar[0]/btn[11]").press()
                    self.session.findById("wnd[1]/tbar[0]/btn[5]").press()
                    sap_messages = self.session.findById("wnd[0]/sbar").Text
                    print(int(index)+1, row.MATERIAL, sap_messages)
                except:
                    continue
                finally:
                    sap_messages = self.session.findById("wnd[0]/sbar").Text
                    print(int(index)+1, row.MATERIAL, sap_messages)
                    info_record.append(sap_messages)
                    gettime = datetime.now()
                    pir_time.append(gettime.strftime('%Y%m%d-%H%M%S'))
                    tmp = pd.DataFrame({
                        'INFO_RECORD': info_record,
                        'TIME': pir_time
                    })
        finally:
            df = pd.concat([data, tmp], axis=1)
            dt = datetime.now()
            row.TIME = dt.strftime('%Y%m%d-%H%M%S')
            f_combied = 'Aluko_Info Record_Change' + \
                '_' + dt.strftime('%Y%m%d-%H%M%S') + '.xlsx'
            df.to_excel(f_combied, sheet_name='PIR', index=False)

    def sapCreateMaterial(self, file_path):
        data = pd.read_excel(file_path,
                             keep_default_na=False).astype(str)
        data.columns = data.columns.str.replace(" ", "_")
        # GET ACTIVE NUMBER RANGE VIA MATERIAL GROUP.
        m_active = []       # Active Number Range
        mgroup = []
        print("*** Start checking number range ***")
        for m_group in set(data.MATL_GROUP[3:]):
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").Text = "/nmm60"
            self.session.findById("wnd[0]").sendVKey(0)
            self.session.findById(
                "wnd[0]/usr/ctxtMS_MATNR-LOW").Text = "*" + m_group + "*"
            self.session.findById(
                "wnd[0]/usr/ctxtMS_MATNR-HIGH").Text = m_group + "9999"
            self.session.findById("wnd[0]/usr/ctxtMATKL-LOW").Text = m_group
            self.session.findById("wnd[0]").sendVKey(8)
            if self.session.findById("wnd[0]/sbar").text == "No materials can be displayed":
                m_active.append(m_group + "0008")
            else:
                self.session.findById(
                    "wnd[0]/usr/cntlGRID1/shellcont/shell").CurrentCellRow = -1
                self.session.findById(
                    "wnd[0]/usr/cntlGRID1/shellcont/shell").SelectColumn("MATNR")
                self.session.findById("wnd[0]/tbar[1]/btn[40]").Press()
                GridView = self.session.findById(
                    "wnd[0]/usr/cntlGRID1/shellcont/shell")
                m_active.append(GridView.GetCellValue(
                    0, GridView.ColumnOrder(0)))
            mgroup.append(m_group)
        print("***", mgroup, " ***")
        tmp = pd.DataFrame({
            'MATL_GROUP': mgroup,
            'MATL_ACTV': m_active
        })
        df = pd.merge(
            data.drop(labels=[0, 1, 2]),
            tmp,
            on='MATL_GROUP',
            how='left',
        ).fillna(0)
        # FILL MATERIAL TO EXCEL
        print("*** Assign Material Number ***")
        for index, row in df.iterrows():
            count_g = sum(1 for i in df.MATL_GROUP[:int(
                index)+1] if i == row.MATL_GROUP)
            if count_g != 0:
                row.MATERIAL = count_g + int(row.MATL_ACTV)
            print(row.MATERIAL)
        # Define Defaul Data
        print("*** Defaul Material Master Data ***")
        mdm_header = data.head(3)
        hav1 = df.drop('MATL_ACTV', axis=1)
        hav1.PLANT = 2100
        hav1.VKORG = 2100
        bd = df.drop('MATL_ACTV', axis=1)
        bd.PLANT = 2110
        bd.VKORG = 2100
        hav2 = df.drop('MATL_ACTV', axis=1)
        hav2.PLANT = 2120
        hav2.VKORG = 2100
        alk = df.drop('MATL_ACTV', axis=1)
        alk.PLANT = 2300
        alk.VKORG = 2300
        # Extend to All Plant
        print("*** Extend to All Plant ***")
        map = pd.concat([mdm_header, hav1, bd, hav2, alk])
        df_mdm = map.drop_duplicates()
        dt = datetime.now()
        print("*** Export to Excel File ***")
        f_combied = 'Aluko_Material' + \
            '_' + dt.strftime('%Y%m%d-%H%M%S') + '.xlsx'
        df_mdm.to_excel(f_combied, index=False)
        msg = ("{0}\{1}".format(os.getcwd(), f_combied))
        return msg
