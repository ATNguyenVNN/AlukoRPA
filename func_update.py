import requests, os, sys, subprocess

def updateCheck():
    update = False
    path = ("{0}\{1}".format(os.getcwd(), 'Aluko RPA.exe'))
    print (path)
    # Gets downloaded version
    versionSource = open(r'dist\IMG\version.txt', 'r')
    versionContents = versionSource.read()
    print(versionContents)

    #gets newest version
    updateSource = requests.get("https://raw.githubusercontent.com/ATNguyenVNN/Aluko_Projects/master/dist/IMG/version.txt")
    updateContents = str(updateSource.content)[2:7]
    print(str(updateContents))
    #checks for updates
    if updateContents == versionContents:
        update = False
        return update     
try:
    if updateCheck() == "True":
        # Write new version
        versionSource = open(r'dist\IMG\version.txt', 'w')
        versionSource.write("updateContents")
        versionSource.close()
except:
    pass

