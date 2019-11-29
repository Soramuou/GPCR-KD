import time
import pickle

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
import sklearn.naive_bayes as nb
import numpy as np
from collections import defaultdict
import analysize


def preprocess(x):
    X_train = preprocessing.scale(np.array(x))
    return X_train


def classifier(x, y):
    clf = MLPClassifier(hidden_layer_sizes=(4000,4000), max_iter=1000)
    # clf = SVC()
    #clf = RandomForestClassifier()
    # clf = GaussianNB()
    clf.fit(x, y)
    return clf

print(time.ctime(), ":" ,'开始读取数据!')
with open("gds_data", 'rb') as f:
    family_names = pickle.load(f)
    x = pickle.load(f)
    y = pickle.load(f)
print(time.ctime(), ":" ,'读取完毕, 开始预处理!')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
x_train = preprocess(x_train)

try:
    print(time.ctime(), ":","训练数据数量：", len(x_train))
    print(time.ctime(), ":","预测数据数量：", len(x_test))
except Exception as e:
    print(time.ctime(), ":","读取长度失败：", e)

test_num = len(x_test)

print(time.ctime(), ":" ,"开始训练!")
clf = classifier(x_train, y_train)
print(time.ctime(), ":" ,"开始预测!")
result = clf.predict(preprocess(x_test))
print(time.ctime(), ":" ,"预测完毕, 开始写入结果!")
count = 0

with open('./result.txt', 'w') as f:
    for y, r in zip(y_test, result):
        if y != r:
            f.write("应分到{}, 结果{}\n".format(family_names[y], family_names[r]))
            count += 1
    print(1 - count / len(result), file=f, end='\n')

analysize.main(test_num)

# 不同精度
# 不同分类器
# 不同类别
# 不同替换矩阵
