# -*- coding: utf-8 -*-
import binascii
import nfc
import time
from threading import Thread, Timer

import pprint
import json
import requests

import datetime
import sys
from pyfiglet import Figlet

# タッチされたあとの次の待受時間
TIME_WAIT = 5
SLACK_API_URL = 'https://ancient-woodland-85036.herokuapp.com/raspi'
FLASK_API_URL = 'sum:url/record'
log_path = '/var/log/nfc.log'


def render_big_msg(msg):
    f = Figlet(font="big")
    msg = f.renderText(msg)
    print(msg)
    # return msg

def post_nfc(url,idm,send_msg):
    assert type(idm) == str
    assert type(send_msg) == str
    
    print('post:',idm,send_msg)
    # print(idm,ent_time,file=open(log_path, 'a+'))
    # with open(log_path, mode='a') as f:
    #     f.write('\nnfc:'+idm+ent_time)

    response = requests.post(
        url,
        json.dumps({'nfc':idm,'msg':send_msg}),
        headers={'Content-Type': 'application/json'})
    pprint.pprint(response)



def main():
    clf = nfc.ContactlessFrontend('usb')
    print('nfc_reader init finish')
    render_big_msg('NFC waiting...')
    # USBに接続されたNFCリーダに接続してインスタンス化
    while True:
        target = clf.sense(nfc.clf.RemoteTarget('212F'))
        if target is not None:
            tag = nfc.tag.activate(clf, target)
            # print(tag)

            if tag.TYPE == 'Type3Tag':
                idm = tag.identifier.hex()

                time_now = datetime.datetime.now()
                send_msg = time_now.strftime('%m月%d日 %H:%M')+'に'

                print('idm',idm,time_now,file=open(log_path, 'a+'))
                post_nfc(SLACK_API_URL,idm,send_msg)
                # post_nfc(FLASK_API_URL,idm,'')
                
                time.sleep(TIME_WAIT)
                render_big_msg("READY FOR READING NFC ... ")
            else:
                render_big_msg("OOPS!!!")
                print(tag+'\n read but Only Type3Tag is supported now.')

    clf.close()

if __name__ == "__main__":
    sys.stdout = open('/dev/console', 'w')
    print('nfc_reader run',datetime.datetime.now(),file=open(log_path, 'a+'))
    main()