from tkinter import *
import MMR

def run():
    txt = txtone.get("0.0",'end')
    with open("test.txt","w",encoding = 'utf-8') as f :
        f.write(txt)
    with open("test.txt", "r", encoding='utf-8') as njuptcs:
        txt = [line.strip() for line in open("test.txt", "r",encoding='utf-8').readlines()]
        text = njuptcs.read().replace('\n', '')
    print ('原文为：')
    for i in txt:
        print (i)
    summarize_text = MMR.summarize(text,3)
    #summarize_text = textrank.summarize(text,5)
    print ('摘要为：')
    #ing = 0
    for i in summarize_text:
        #ing += 1
        #txttwo.insert('end',ing)
        #txttwo.insert('end','、')
        txttwo.insert('end',i)
        txttwo.insert('end','\n')
        #print (ing,i)
    txttwo.insert('end', '\n')

#初始化Tk()
myWindow = Tk()
myWindow.minsize(830,480)
#设置标题
myWindow.title('论文摘要自动生成系统(MMR)')
#标签控件布局
Label(myWindow, text = "输入文本",font = ('微软雅黑 12 bold')).grid(row = 0,column = 0)
Label(myWindow, text = "输出摘要",font = ('微软雅黑 12 bold')).grid(row = 0,column = 2)
#Entry控件布局
entry1=Entry(myWindow)
txtone = Text(entry1)
txtone.pack()
entry2=Entry(myWindow)
txttwo = Text(entry2)
txttwo.pack()
entry1.grid(row = 0, column = 1)
entry2.grid(row = 0, column = 3)
#Quit按钮退出；Run按钮打印计算结果
Button(myWindow, text='退出',command = myWindow.quit, font = ('微软雅黑 12 bold')).grid(row = 1, column = 3,sticky = S,padx = 20,pady = 20)
Button(myWindow, text='运行',command = run, font = ('微软雅黑 12 bold')).grid(row = 1, column = 1, sticky = S, padx = 20,pady = 20)
#进入消息循环
myWindow.mainloop()