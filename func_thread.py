import threading
import time
<<<<<<< HEAD
from selenium import webdriver
import pandas as pd
import numpy as np

def rpa_selenium(l):
	print('Dang chay luong',l)
	time.sleep(1)
	# Get Chorme Version
	# chrome://version/
	options = webdriver.ChromeOptions()
	options.add_argument('--user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data')
	options.add_argument('--profile-directory=Profile 1')
	options.add_argument('--app=https://vn.aluko.com/')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	options.add_argument("headless") # Run in background
	driver = webdriver.Chrome(executable_path=r'dist\Lib\chromedriver.exe', chrome_options=options)

	# # Set Windows Size
	# driver.set_window_size(300,500) 
	# # Set Location Windows
	# x = l*300
	# y = 10
	# driver.set_window_rect(x,y,300,500)

	for index, row in data_split[l].iterrows():
		print(index +1, row.MATERIAL, row.QTY)
		print("\n------")

soluong = 7

data = pd.read_excel(r"C:\Users\Admin\Desktop\ZMMI0021.xlsx").astype(str)
data_split = np.array_split(data,int(soluong))
threads_selenium = []

start = time.time()
for l in range(soluong):
	threads_selenium += [threading.Thread(target=rpa_selenium, args={l},)]
for t in threads_selenium:
	t.start()
for t in threads_selenium:
	t.join()
end = time.time()
print (f'Ket Thuc {round(end-start,2)} second')
=======


def runtest(x):
	print('Dang chay luong',x)
	time.sleep(5)

soluong = 4
threads = []
for x in range(soluong):
	t = threading.Thread(target=runtest, args={x},)
	t.start()
for t in threads:
	t.join()

print('Ket thuc luong chinh')
>>>>>>> ff12ee7f6f868df0f7af348ed8d50530d3bb1ab7
