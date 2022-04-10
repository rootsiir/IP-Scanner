from time import sleep
import requests
import json

#BU SCRİPT TAMAMEN ROOTSİİR TARAFINDAN YAZILMIŞ OLUP BLACK POETRY ADINA YAZILMIŞTIR. KODLARI DEĞİŞTİRMEMENİZ RİCA OLUNUR.

banner = (""" ____  _            _      ____            _
| __ )| | __ _  ___| | __ |  _ \ ___   ___| |_ _ __ _   _
|  _ \| |/ _` |/ __| |/ / | |_) / _ \ / _ \ __| '__| | | |
| |_) | | (_| | (__|   <  |  __/ (_) |  __/ |_| |  | |_| |
|____/|_|\__,_|\___|_|\_\ |_|   \___/ \___|\__|_|   \__, |
                                                    |___/""")
print(banner)
print("""[Welcome to Ip Scanner Tool]

[Discord] - [rootsiir#3334]
[Github] - [github.com/rootsiir]""")
ip = input("\n[IP Adress]:")
ipurl = ("http://ip-api.com/json/"+ip)
result = requests.get(ipurl)
result = json.loads(result.text)
ülke = result['country']
ülkekodu = result['countryCode']
plaka = result['region']
şehir = result['city']
posta = result['zip']
isp = result['isp']
saat = result['timezone']
as1 = result['as']
ipadresi = result['query']
gps1 = result['lat']
gps2 = result['lon']
konum = (gps1,gps2)
print("Scanning..")
sleep(1.5)
print("\nIP = ",ipadresi)
sleep(0.4)
print("Ülke = ",ülke)
sleep(0.4)
print("Şehir = ",şehir)
sleep(0.4)
print("Posta Kodu = ",posta)
sleep(0.4)
print("ISP = ",isp)
sleep(0.4)
print("Konum = ",konum)
sleep(0.4)
print("Ülke Kodu = ",ülkekodu)
sleep(0.4)
print("Plaka = ",plaka)
sleep(0.4)
print("Zaman dilimi = ",saat)
sleep(0.4)
print("AS = ",as1)