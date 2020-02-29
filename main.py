#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import os
import random
import requests
import sys
sys.setrecursionlimit(1000000000)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/72.0'
}

def parse_audio():
    while True:
        global ebobocore
        ebobocore = 1
        num = '6' + str(random.randrange(1111, 9999))
        num2 = str(random.randrange(111, 999)) + ".wav"
        pizdec = num + num2
        url = "http://static.donationalerts.ru/audiodonations/" + num + '/' + num + num2
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            aaa(url, ebobocore)
        else:
            return parse_audio()

def aaa(url, ebobocore):
    if os.path.exists('audio/' + str(ebobocore) + "_EboboCore.wav"):
        ebobocore += 1
        return aaa(url, ebobocore)
    else:
        print(str(ebobocore) + " voice donations downloaded")
        path = os.path.join('audio', f'{str(ebobocore) + "_EboboCore.wav"}')
        with open(path, 'wb') as f:
            f.write(requests.get(url, headers=headers).content)


if __name__ in '__main__':
    if os.path.exists('audio'):
        parse_audio()
    else:
        os.mkdir('audio')
        parse_audio()
