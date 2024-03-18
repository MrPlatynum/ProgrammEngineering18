#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('file2.txt', 'r') as fileptr:
        content = fileptr.readlines()
        print(content)
