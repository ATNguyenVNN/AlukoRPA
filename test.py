import urllib.request
with urllib.request.urlopen('https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx') as ex_vcb:
    data = ex_vcb.read().decode('utf-8')
    for line in data.split('\n'):
        if line.find("<DateTime>") >0:
            get_time = line[line.find("<DateTime>")+ 10:line.find("</DateTime>")]
        if str(line).find("AUD") > 0:
            tranfer = float(line[line.find('Transfer="')+10:line.find('" Sell="')].replace(",",""))
            sell = float(line[line.find('" Sell="')+8:line.find('" Sell="')+17].replace(",",""))
            ex_usd = (tranfer+sell)/2
            break
    print(ex_usd, get_time)
