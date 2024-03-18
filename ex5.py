#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('newfile.txt', 'x') as fileptr:
        print(fileptr)

        if fileptr:
            print('File create successfully')
