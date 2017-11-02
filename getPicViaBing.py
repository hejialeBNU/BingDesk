import urllib2
import urllib
import datetime
try:
    import xml.etree.cElementTree as ET
except:
    import xml.etree.ElementTree as ET

#init some parameters
today = datetime.datetime.now().strftime('%Y%m%d')
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
urllib.urlretrieve(bg_url, local_name)



