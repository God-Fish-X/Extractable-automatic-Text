# import gensim
#
# model = gensim.models.Word2Vec.load("word2vec2")
#
# result = model.wv.most_similar(u'南京')
# for each in result:
#     print (each[0],each[1])
# print()

#测试训练后的模型

from gensim.models import word2vec

model = word2vec.Word2Vec.load(u'./train_test_x/word2vec2')

result = model.wv.__getitem__('软件')
print("软件：",result)

similar = model.wv.similarity(u'南京',u'上海')
print("南京与上海的相似度为：",similar)

similar = model.wv.similarity(u'太原',u'上海')
print("太原与合肥的相似度为：",similar)

print("与'计算机'最相近的单词")
result = model.wv.most_similar(u'计算机',topn=20)
for each in result:
    print(each)
print()