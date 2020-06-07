# Extractable-automatic-Text
    使用三种方法实现中文抽取式自动文摘，分别是TextRank算法、MMR（最大边界相关算法）算法和TextRank+Word2vec方法；最后使用Rouge评价方法，将生成的摘要和标准摘要进行比较，输出p、r、f值。       
  
    本项目中删去了中文语料库以及训练好的Word2vec词向量，下载好项目后，只需将处理过的中文语料库放在chinese_corpus中，然后使用word_text和train_text对语料库进行训练，生成的词向量放在train_test_x即可。

    具体方法可参考我在CSDN的博客，地址是https://blog.csdn.net/qq_41215527/article/details/104207505

    本项目有个新想法是Word2vec+TextRank算法是基于TextRank算法的，而TextRank算法有其自身的缺陷，那就是提取摘要句时，只关注分数的大小，而不关注提取出的摘要句之间有何种联系，这也就导致提取出的摘要句虽然分数高，但很可能说的是同一个意思，这就大大降低了提取出的摘要的多样性，而本文中的MMR算法考虑到了摘要多样性这一问题，所以如果可以将MMR算法的思想加入到Word2vec+TextRank的算法中，将会提高Word2vec+TextRank算法提取摘要的多样性。

    其中的45篇小论文，包括三种摘要方法生成的摘要、标准摘要和各摘要方法生成的摘要的p、r、f值
