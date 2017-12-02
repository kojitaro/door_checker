#!/usr/bin/env python
# coding: UTF-8

from serial import *
import sys
import twelite


def parse(line):
    if line[0] != ":":
        return
    
    line = line[1:]
    data = twelite.parse_readdata(line)
    print(data)


def main(port):
# シリアルポートを開く
    try:
        ser = Serial(port, 115200)
        print("open serial port: %s" % port)
    except:
        print("cannot open serial port: %s" % port)
        exit(1)

    while True:
        line = ser.readline().rstrip()
        parse(line)


if __name__ == '__main__':
    port = sys.argv[1]
    main(port)
