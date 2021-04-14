import json
import requests
import os
import subprocess
file_place = input("enter file path : ")

def bashout(text):
    output = subprocess.check_output(text, shell=True)
    output = output.decode("utf-8")
    return output

#server = requests.get('https://apiv2.gofile.io/getServer')
server = bashout('curl https://apiv2.gofile.io/getServer')
server = json.loads(server)
server = server['data']['server']

upload_url = 'curl -F email=khadem13khadem@gmail.com -F file=@'+file_place+' https://'+server+'.gofile.io/uploadFile'

download_url = bashout(upload_url)
download_url = json.loads(download_url)
download_url = download_url['data']['code']
#print('https://gofile.io/d/'+download_url)
print('\033[93m' + 'https://gofile.io/d/'+download_url + '\033[0m' )
