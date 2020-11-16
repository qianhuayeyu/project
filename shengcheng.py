import os
import random
trainval_percent = 0.86 #trainval占整个数据集的百分比，剩下部分就是test所占百分比
train_percent = 0.8 #train占trainval的百分比，剩下部分就是val所占百分比
xmlfilepath = r'C:\Users\1\Desktop\nongzuowu\VOCdevkit\VOC2007\Annotations'
txtsavepath = r'C:\Users\1\Desktop\nongzuowu\VOCdevkit\VOC2007\ImageSets\Main'
total_xml = os.listdir(xmlfilepath)
num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)
ftrainval = open(r'C:\Users\1\Desktop\nongzuowu\VOCdevkit\VOC2007\ImageSets\Main/trainval.txt', 'w')
ftest = open(r'C:\Users\1\Desktop\nongzuowu\VOCdevkit\VOC2007\ImageSets\Main/test.txt', 'w')
ftrain = open(r'C:\Users\1\Desktop\nongzuowu\VOCdevkit\VOC2007\ImageSets\Main/train.txt', 'w')
fval = open(r'C:\Users\1\Desktop\nongzuowu\VOCdevkit\VOC2007\ImageSets\Main/val.txt', 'w')
for i  in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
       ftest.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest .close()

