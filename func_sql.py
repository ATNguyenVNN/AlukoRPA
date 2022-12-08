import os , sys, platform, cx_Oracle, xlsxwriter
from datetime import time, datetime
import pandas as pd
class MES_DB():
       def __init__(self) -> None:
              super().__init__()      
       def DB_connect(self,host,port):
              try:
                     self.host = host
                     self.port = port
                     path_lib = os.getcwd()+"Lib\Windows"
                     if platform.system() == "Darwin":
                            lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
                                   "instantclient_19_8")
                            cx_Oracle.init_oracle_client(lib_dir=lib_dir)          
                     elif platform.system() == "Windows":
                            cx_Oracle.init_oracle_client(lib_dir=path_lib)
              except Exception as err:
                     print(err)

       def DB_query(self,sql_query):
              # Configure Database.
              self.dsn_tns = cx_Oracle.makedsn(self.host, self.port , service_name='MESDB') 
              self.db = cx_Oracle.connect(user='Aluko', password='mesmgr', dsn=self.dsn_tns)
              self.sql_query = sql_query
              self.cursor = self.db.cursor()
              self.cursor.execute(self.sql_query)
              df = pd.DataFrame(self.cursor.fetchall())
              df.columns = [x[0] for x in self.cursor.description]
              df.fillna(value="", inplace=True)
              return df
       def DB_export(self):
              # Create Excel File Name:
              dt = datetime.now()
              # Get Table Name:            
              table = self.sql_query[self.sql_query.find("FROM ")+5:self.sql_query.find("WHERE")-1]
              print("**** Table Name is :", table)
              file_name = '\MES_' + str(table)+ '_' + dt.strftime('%Y%m%d-%H%M%S') + '.xlsx'
              self.path = os.getcwd()+file_name
              print("**** Path of current directory:", self.path)
              # Starting Write DB to Excel
              workbook = xlsxwriter.Workbook(self.path)
              sheet = workbook.add_worksheet()
              # Connect DB using Query
              col_names = [row[0] for row in self.cursor.description]
              # Get database
              
              for r, row in enumerate(self.cursor.fetchall()):
                     for c, col in enumerate(row):
                            sheet.write(r+1, c, col)
                            
              for cols, header in enumerate(col_names):
                     sheet.write(0,cols, header)
              workbook.close()
              self.cursor.close()
              return self.path
