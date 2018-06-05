#!/usr/bin/python3

import configparser

print("===Config parset test===")
config = configparser.RawConfigParser()
config.readfp(open(r'./config.ini'))
test1 = config.get('Test', 'test1')
print(test1)
test2 = config.get('Test', 'test2')
print(test2)
