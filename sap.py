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
    # TuNA 2211118 _ Define Open SAP.
    def open_sap(self):
        self.path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(self.path)

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

    def sapLogout(self):
        self.connection.CloseSession('ses[0]')

    # Đếm số ký tự trong chuỗi
    def count_char(self, dict, keys):
        count = 0
        for char in dict:
            count = count + char.count(keys, 1)
        return (count)

    def sapConnect(self):
        self.SapGuiAuto = win32.GetObject("SAPGUI")
        application = self.SapGuiAuto.GetScriptingEngine
        self.connection = application.OpenConnection(self.sid, True)
        time.sleep(1)
        self.session = self.connection.Children(0)
        self.session.findById("wnd[0]").maximize
    # Auto generate Material Code from SAP.

    # TuNA 2221118_ Start add SAP Close script.

    def sapCreatePIR(file_path):
        sap = SapGui()
        sap.sapConnect()
        data = pd.read_excel(file_path)
        print(data)
        data.columns = data.columns.str.replace(" ", "_")
        info_record = []
        pir_time = []
        sap_msg = []
        try:
            for index, row in data.iterrows():
                sap.session.findById("wnd[0]/tbar[0]/okcd").Text = "/nme11"
                sap.session.findById("wnd[0]").sendVKey(0)
                # Subcontract
                sap.session.findById("wnd[0]/usr/radRM06I-LOHNB").Select()
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINA-LIFNR").Text = row.VENDOR   # Vendor
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINA-MATNR").Text = row.MATERIAL  # Material
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINE-EKORG").Text = row.PLANT     # Plant
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINE-WERKS").Text = row.PUR_ORG   # Pur.Org
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINA-INFNR").Text = ""   # Info Record
                sap.session.findById("wnd[0]").sendVKey(0)
                try:
                    sap.session.findById("wnd[0]").sendVKey(0)
                    sap_messages = str(
                        sap.session.findById("wnd[0]/sbar").Text)
                    print(sap_messages)
                    if 'exists' in sap_messages:
                        info_record.append(sap_messages[23:33])
                        sap_msg.append(sap_messages)
                        gettime = datetime.now()
                        pir_time.append(gettime.strftime('%Y%m%d-%H%M%S'))
                        continue
                except:
                    continue
                sap.session.findById("wnd[0]").sendVKey(0)
                sap.session.findById("wnd[0]/usr/txtEINE-APLFZ").Text = "1"
                sap.session.findById("wnd[0]/usr/txtEINE-UNTTO").Text = "0"
                sap.session.findById("wnd[0]/usr/ctxtEINE-EKGRP").Text = "105"
                sap.session.findById("wnd[0]/usr/txtEINE-NORBM").Text = "1"
                sap.session.findById(
                    "wnd[0]/usr/chkEINE-WEBRE").Selected = True
                sap.session.findById("wnd[0]/usr/ctxtEINE-MWSKZ").Text = "VA"
                sap.session.findById("wnd[0]/usr/ctxtEINE-BWTAR").Text = "EX"
                sap.session.findById("wnd[0]/usr/txtEINE-UNTTO").Text = "0"
                sap.session.findById("wnd[0]/usr/txtEINE-UEBTO").Text = "0"
                sap.session.findById(
                    "wnd[0]/usr/chkEINE-UEBTK").Selected = True
                sap.session.findById("wnd[0]/usr/ctxtEINE-BSTAE").Text = "0004"
                sap.session.findById(
                    "wnd[0]/usr/txtEINE-NETPR").Text = row.NET_PRICE  # Price
                sap.session.findById(
                    "wnd[0]/usr/txtEINE-PEINH").Text = row.PER  # Per
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINE-BPRME").Text = row.OUP  # OUP
                if row.OUN != row.OUP:
                    sap.session.findById("wnd[0]").sendVKey(0)
                    sap.session.findById(
                        "wnd[0]/usr/txtEINE-BPUMN").Text = int(row.NUME)
                    sap.session.findById(
                        "wnd[0]/usr/txtEINE-BPUMZ").Text = row.DENO
                sap.session.findById("wnd[0]").sendVKey(0)
                sap.session.findById("wnd[0]").sendVKey(0)
                sap.session.findById("wnd[0]").sendVKey(0)
                sap.session.findById("wnd[0]").sendVKey(8)
                sap.session.findById(
                    "wnd[0]/usr/ctxtRV13A-DATAB").Text = row.VAILD_FROM  # Vaid From
                sap.session.findById(
                    "wnd[0]/usr/ctxtRV13A-DATBI").Text = row.VAILD_TO  # Vaid To
                sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
                sap_messages = sap.session.findById("wnd[0]/sbar").Text
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
            sap.count_char(sap_msg, "exits")
        err = "Exist: " + str(sap.count_char(sap_msg, "exists")
                              ) + "/" + str(data.shape[0])
        ok = "Created: " + \
            str(sap.count_char(sap_msg, "created")) + "/" + str(data.shape[0])
        msg = str(err) + " " + str(ok) + "        " + str(f_combied)
        return msg,f_combied

    def sapChangePIR(file_path):
        sap = SapGui()
        sap.sapConnect()
        data = pd.read_excel(file_path)
        data.columns = data.columns.str.replace(" ", "_")
        info_record = []
        pir_time = []
        try:
            for index, row in data.iterrows():
                sap.session.findById("wnd[0]/tbar[0]/okcd").Text = "/nme12"
                sap.session.findById("wnd[0]").sendVKey(0)
                # Subcontract
                sap.session.findById("wnd[0]/usr/radRM06I-LOHNB").Select()
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINA-LIFNR").Text = row.VENDOR   # Vendor
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINA-MATNR").Text = row.MATERIAL  # Material
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINE-EKORG").Text = row.PLANT     # Plant
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINE-WERKS").Text = row.PUR_ORG   # Pur.Org
                sap.session.findById(
                    "wnd[0]/usr/ctxtEINA-INFNR").Text = ""  # Info Record
                sap.session.findById("wnd[0]").sendVKey(0)
                try:
                    # Change Order Unit
                    if row.OUN != sap.session.findById("wnd[0]/usr/ctxtEINA-MEINS").Text:
                        sap.session.findById(
                            "wnd[0]/usr/ctxtEINA-MEINS").Text = row.OUN
                        sap.session.findById(
                            "wnd[0]/usr/txtEINA-UMREN").Text = row.NUME
                        sap.session.findById(
                            "wnd[0]/usr/txtEINA-UMREZ").Text = row.DENO
                        sap.session.findById("wnd[0]").sendVKey(0)
                    sap.session.findById("wnd[0]").sendVKey(0)
                    sap.session.findById("wnd[0]/usr/txtEINE-APLFZ").Text = "1"
                    sap.session.findById("wnd[0]/usr/txtEINE-UNTTO").Text = "0"
                    sap.session.findById(
                        "wnd[0]/usr/ctxtEINE-EKGRP").Text = "105"
                    sap.session.findById("wnd[0]/usr/txtEINE-NORBM").Text = "1"
                    sap.session.findById(
                        "wnd[0]/usr/chkEINE-WEBRE").Selected = True
                    sap.session.findById(
                        "wnd[0]/usr/ctxtEINE-MWSKZ").Text = "VA"
                    sap.session.findById(
                        "wnd[0]/usr/ctxtEINE-BWTAR").Text = "EX"
                    sap.session.findById("wnd[0]/usr/txtEINE-UNTTO").Text = "0"
                    sap.session.findById("wnd[0]/usr/txtEINE-UEBTO").Text = "0"
                    sap.session.findById(
                        "wnd[0]/usr/chkEINE-UEBTK").Selected = True
                    sap.session.findById(
                        "wnd[0]/usr/ctxtEINE-BSTAE").Text = "0004"
                    sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
                    try:
                        sap.session.findById("wnd[1]/tbar[0]/btn[7]").press()
                    except:
                        pass
                    sap.session.findById(
                        "wnd[0]/usr/ctxtRV13A-DATAB").Text = row.VAILD_FROM  # Vaid F
                    sap.session.findById(
                        "wnd[0]/usr/ctxtRV13A-DATBI").Text = row.VAILD_TO  # Vaid T

                    sap.session.findById(
                        "wnd[0]/usr/tblSAPMV13ATCTRL_D0201").getAbsoluteRow(0).selected = True
                    sap.session.findById(
                        "wnd[0]/usr/tblSAPMV13ATCTRL_D0201/txtKONP-KBETR[2,0]").Text = row.NET_PRICE
                    sap.session.findById(
                        "wnd[0]/usr/tblSAPMV13ATCTRL_D0201/txtKONP-KPEIN[4,0]").Text = row.PER
                    sap.session.findById(
                        "wnd[0]/usr/tblSAPMV13ATCTRL_D0201/ctxtKONP-KMEIN[5,0]").Text = row.OUP
                    if row.OUN != row.OUP:
                        sap.session.findById(
                            "wnd[0]/mbar/menu[2]/menu[7]").select()
                        sap.session.findById("wnd[0]/tbar[1]/btn[13]").press()
                        sap.session.findById(
                            "wnd[1]/usr/txtKONP-KUMNE").Text = row.DENO
                        sap.session.findById(
                            "wnd[1]/usr/txtKONP-KUMZA").Text = row.NUME
                        sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()

                    sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
                    sap.session.findById("wnd[1]/tbar[0]/btn[5]").press()
                    sap_messages = sap.session.findById("wnd[0]/sbar").Text
                    print(int(index)+1, row.MATERIAL, sap_messages)
                except:
                    continue
                finally:
                    sap_messages = sap.session.findById("wnd[0]/sbar").Text
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
        sap = SapGui()
        sap.sapConnect()
        data = pd.read_excel(file_path,
                             keep_default_na=False).astype(str)
        data.columns = data.columns.str.replace(" ", "_")
        # GET ACTIVE NUMBER RANGE VIA MATERIAL GROUP.
        m_active = []       # Active Number Range
        mgroup = []
        print("*** Start checking number range ***")
        for m_group in set(data.MATL_GROUP[3:]):
            sap.session.findById("wnd[0]/tbar[0]/okcd").Text = "/nmm60"
            sap.session.findById("wnd[0]").sendVKey(0)
            sap.session.findById(
                "wnd[0]/usr/ctxtMS_MATNR-LOW").Text = "*" + m_group + "*"
            sap.session.findById(
                "wnd[0]/usr/ctxtMS_MATNR-HIGH").Text = m_group + "9999"
            sap.session.findById("wnd[0]/usr/ctxtMATKL-LOW").Text = m_group
            sap.session.findById("wnd[0]").sendVKey(8)
            if sap.session.findById("wnd[0]/sbar").text == "No materials can be displayed":
                m_active.append(m_group + "0008")
            else:
                sap.session.findById(
                    "wnd[0]/usr/cntlGRID1/shellcont/shell").CurrentCellRow = -1
                sap.session.findById(
                    "wnd[0]/usr/cntlGRID1/shellcont/shell").SelectColumn("MATNR")
                sap.session.findById("wnd[0]/tbar[1]/btn[40]").Press()
                GridView = sap.session.findById(
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

    # SAP Auto Change Bussiness Partner _ 2022.06.02.
        # Change Name 1/2/3/4.
        # Change TaxCode.

    def sapChangeBP(file_path):
        sap = SapGui()
        sap.sapConnect()
        data = pd.read_excel(file_path, keep_default_na=False)
        data.columns = data.columns.str.replace(" ", "_")
        # Define MSG & Time Process Column.
        sap_msg = []
        time_msg = []
        # Load data from Excel & Start Script.
        try:
            for index, row in data.iterrows():
                sap.session.findById("wnd[0]/tbar[0]/okcd").Text = "/nbp"
                sap.session.findById("wnd[0]").sendVKey(0)
                sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2240/subSCREEN_1010_LEFT_AREA:SAPLBUS_LOCATOR:3100/tabsGS_SCREEN_3100_TABSTRIP/tabpBUS_LOCATOR_TAB_02/ssubSCREEN_3100_TABSTRIP_AREA:SAPLBUS_LOCATOR:3202/subSCREEN_3200_SEARCH_AREA:SAPLBUS_LOCATOR:3211/subSCREEN_3200_SEARCH_FIELDS_AREA:SAPLBUPA_DIALOG_SEARCH:2100/txtBUS_JOEL_SEARCH-PARTNER_NUMBER").text = row.BP
                sap.session.findById("wnd[0]").sendVKey(0)
                sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2240/subSCREEN_1010_LEFT_AREA:SAPLBUS_LOCATOR:3100/tabsGS_SCREEN_3100_TABSTRIP/tabpBUS_LOCATOR_TAB_02/ssubSCREEN_3100_TABSTRIP_AREA:SAPLBUS_LOCATOR:3202/subSCREEN_3200_SEARCH_AREA:SAPLBUS_LOCATOR:3211/subSCREEN_3200_RESULT_AREA:SAPLBUPA_DIALOG_JOEL:1060/ssubSCREEN_1060_RESULT_AREA:SAPLBUPA_DIALOG_JOEL:1080/cntlSCREEN_1080_CONTAINER/shellcont/shell").selectedRows = "0"
                sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2240/subSCREEN_1010_LEFT_AREA:SAPLBUS_LOCATOR:3100/tabsGS_SCREEN_3100_TABSTRIP/tabpBUS_LOCATOR_TAB_02/ssubSCREEN_3100_TABSTRIP_AREA:SAPLBUS_LOCATOR:3202/subSCREEN_3200_SEARCH_AREA:SAPLBUS_LOCATOR:3211/subSCREEN_3200_RESULT_AREA:SAPLBUPA_DIALOG_JOEL:1060/ssubSCREEN_1060_RESULT_AREA:SAPLBUPA_DIALOG_JOEL:1080/cntlSCREEN_1080_CONTAINER/shellcont/shell").doubleClickCurrentCell()
                sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01").Select()
                print(row.Name1)
                sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7016/subA02P02:SAPLBUD0:1200/txtBUT000-NAME_ORG1").text = row.Name1
                sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7016/subA02P02:SAPLBUD0:1200/txtBUT000-NAME_ORG2").text = row.Name2
                sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7016/subA02P02:SAPLBUD0:1200/txtBUT000-NAME_ORG3").text = row.Name3
                sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7016/subA02P02:SAPLBUD0:1200/txtBUT000-NAME_ORG4").text = row.Name4
                sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
                try:
                    sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
                    sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
                    # if row.TaxCode !="":
                    #     sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_03").Select()
                    # try:
                    #     sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
                    #     sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
                    # except:
                    #     pass
                    #     sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_03/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7012/subA08P01:SAPLBUPA_BUTX_DIALOG:0100/tblSAPLBUPA_BUTX_DIALOGTCTRL_BPTAX/ctxtDFKKBPTAXNUM-TAXTYPE[0,0]").text = "VN1"
                    #     sap.session.findById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_03/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7012/subA08P01:SAPLBUPA_BUTX_DIALOG:0100/tblSAPLBUPA_BUTX_DIALOGTCTRL_BPTAX/txtDFKKBPTAXNUM-TAXNUMXL[2,0]").text = row.TaxCode
                except:
                    pass
                finally:
                    sap_messages = sap.session.findById("wnd[0]/sbar").Text
                    print(int(index)+1, row.BP, sap_messages)
                    sap_msg.append(sap_messages)
                    gettime = datetime.now()
                    time_msg.append(gettime.strftime('%Y%m%d-%H%M%S'))
                continue
        except:
            pass
        finally:
            # Assign Cols & Export to Excel.
            tmp = pd.DataFrame({
                'ZMSG': sap_msg,
                'TIME': time_msg
            })
            df = pd.concat([data, tmp], axis=1)
            dt = datetime.now()
            row.TIME = dt.strftime('%Y%m%d-%H%M%S')
            f_combied = 'Aluko_Change BP' + \
                '_' + dt.strftime('%Y%m%d-%H%M%S') + '.xlsx'
            df.to_excel(f_combied, sheet_name='PIR', index=False)

    def sap_MM02_Delivery(file_path):
        # Auto Tick to ZDelivery:
        sap = SapGui()
        sap.sapConnect()
        data = pd.read_excel(file_path, keep_default_na=False, header=0)
        data.columns = data.columns.str.replace(" ", "_")
        df = pd.DataFrame(data[3:])
        print(df)
        # Define MSG & Time Process Column.
        sap_msg = []
        time_msg = []
        sap_werks = []
        sap_matnr = []
        # Load data from Excel & Start Script.
        try:
            for index, row in df.iterrows():
                print(row.MATERIAL)
                sap.session.findById("wnd[0]").maximize
                sap.session.findById("wnd[0]/tbar[0]/okcd").text = "/nmm02"
                sap.session.findById("wnd[0]").sendVKey(0)
                sap.session.findById(
                    "wnd[0]/usr/ctxtRMMG1-MATNR").text = row.MATERIAL
                sap.session.findById("wnd[0]").sendVKey(0)
                sap.session.findById("wnd[1]/tbar[0]/btn[19]").press()
                sap.session.findById("wnd[1]/tbar[0]/btn[20]").press()
                sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
                sap.session.findById(
                    "wnd[1]/usr/ctxtRMMG1-WERKS").text = row.PLANT
                sap.session.findById("wnd[1]").sendVKey(0)
                sap.session.findById(
                    "wnd[0]/usr/tabsTABSPR1/tabpSP21").select()
                sap.session.findById(
                    "wnd[0]/usr/tabsTABSPR1/tabpSP21/ssubTABFRA1:SAPLMGMM:2000/subSUB2:SAPLMGD1:2701/txtMARC-ZDELIVERY").text = 'X'
                sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
                sap_messages = sap.session.findById("wnd[0]/sbar").text
                print(int(index)+1, sap_messages)
                sap_msg.append(sap_messages)
                sap_werks.append(row.PLANT)
                sap_matnr.append(row.MATERIAL)
                gettime = datetime.now()
                time_msg.append(gettime.strftime('%Y%m%d-%H%M%S'))
        except:
            pass
        finally:
            # Assign Cols & Export to Excel.
            tmp = pd.DataFrame({
                'MATERIAL': sap_matnr,
                'PLANT': sap_werks,
                'ZMSG': sap_msg,
                'TIME': time_msg
            })
            dt = datetime.now()
            row.TIME = dt.strftime('%Y%m%d-%H%M%S')
            f_combied = 'Aluko_ZDelivery' + \
                '_' + dt.strftime('%Y%m%d-%H%M%S') + '.xlsx'
            tmp.to_excel(f_combied, sheet_name='PIR', index=False)
