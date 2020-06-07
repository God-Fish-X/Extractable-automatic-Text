import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import operator

# 停止词
stopwords = [line.strip() for line in open("stopwords.txt", 'r', encoding='utf-8').readlines()]

def cut_sentences(sentence):
    #以。！？.为结束符，对文章进行分割
    puns = frozenset(u'。') #返回一个冻结的集合
    tmp = []
    for ch in sentence:
        tmp.append(ch) #逐字遍历文章并添加到tmp中
        if puns.__contains__(ch): #如果遇到句子结束符
            yield  ''.join(tmp) #将结束符拼接到tmp，并返回
            tmp = []
    yield ''.join(tmp)

def cleanData(name):
    setlast = jieba.cut(name, cut_all=False)
    seg_list = [i.lower() for i in setlast if i not in stopwords]
    return " ".join(seg_list)

def calculateSimilarity(sentence, doc):  # 根据句子和句子，句子和文档的余弦相似度
    if doc == []:
        return 0
    vocab = {}
    for word in sentence.split():
        vocab[word] = 0  # 生成所在句子的单词字典，值为0
    docInOneSentence = '';
    for t in doc:
        docInOneSentence += (t + ' ')  # 所有剩余句子合并
        for word in t.split():
            vocab[word] = 0  # 所有剩余句子的单词字典，值为0
    cv = CountVectorizer(vocabulary=vocab.keys())
    docVector = cv.fit_transform([docInOneSentence])
    sentenceVector = cv.fit_transform([sentence])
    return cosine_similarity(docVector, sentenceVector)[0][0] #余弦相似度

sentences = []
clean = []
originalSentenceOf = {}

def dic (texts):
    parts = cut_sentences(texts)
    #print(parts)
    for part in parts:
        cl = cleanData(part)  # 句子切分以及去掉停止词
        #		print (cl)
        sentences.append(part)  # 原本的句子
        clean.append(cl)  # 干净有重复的句子
        originalSentenceOf[cl] = part  # 字典格式
    setClean = set(clean)  # 干净无重复的句子
    return setClean

scores = {}

# def scores(setClean):
#     for data in clean:
#         temp_doc = setClean - set([data])  # 在除了当前句子的剩余所有句子
#         score = calculateSimilarity(data, list(temp_doc))  # 计算当前句子与剩余所有句子的相似度
#         scores[data] = score  # 得到相似度的列表
# print score
# calculate MMR
alpha = 0.7
summarySet = []

def summarize(text,n):
    sent_index = []
    setClean = dic(text)
    for data in clean:
        temp_doc = setClean - set([data])  # 在除了当前句子的剩余所有句子
        score = calculateSimilarity(data, list(temp_doc))  # 计算当前句子与剩余所有句子的相似度
        scores[data] = score
    while n > 0:
        mmr = {}
        # kurangkan dengan set summary
        for sentence in scores.keys():
            if not sentence in summarySet:
                mmr[sentence] = alpha * scores[sentence] - (1 - alpha) * calculateSimilarity(sentence, summarySet)  # 公式
        selected = max(mmr.items(), key=operator.itemgetter(1))[0]
        summarySet.append(selected)
        #print (summarySet)
        n -= 1
# rint str(time.time() - start)
    i = 1
    for sentence in summarySet:
        print(i,end='')
        print('、',end='')
        print(originalSentenceOf[sentence])
        i += 1
        sent_index.append(originalSentenceOf[sentence])
    return sent_index