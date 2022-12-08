from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, os, sys
from datetime import datetime
import pandas as pd


class RPA_MES():
    def __init__(self, ip, usr, pwd) -> None:
        self.ip = ip
        self.usr = usr
        self.pwd = pwd
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument("headless") # Run in background
        self.driver = webdriver.Chrome(
            executable_path=r'dist\Lib\chromedriver.exe', chrome_options=options)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()

    def mes_login(self):
        self.driver.get(self.ip)
        elm_usr = self.driver.find_element(By.NAME, "username")
        elm_usr.send_keys(self.usr)
        time.sleep(1)
        elm_pwd = self.driver.find_element(By.NAME, "password")
        elm_pwd.send_keys(self.pwd)
        time.sleep(1)
        btn_login = elm_usr = self.driver.find_element(
            By.ID, "login_buttonLogin")
        btn_login.click()
        return ('Login Completed.')

    def mes_tab(self, tab_id):
        time.sleep(1)
        self.driver.get(str(self.ip + '#/tabs/' + tab_id))

        return 'Load website thành công.'

    def mes_30920001(self, inbound, material, qty):
        # Thao tác màn hình kiểm tra số lượng mua
        # Kiểm tra số inbound.
        self.driver.get(str(self.ip + '#/tabs/' + "30920001"))
        time.sleep(1)
        xp_material = "//div[contains(text(),'" + material + "')]"
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, "//input[@placeholder='Start date']").click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "//a[normalize-space()='This Month']").click()
        # Điền mã Nguyên vật liệu
        self.driver.find_elements(
            By.XPATH, "//tr/th[contains(text(),'Code nguyên liệu') or contains(text(),'Material Code')]//parent::tr/td[2]/div/a")[0].click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/div/div[3]/div/div[2]/div[1]/input").send_keys(material)
        self.driver.find_element(
            By.XPATH, "//div[@class='codeSch']//i[@class='opus-ic-search-line-s']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, xp_material).click()
        self.driver.find_element(
            By.XPATH, "//span[contains(text(),'Lựa chọn')]").click()

        # Điền inbound Delivery
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[2]/td[1]/div/input").send_keys(inbound)
        time.sleep(1)
        # Tra cứu thông tin
        self.driver.find_element(
            By.XPATH, "//span[contains(text(),'Tra cứu')]").click()
        print('Đã điền inbound')
        time.sleep(2)
        # Kiểm tra nguyên vật liệu giao trực tiếp
        try:
            delivery = self.driver.find_element(
                By.XPATH, "//span[@class='jqx-checkbox-check-checked']").is_displayed()
        except:
            delivery = False
        print(delivery)
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[4]/div/div/div/div[4]/div[1]/div/div[2]/div/div[1]/div[1]").click()

        # Hoàn thành kiểm tra
        self.driver.find_element(
            By.XPATH, "//span[contains(text(),'Hoàn thành kiểm tra')]").click()
        try:
            self.driver.find_element(
                By.XPATH, "//span[normalize-space()='Yes/Có']").click()
            msg = 'Hoàn tất kiểm tra số lượng mua...'
        except:
            msg = 'Không tìm thấy Nguyên liệu trong Inbound này.'
            print(msg)
        return delivery, msg

    # Nhập vật liệu giao thẳng
    def mes_30930002(self, inbound, material, slog):
        self.driver.get(str(self.ip + '#/tabs/' + "30930002"))
        time.sleep(3)
        xp_material = "//div[contains(text(),'" + material + "')]"
        xp_slog = "//div[contains(text(),'" + slog + "')]"
        # Lookup Material
        self.driver.find_elements(
            By.XPATH, "//tr/th[contains(text(),'Code nguyên liệu') or contains(text(),'Material Code')]//parent::tr/td[1]/div/a")[0].click()
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/div[3]/div/div[2]/div[1]/input").click()
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/div[3]/div/div[2]/div[1]/input").send_keys(material)
        self.driver.find_element(
            By.XPATH, "//div[@class='codeSch']//i[@class='opus-ic-search-line-s']").click()
        time.sleep(1)
        self.action.double_click(self.driver.find_element(
            By.XPATH, xp_material)).perform()
        time.sleep(1)
        # Điền số inbound Delivery
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div/input").send_keys(inbound)
        self.driver.find_element(
            By.XPATH, "//span[contains(text(),'Tra cứu')]").click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "//div[@class='opus-ic-new-window-overlap-line-s jqx-icon']").click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[6]/div/div[2]/div[1]/input").click()

        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[6]/div/div[2]/div[1]/input").send_keys(slog)
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "//div[@class='codeSch']//i[@class='opus-ic-search-line-s']").click()
        time.sleep(1)
        self.action.double_click(
            self.driver.find_element(By.XPATH, xp_slog)).perform()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "//span[contains(text(),'Nhập kho')]").click()
        self.driver.find_element(
            By.XPATH, "//span[normalize-space()='Yes/Có']").click()
        msg = 'Nhập kho NVL giao thẳng thành công.'
        return msg

    def mes_30930001(self, inbound, material, slog, loc, qty):
        time.sleep(1)
        self.driver.get(str(self.ip + '#/tabs/' + "30930001"))
        time.sleep(1)
        # Thao tác màn hình nhập kho NVL trực tiếp
        try:
            # Input Inbound Delivery Number
            time.sleep(2)
            xp_inbound = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr/td[3]/div/input")
            if xp_inbound.text != inbound:
                try:
                    xp_inbound.clear()
                    xp_inbound.send_keys(inbound)
                except:
                    pass
            # Lookup Material Line
            xp_material = "//div[contains(text(),'" + material + "')]"
            self.driver.find_elements(
                By.XPATH, "//tr/th[contains(text(),'Code nguyên liệu') or contains(text(),'Material Code')]//parent::tr/td[1]/div/a")[0].click()
            time.sleep(1)
            self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[3]/div/div[2]/div[1]/input").send_keys(material)
            self.driver.find_element(
                By.XPATH, "//div[@class='codeSch']//i[@class='opus-ic-search-line-s']").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, xp_material).click()
            self.driver.find_element(
                By.XPATH, "//span[contains(text(),'Lựa chọn')]").click()
            self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/span").click()
            time.sleep(1)
            xp_material = "//div[contains(text(),'" + material + "')]"
            try:
                self.driver.find_element(By.XPATH, xp_material).click()
            except:
                erorr_msg = 'Không tìm thấy Nguyên liệu trong Inbound này.'

            self.driver.find_element(
                By.XPATH, "//div[@class='jqx-grid-cell jqx-item grid_codeview_input jqx-grid-cell-selected jqx-fill-state-pressed']//div[@class='opus-ic-new-window-overlap-line-s jqx-icon']").click()
            time.sleep(1)
            self.driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[5]/div[1]/div[2]/div[1]/input[1]").send_keys(slog)
            self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[5]/div/div[2]/a[2]").click()
            time.sleep(1)
            self.action.double_click(self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[5]/div/div[3]/div/div/div/div[4]/div[2]/div/div[1]/div[3]/div")).perform()
            # Xác định vị trí chất xếp.
            time.sleep(1)
            xp_loc = "//div[contains(text(),'" + loc + "')]"
            try:
                self.driver.find_element(By.XPATH, xp_loc).click()
                erorr_msg = "Đã tìm thấy vị trí chất xếp."
                xp_checkbox = "//div[contains(text(),'" + loc + \
                    "')]/parent::div//preceding::div[contains(@style,'display: inline')][1]/div"
                self.driver.find_element(By.XPATH, xp_checkbox).click()
                xp_qty = "//div[contains(text(),'" + loc + \
                    "')]/parent::div//following::div[contains(@style,'display: inline')][2]"
                self.driver.find_element(By.XPATH, xp_qty).click()
                self.driver.find_element(
                    By.XPATH, "//input[@type='textarea']").send_keys(qty)

            except:
                self.driver.find_element(
                    By.XPATH, "//span[normalize-space()='Thêm']").click()
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[5]/div/table/tbody/table/tbody/tr[3]/td[2]/input").clear()
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[5]/div/table/tbody/table/tbody/tr[3]/td[2]/input").send_keys(qty)
                self.driver.find_elements(
                    By.XPATH, "//tr/th[contains(text(),'Vị trí chất xếp') or contains(text(),'MM MATExxx')]//parent::tr/td[1]/div/a")[0].click()
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[5]/div/table/tbody/table/tbody/tr[3]/td[1]/div/div[3]/div/div[2]/div[1]/input").send_keys(loc)
                self.driver.find_element(
                    By.XPATH, "//div[@class='codeSch']//i[@class='opus-ic-search-line-s']").click()
                try:
                    self.driver.find_element(
                        By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[5]/div/table/tbody/table/tbody/tr[3]/td[1]/div/div[3]/div/div[3]/div/div/div/div[4]/div[2]/div/div[1]/div[1]/span").text == "No data to display"
                    erorr_msg = 'Không tìm thấy vị trí chất xếp.'

                except:
                    list_loc = "//div[@class='jqx-grid-cell-middle-align'][normalize-space()='" + \
                        loc + "']"
                    time.sleep(1)
                    self.action.double_click(
                        self.driver.find_element(By.XPATH, list_loc)).perform()
                    self.driver.find_element(
                        By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[5]/div/div/div/div[2]/span").click()
            finally:
                time.sleep(1)
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[4]/div[1]/div[3]/div[2]").click()
                time.sleep(1)
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]").click()
                time.sleep(2)
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div").click()
                print('Hoàn thành nhập kho.')
                print('Xử lý kết thúc:', time.asctime(
                    time.localtime(time.time())))
                erorr_msg = 'Hoàn thành nhập kho.'
        except:
            erorr_msg = self.driver.find_element(
                By.XPATH, "//div[@class='pop_mesage_cont']").text
            print(erorr_msg)
        finally:
            return erorr_msg

    def mes_30940003(self, slog):
        # Tự động tạo yêu cầu xuất vật liệu.
        time.sleep(2)
        self.driver.get(str(self.ip + '#/tabs/30940003'))
        time.sleep(5)
        # Choosee Storage Location
        self.driver.find_elements(
            By.XPATH, "//tr/th[contains(text(),'Kho công đoạn') or contains(text(),'MM MATERIAL CODE')]//parent::tr/td[1]/div/a")[0].click()
        storage_loc = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[3]/div/div[2]/div[1]/input")
        storage_loc.send_keys("2201")
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[3]/div/div[2]/a[2]/i").click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[3]/div/div[3]/div/div/div/div[4]/div[2]/div/div[1]/div[3]").click()
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[3]/div/div[5]/div/div[2]/span").click()

        # Add More Material
        # Read Excel File.
        path = r"C:\Users\Admin\Desktop\PRD_100_Material List_ 220926.xlsx"
        data = pd.read_excel(path)
        data.columns = data.columns.str.replace(" ", "_")
        for index, row in data.iterrows():
            try:
                print(row.MATNR)
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[3]/div[2]/span").click()  # Add Line
                # Material
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[4]/div/div/div/div[4]/div[2]/div/div[1]/div[5]/div[2]").click()
                material = self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[6]/div/div[2]/div[1]/input")
                time.sleep(1)
                material.send_keys(str(row.MATNR))
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[6]/div/div[2]/a[2]/i").click()
                time.sleep(0.5)
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[6]/div/div[3]/div/div/div/div[4]/div[2]/div/div[1]/div[1]").click()
                self.driver.find_element(
                    By. XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[6]/div/div[5]/div/div[2]/span").click()
                time.sleep(0.5)
                qty = self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[4]/div/div/div/div[4]/div[2]/div/div[1]/div[10]")
                qty.click()
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[1]/div/section/div/div/div[3]/div/div[2]/div[2]/div[4]/div/div/div/div[4]/div[2]/div/div[1]/input").send_keys(str(row.QTY))
            except:
                continue
        # Export Result
        dt = datetime.now()  # Get Current Time.
        file_name = '\MES_30940003' + '_' + \
            dt.strftime('%Y%m%d-%H%M%S') + '.xlsx'
        path = os.getcwd()+file_name
        print("**** Path of current directory:", path)


# if __name__ == "__main__":
#     rpa = RPA_MES('http://10.12.40.3/', 'hav1', '1')
#     data = pd.read_excel(r"C:\Users\Admin\Desktop\8100005015.XLSX").astype(str)
#     rpa.mes_login()
#     rpa.mes_tab('30930001')
#     msg = []
#     time_start = []
#     time_end = []

#     for index, row in data.iterrows():
#         print("******\n Bắt đầu: " ,row.MATERIAL, time.asctime( time.localtime(time.time()) ))
#         gettime = datetime.now()
#         time_start.append(gettime.strftime('%Y%m%d-%H%M%S'))
#         msg.append(rpa.mes_30930001(row.MATERIAL ,row.INBOUND,row.SLOG, row.LOC, row.QTY))
#         print(msg[index])
#         gettime = datetime.now()
#         time_end.append(gettime.strftime('%Y%m%d-%H%M%S'))
#     tmp = pd.DataFrame({
#             'START': time_start,
#             'END': time_end,
#             'MSG': msg,
#         })
#     df = pd.concat([data, tmp], axis=1)
#     dt = datetime.now() 
#     row.TIME = dt.strftime('%Y%m%d-%H%M%S')
#     f_combied = 'Aluko_MES_GR' + \
#         '_' + dt.strftime('%Y%m%d-%H%M%S') + '.xlsx'
#     df.to_excel(f_combied, sheet_name='MES_RPA', index=False)
