# GUI测试用

import os
import tkinter
import tkinter.messagebox
from tkinter.filedialog import askdirectory
from urllib.parse import quote
from urllib import request
import re
import time


def selectPath():
    path_ = askdirectory()
    path.set(path_)

def butonck():
    lujin=path.get()

    if lujin == '' or lujin == None:
        t2='路径不能为空，请选择一个路径！'
        tkinter.messagebox.showinfo('友情提示', t2)
        return False
    if os.path.exists(str(lujin)):
        pass
    else:
        os.mkdir(str(lujin))

    keyword=zhanghao.get()
    num=mima.get()
    if keyword == '' or keyword == None:
        keyword='火影'
    if num == '' or keyword == None:
        num=30
    tt='图片保存在桌面的img文件夹，现在开始爬取。。。'
    tkinter.messagebox.showinfo("友情提示", tt)
    pachong(keyword,num,lujin)

def pachong(keyword='火影',num='30',lujin=''):
    # 处理中文关键字
    kw = quote(keyword)
    num=str(num)
    qs = '1'
    lj = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&fp=result&queryWord=" + kw + "=utf-8&oe=utf-8&copyright=&word=" + kw + "&pn=" + qs + "&rn=" + num

    # 定义头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    # 发送请求百度图片链接
    req = request.Request(url=lj, data=None, headers=headers, method='GET')
    response = request.urlopen(req)
    xinxi = response.read()
    xx = xinxi.decode(encoding='utf-8')
    # wj = open('linshi.txt', 'w', encoding='utf-8')
    # wj.write(str(xx))
    ll = re.findall('middleURL":".*?jpg', str(xx))
    arr = []
    for var in ll:
        rr = re.findall('https.*?jpg', var)
        arr.append(rr)
    nn = 1


    for ii in arr:
        aa = ii[0]
        time.sleep(2)
        request.urlretrieve(aa, filename= str(lujin)+'\img'+str(nn)+'.jpg')
        nn += 1
    tkinter.messagebox.showinfo("郑重提示", '爬取完成！！！')



# 创建窗口
obj=tkinter.Tk()
# 窗口的标题
obj.title('wocao百度图片')

# 窗口尺寸
obj.geometry("600x250")

#窗口基于屏幕的坐标 +x轴+y轴
# obj.geometry("+200+200")

# 创建lab标签
labelx=tkinter.Label(obj,text="输入关键字", fg="red", font=("宋体", 20),padx=30, pady=10)

# 显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
labelx.grid(row=0,column=0)

# 创建输入框
zhanghao=tkinter.StringVar()
entryx= tkinter.Entry(obj, text="输入关键字",font=("宋体", 20),textvariable=zhanghao)
zhanghao.set('火影')
entryx.grid(row=0, column=1)

tkinter.Label(obj,text='默认：火影').grid(column=2,row=0)


# 创建第二个lab标签
labelx2=tkinter.Label(obj, text="输入爬取量",fg="red", font=("宋体", 20), padx=30, pady=10)

# 显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
labelx2.grid(row=2,column=0)


# 创建第二个输入框
mima=tkinter.StringVar()
entryx2= tkinter.Entry(obj, text="输入爬取量",font=("宋体", 20),textvariable=mima)
mima.set('30')
entryx2.grid(row=2, column=1)

tkinter.Label(obj,text='默认：30张').grid(column=2,row=2)

# 创建第三个lab标签
labelx3=tkinter.Label(obj, text="选择存放路径",fg="red", font=("宋体", 20), padx=30, pady=10)
labelx3.grid(row=3,column=0)
path = tkinter.StringVar()

tkinter.Entry(obj, text="",font=("宋体", 20), textvariable = path).grid(row = 3, column = 1)
#选择路劲按钮
tkinter.Button(obj, text = "路径选择", command = selectPath).grid(row = 3, column = 2)


# 创建按钮
bt = tkinter.Button(obj, text="确定", font=("宋体", 25), padx=20, command=butonck)


#显示按钮
bt.grid(row=4, column=1)
# tkinter.Label(obj,text='小爬虫体验，这里是一个文字标签！！！').grid(column=1,row=5)

# 消息循环 显示窗口
obj.mainloop()

