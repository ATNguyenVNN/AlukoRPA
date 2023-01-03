from pyrfc import Connection, ABAPApplicationError, ABAPRuntimeError, LogonError, CommunicationError
import pandas as pd
import re
import numpy as np


class SAP_RFC():
    def __init__(self):
        # PRD 100
        ASHOST = '100.100.0.114'
        CLIENT = '100'
        SYSNR = '00'
        USER = 'AMMP35'
        PASSWD = 'Dua@2022@'

        # # ALP 500
        # ASHOST = '100.100.0.113'
        # CLIENT = '500'
        # SYSNR = '50'
        # USER = 'AMMP35'
        # PASSWD = 'Dua@2022@'
        self.conn = Connection(ashost=ASHOST, sysnr=SYSNR,
                               client=CLIENT, user=USER, passwd=PASSWD)

    def query(self, Fields, SQLTable, Where='', MaxRows=50, FromRow=0):
        """A function to query SAP with RFC_READ_TABLE"""

        # By default, if you send a blank value for fields, you get all of them
        # Therefore, we add a select all option, to better mimic SQL.
        if Fields[0] == '*':
            Fields = ''
        else:
            Fields = [{'FIELDNAME': x} for x in Fields]  # Notice the format

        # the WHERE part of the query is called "options"
        options = [{'TEXT': x} for x in Where]  # again, notice the format
        print(options)

        # we set a maximum number of rows to return, because it's easy to do and
        # greatly speeds up testing queries.
        rowcount = MaxRows
        try:
            # Here is the call to SAP's RFC_READ_TABLE
            tables = self.conn.call('RFC_READ_TABLE',
                                    QUERY_TABLE=SQLTable,
                                    DELIMITER='|',
                                    FIELDS=Fields,
                                    OPTIONS=options,
                                    ROWSKIPS=FromRow, ROWCOUNT=MaxRows)
        # We split out fields and fields_name to hold the data and the column names
        except CommunicationError:
            print("Could not connect to server.")
            raise
        except LogonError:
            print("Could not log in. Wrong credentials?")
            raise
        except (ABAPApplicationError, ABAPRuntimeError):
            print("An error occurred.")
            raise
        fields = []
        fields_name = []

        data_fields = tables["DATA"]  # pull the data part of the result set
        # pull the field name part of the result set
        data_names = tables["FIELDS"]

        headers = [x['FIELDNAME'] for x in data_names]  # headers extraction
        long_fields = len(data_fields)  # data extraction
        long_names = len(data_names)  # full headers extraction if you want it

        # now parse the data fields into a list
        for line in range(0, long_fields):
            fields.append(data_fields[line]["WA"].strip())

        # for each line, split the list by the '|' separator
        fields = [x.strip().split('|') for x in fields]

        # return the 2D list and the headers
        df = pd.DataFrame(fields, columns=headers)
        return df

    def table_header(self,fiels):
        # fields = ['ROLLNAME', 'SCRTEXT_S']
        # table = 'DD04T'
        # value = ["MANDT", "LIFNR", "LAND1", "NAME1", "NAME2", "NAME3",
        #          "NAME4", "ORT01", "ORT02", "PFACH", "PSTL2", "PSTLZ", "REGIO", "SORTL"]
        where = []

        for index, line in enumerate(fiels):
            if index == 0:
                where.append(
                    "DDLANGUAGE = 'EN' AND ROLLNAME = " + "'" + line+"'")
                continue
            where.append(
                "OR DDLANGUAGE = 'EN' AND ROLLNAME = " + "'" + line+"'")

        # Get Header in Table.
        df_header = self.query(['ROLLNAME', 'SCRTEXT_S'],'DD04T', where, 0, 0)
        # print(df_header['SCRTEXT_S'].values.tolist())
        return df_header['SCRTEXT_S'].values.tolist()
