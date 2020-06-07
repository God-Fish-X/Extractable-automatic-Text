import jieba
import math
from string import punctuation
from heapq import nlargest
from itertools import product, count
from gensim.models import word2vec
import numpy as np

model = word2vec.Word2Vec.load("train_test_x/word2vec2")

def cut_sentences(sentence):
    #以。！？.为结束符，对文章进行分割
    puns = frozenset(u"'。") #返回一个冻结的集合
    tmp = []
    for ch in sentence:
        tmp.append(ch) #逐字遍历文章并添加到tmp中
        if puns.__contains__(ch): #如果遇到句子结束符
            yield  ''.join(tmp) #将结束符拼接到tmp，并返回
            tmp = []
    yield ''.join(tmp)

def create_stopwords():
    stop_list = [line.strip() for line in open("stopwords.txt", 'r', encoding='utf-8').readlines()] #去除首尾空格，创建停用词列表
    return stop_list

def cosine_similarity(vec1, vec2):#余弦相似度
    #计算两个向量之间的余弦相似度
    tx = np.array(vec1)
    ty = np.array(vec2)
    cos1 = np.sum(tx * ty)
    denom = np.linalg.norm(tx) * np.linalg.norm(ty)
    cosine_value = cos1/denom
    #print(vec1+vec2+cosine_value)
    return cosine_value

def compute_similarity_by_avg(sents_1,sents_2):#计算simsiarity
    #两个句子之间的相似度
    if len(sents_1) == 0 or len(sents_2) == 0:
        return 0.0
    if sents_1[0] not in model:
        vec1 = 0
    else:
        vec1 = model[sents_1[0]]
    for word1 in sents_1[1:]:
        if word1 in model:
            vec1 = vec1 + model[word1]
    if sents_2[0] not in model:
        vec2 = 0
    else:
        vec2 = model[sents_2[0]]
    for word2 in sents_2[1:]:
        if word2 in model:
            vec2 = vec2 + model[word2]

    similarity = cosine_similarity(vec1 / len(sents_1), vec2 / len(sents_2))
    return similarity

def calculate_score(weight_graph,scores,i):#TextRank公式
    #句子权重计算
    length = len(weight_graph)
    d = 0.85
    added_score = 0.0
    for j in range(length):
        fraction = 0.0
        denominator = 0.0
        #计算分子
        fraction = weight_graph[j][i] * scores[j]
        #计算分母
        for k in range(length):
            denominator += weight_graph[j][k]
            if denominator == 0:
                denominator = 1
        added_score += fraction / denominator
    #计算最终分数
    weighted_score = (1 - d) + d * added_score
    return weighted_score

def different(scores,old_scores):#出口
    #判断前后分数有无变化
    flag = False
    for i in range(len(scores)):
        if math.fabs(scores[i] - old_scores[i]) >= 0.0001:
            flag = True
            break
    return flag

def weight_sentences_rank(weight_graph):#迭代计算句子分数
    #句子排序
    #初始分数设置为0.5
    scores = [0.5 for _ in range(len(weight_graph))]
    old_scores = [0.0 for _ in range(len(weight_graph))]
    #开始迭代
    while different(scores,old_scores):
        for i in range(len(weight_graph)):
            old_scores[i] = scores[i]
        for i in range(len(weight_graph)):
            scores[i] = calculate_score(weight_graph,scores,i)
    return scores

# def filter_model(sents,model):
#     #过滤模型中没有的词或者停用词
#     stopwords = create_stopwords() + ['。', ' ', '.']
#     total = []
#     for sentence_i in sents:
#         sentence_list = []
#         for word_j in sentence_i:
#             if model.wv.__contains__(word_j) or word_j not in stopwords:
#                 sentence_list.append(word_j)
#         total.append(sentence_list)
#     return total

def filter_model(sents):#过滤器
    _sents = []
    for sentence in sents:
        for word in sentence:
            if word not in model:
                sentence.remove(word)
        if sentence:
            _sents.append(sentence)
    return _sents

def create_graph(word_sent):#建图
    #传入句子链表  返回句子之间相似度的图
    num = len(word_sent[0])
    board = [[0.0 for _ in range(num)] for _ in range(num)]
    for i, j in product(range(num), repeat=2):
        if i != j:
            compute_similarity = compute_similarity_by_avg(word_sent[0][i],word_sent[0][j])
            board[i][j] = compute_similarity
    return board


def summarize(text,n):
    tokens = cut_sentences(text)
    sentences = []
    sents = []
    for sent in tokens:
        sentences.append(sent)
        sents.append([word for word in jieba.cut(sent) if word])
    #sents = filter_model(sents,model)
    sents = filter_model(sents)
    graph = create_graph(sents)
    scores= weight_sentences_rank(graph)
    sent_selected = nlargest(n,zip(scores,count()))
    sent_index = []
    for i in range(n):
        sent_index.append(sent_selected[i][1])
    return [sentences[i] for i in sent_index]

