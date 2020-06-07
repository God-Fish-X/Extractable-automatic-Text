# -*- coding: utf-8 -*-
import chardet
f = open('some_words_train.txt','rb')# 要有"rb"，如果没有这个的话，默认使用gbk读文件。
data = f.read()
print(chardet.detect(data))
f.close()