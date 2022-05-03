# import xml.etree.ElementTree as et
import defusedxml.ElementTree as et
import os
from urllib.request import urlopen

# file = urlopen("https://login.microsoftonline.com/{os.environ.get('ARM_TENANT_ID')}/federationmetadata/2007-06/federationmetadata.xml?appid=<app_id>")
# data = file.read()
# file.close()
# # xml_doc = et.parse(data)
# # xml_root = xml_doc.getroot()
# xml_root = et.fromstring(data)
# xml_string = et.tostring(xml_root, encoding="unicode", method="xml")
# print(xml_string)

# thing = "test"
# url = f"l;kadjf/{thing}\
# /stuff"

# print(url)

url = f"https://login.microsoftonline.com/{os.environ.get('ARM_TENANT_ID')}/federationmetadata/2007-06/federationmetadata.xml?appid=<app_id>"
xml_file = urlopen(url)
xml_data = xml_file.read()
xml_file.close()
# xml_root = et.fromstring(xml_data)
# self.xml_string = et.tostring(xml_root, encoding="unicode", method="xml")
parser = et.DefusedXMLParser()
xml = et.XML(xml_data, parser)
xml_string = et.tostring(xml)
print(type(xml_string))