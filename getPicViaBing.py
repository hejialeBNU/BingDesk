import urllib2
import urllib
import datetime
import os
try:
    import xml.etree.cElementTree as ET
except:
    import xml.etree.ElementTree as ET

#init some parameters
today = datetime.datetime.now().strftime('%Y%m%d')
thisyear = datetime.datetime.now().strftime('%Y')
bg_size = "1920x1080"
local_path = "E:/background_imgs/"
bingUrl = "http://www.bing.com"

#get xml data from bing.com XML
response = urllib2.urlopen("http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1")
xml = response.read()
response.close()

#Formate XML
treeRoot = ET.fromstring(xml)

#formate url and local paths
urlBase =  bingUrl + treeRoot.find("image").find("urlBase").text
nameBase = urlBase.split("/")[-1]
local_name = local_path + today + "_" + nameBase.split("_")[0] + "_" + bg_size + ".jpg"
bg_url = urlBase + "_" + bg_size + ".jpg"

#download bg image
if not os.path.exists(local_name):
    #get description of the pic
    copyright = treeRoot.find("image").find("copyright").text
    try:
        #insert copyright string into the front of the TXT file, CodeType Attention
        #touch a new file for a new year
        if not os.path.exists(local_path + "copyrights_" + thisyear +".txt"):
            file = open(local_path + "copyrights_" + thisyear +".txt",'a')
            file.close()
            #linux/unix can use os.mknod command instead of lines above for touching a new file

        #read the old file into MEM
        file = open(local_path + "copyrights_" + thisyear +".txt",'r')
        before = file.read()
        file.close()

        #insert the new line into the head off the old file string
        line = str(today) + ":\t" + copyright + "\n"
        after = line.encode("utf-8") + before

        #rewrite the old copyright file
        file = open(local_path + "copyrights_" + thisyear +".txt",'w')
        file.write(after)
        file.close()

        #download bing bg image
        urllib.urlretrieve(bg_url, local_name)
    except:
        print "download pic failed"
else:
    pass


