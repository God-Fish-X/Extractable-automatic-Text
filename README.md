# Extractable-automatic-Text
        使用三种方法实现中文抽取式自动文摘，分别是TextRank算法、MMR（最大边界相关算法）算法和TextRank+Word2vec方法；最后使用Rouge评价方法，将生成的摘要和标准摘要进行比较，输出p、r、f值。         本项目中删去了中文语料库以及训练好的Word2vec词向量，下载好项目后，只需将处理过的中文语料库放在chinese_corpus中，然后使用word_text和train_text对语料库进行训练，生成的词向量放在train_test_x即可。         具体方法可参考我在CSDN的博客，地址是https://blog.csdn.net/qq_41215527/article/details/104207505
