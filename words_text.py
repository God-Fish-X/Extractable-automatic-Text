# _*_ coding:utf-8 _*_

#对经过分词以后的维基百科中文语料库进行去除停用词处理

import jieba
import codecs
import re

file_chinese = codecs.open('chinese_corpus/cut_zh_wiki.txt',"a+",'utf-8')
stopwordslist = [line.strip() for line in open('stopwords.txt',encoding='utf-8').readlines()] #创建停用词列表


# for line in open("chinese_corpus/zh_wiki",'r',encoding='utf-8'):
#     for i in re.sub('[a-zA-Z0-9]', '', line).split(' '):
#         if i != '':
#             data = list(jieba.cut(i, cut_all = False))
#             readline = ' '.join(data) + '\n'
#             file_chinese_one.write(readline)
# file_chinese_one.close()
#去除停用词
# file_chinese_two = codecs.open('chinese_corpus/cut_zh_wiki.txt',"a+",'utf-8')
# for line in open("chinese_corpus/cut_zh_wiki_00.txt","r",encoding='utf-8'):
#     for i in re.sub('[a-zA-Z0-9]','',line).split(' '):
#         if i != '':
#             data = list(jieba.cut(i,cut_all=False))
#             outstr = ''
#             for word in data:
#                 if word not in stopwordslist:
#                     if word != '\t':
#                         outstr += word
#                         outstr += " "
#             file_chinese_two.write(outstr + '\n')
#
# file_chinese_two.close()
#
for line in open("chinese_corpus/zh_wiki","r",encoding='utf-8'):
    for i in re.sub('[a-zA-Z0-9]','',line).split(' '):
        if i != '':
            data = list(jieba.cut(i,cut_all=False))
            outstr = ''
            for word in data:
                if word not in stopwordslist:
                    if word != '\t':
                        outstr += word
                        outstr += " "
            file_chinese.write(outstr + '\n')

file_chinese.close()