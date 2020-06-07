#首先使用pip安装rouge
from pprint import pprint
import perl
from pyrouge import Rouge155
from rouge import Rouge
from rouge import FilesRouge
import os,json
#将语料文件中的数据转换成[中文:ID]的形式存储到json文件中
from tqdm import tqdm

min_count = 0
if os.path.exists('seq2seq_config.json'):
    chars,id2char,char2id = json.load(open('seq2seq_config.json'))
    # id2char = {int(i):j for i,j in id2char.items()}
else:
    with open("train_test_x/word2vec2",'r',encoding='utf-8') as f:
        titleList = f.readlines()
    chars = {}
    for singleTitle in titleList:
        for w in tqdm(list(singleTitle)): # 纯文本，不用分词
            chars[w] = chars.get(w,0) + 1
    #字符：数量
    chars = {i:j for i,j in chars.items() if j >= min_count}
    id2char = {i:j for i,j in enumerate(chars)}
    char2id = {j:i for i,j in id2char.items()}
    json.dump([chars,id2char,char2id], open('seq2seq_config.json', 'w'))

def str2id(s):
    #char2id 字符-id
    # 文字转整数id
    maxlen = len(s);
    ids = [char2id.get(c, 1) for c in s[:maxlen]]
    return ids

#将语料转成ID的形式
def dealData(hyp_path,ref_path,new_hyp_path,new_ref_path):
    with open(hyp_path,'r',encoding='utf-8') as f:
        data = f.readlines();
    charIDs = list();
    for item in data:
        charID = str2id(item);
        charID = [str(x) for x in charID]
        charIDs.append(charID);
    with open(new_hyp_path,'a',encoding='utf-8') as f:
        for item in charIDs:
            f.write(" ".join(item)+"\n");
    with open(ref_path,'r',encoding='utf-8') as f:
        data = f.readlines();
    charIDs = list();
    for item in data:
        charID = str2id(item);
        charID = [str(x) for x in charID];
        charIDs.append(charID);
    with open(new_ref_path,'a',encoding='utf-8') as f:
        for item in charIDs:
            f.write(" ".join(item)+"\n");

#hyp_path是程序给出的摘要，ref_path是标准的摘要
def getRouge(hyp_path,ref_path):
    files_rouge = FilesRouge()
    rouge = Rouge()
    #files_rouge = Rouge155()
    # or
    #scores = rouge.get_scores(hyp_path,ref_path,avg=True)
    scores = files_rouge.get_scores(hyp_path,ref_path,avg=True)
    pprint(scores)

if __name__ == '__main__':
    f1 = open('system1.txt', "r+")
    f1.truncate()
    f1.close()
    f2 = open('reference1.txt', "r+")
    f2.truncate()
    f2.close()
    dealData('system.txt','reference.txt','system1.txt','reference1.txt')
    getRouge('system1.txt','reference1.txt')

	# 存有中文的文件
	# system.txt 程序给出摘要
	# reference.txt 标准摘要
	# 中文转存为ID的文件
	# system1.txt
	# reference1.txt
