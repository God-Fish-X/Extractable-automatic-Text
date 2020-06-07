#word2vec模型训练

from gensim.models import word2vec
import logging

logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)
sentences_one = word2vec.LineSentence('chinese_corpus/cut_zh_wiki.txt')
#sentences_two = word2vec.LineSentence(u'./cut_zh_wiki_01.txt')
model_one = word2vec.Word2Vec(sentences_one,size=200,window=10,min_count=64,sg=1,hs=1,iter=10,workers=25)
#model_two = word2vec.Word2Vec(sentences_two,size=200,window=10,min_count=64,sg=1,hs=1,iter=10,workers=25)
model_one.save(u'./train_test_x/word2vec2')
#model_one.wv.save_word2vec_format(u'./w2v',binary=False)
#model_two.save(u'./word2vec2')

# import logging
# import multiprocessing
# import os.path
# import sys
# import jieba
#
# from gensim.models import Word2Vec
# from gensim.models.word2vec import PathLineSentences
#
# if __name__ == '__main__':
#     # 日志信息输出
#     program = os.path.basename(sys.argv[0])
#     logger = logging.getLogger(program)
#     logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
#     logging.root.setLevel(level=logging.INFO)
#     logger.info("running %s" % ' '.join(sys.argv))
#
#     input_dir = u'./cut_zh_wiki_00.txt'
#     outp1 = 'baike.model'
#     outp2 = 'word2vec_format'
#     #fileNames = os.listdir(input_dir)
#     # 训练模型
#     # 输入语料目录:PathLineSentences(input_dir)
#     # embedding size:256 共现窗口大小:10 去除出现次数5以下的词,多线程运行,迭代10次
#     model = Word2Vec(PathLineSentences(input_dir),size=200, window=10, min_count=64,sg=1,hs=1,workers=multiprocessing.cpu_count(), iter=10)
#     model.save(outp1)
#     model.wv.save_word2vec_format(outp2, binary=False)