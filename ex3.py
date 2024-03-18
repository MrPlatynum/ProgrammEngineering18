#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('file2.txt', 'r') as fileptr:
        content1 = fileptr.readline()
        content2 = fileptr.readline()

        print(content1, end='')
        print(content2)
