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

# タッチされたあとの次の待受時間
TIME_WAIT = 5
API_URL = 'https://ancient-woodland-85036.herokuapp.com/raspi'
log_path = '/var/log/nfc.log'

def post_nfc(idm,ent_time):
    assert type(idm) == str
    assert type(ent_time) == str

    send_msg = ent_time + 'に'
    print('post:',idm,send_msg)
    # print(idm,ent_time,file=open(log_path, 'a+'))
    # with open(log_path, mode='a') as f:
    #     f.write('\nnfc:'+idm+ent_time)

    response = requests.post(
        API_URL,
        json.dumps({'nfc':idm,'msg':send_msg}),
        headers={'Content-Type': 'application/json'})
    pprint.pprint(response)



def main():
    clf = nfc.ContactlessFrontend('usb')
    print('nfc_reader init finish , NFC waiting...')
    # USBに接続されたNFCリーダに接続してインスタンス化
    while True:
        target = clf.sense(nfc.clf.RemoteTarget('212F'))
        if target is not None:
            tag = nfc.tag.activate(clf, target)
            # print(tag)

            if tag.TYPE == 'Type3Tag':
                idm = tag.identifier.hex()
                ent_time = (datetime.datetime.now().strftime('%m月%d日 %H:%M'))
                # print(idm,ent_time)
                # print()
                post_nfc(idm,ent_time)
                print('idm',idm,datetime.datetime.now(),file=open(log_path, 'a+'))

                time.sleep(TIME_WAIT)
                print('ready for read !!')
            else:
                print(tag+'\n read but Only Type3Tag is supported now.')

    clf.close()


print('aaa')


if __name__ == "__main__":
    sys.stdout = open('/dev/console', 'w')
    print('nfc_reader run',datetime.datetime.now(),file=open(log_path, 'a+'))
    print('start nfc !!')
    main()