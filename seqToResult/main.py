import time
import pickle
import threading

from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import numpy as np
from collections import defaultdict

from read_data import read_all_data
from extract_word import extract_feature
from exture_feature_vec import extract_feature_of_a_seq


all_family_data = read_all_data()
sum_num = 0
for data in all_family_data.values():
    sum_num += len(data)
print(time.ctime(),":", "数据总量：",sum_num)
features = extract_feature(all_family_data)
dict_feature = {}
for feature in features:
    if len(feature) in dict_feature.keys():
        dict_feature[len(feature)] +=1
    else:
        dict_feature[len(feature)] = 1
print(sorted(dict_feature.items(), key=lambda d: d[0], reverse=False))
print(features, len(features))

family_names ={}
mutex = threading.Lock()
def get_data():
    x = []
    y = []
    for i, (family_name, family_data) in enumerate(all_family_data.items()):
        family_names[i] = family_name
        for seq in family_data:
            x.append(extract_feature_of_a_seq(seq, features))
            y.append(i)
    return x, y


def classifier_factory(classifier_name):
    if classifier_name == "MLPClassifier":
        return MLPClassifier(hidden_layer_sizes=(2000,2000), max_iter=1000)
    elif classifier_name == "SVC":
        return SVC()
    elif classifier_name =="RandomForestClassifier":
        return RandomForestClassifier()
    elif classifier_name == "GaussianNB":
        return GaussianNB()

def preprocess(x):
    X_train = preprocessing.scale(np.array(x))
    return X_train


def classifier(x, y):
    clf = classifier_factory(SVC)
    clf.fit(x, y)
    return clf


print(time.ctime(), ":", '开始处理数据!')
x, y = get_data()

print(time.ctime(), ":", 'len(x): {}, len(y): {}, len(x[0]): {}', len(x), len(y), len(x[0]))
print(time.ctime(), ":", '开始写入数据到文件!')
with open("data", 'wb') as f:
    pickle.dump(family_names,f)
    pickle.dump(x,f)
    pickle.dump(y,f)
print(time.ctime(), ":", '写入数据完毕, 开始预处理!')
x = preprocess(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

try:
    print(time.ctime(), ":","训练数据数量：", len(x_train))
    print(time.ctime(), ":","预测数据数量：", len(x_test))
except Exception as e:
    print(time.ctime(), ":","读取长度失败：", e)

print(time.ctime(), ":", "开始训练!")
clf = classifier(x_train, y_train)
print(time.ctime(), ":", "开始预测!")
result = clf.predict(x_test)
print(time.ctime(), ":", "预测完毕, 开始写入结果!")
count = 0

with open('./result.txt', 'w') as f:
    for y, r in zip(y_test, result):
        if y != r:
            f.write("应分到{}, 结果{}\n".format(family_names[y], family_names[r]))
            count += 1
    print(1 - count / len(result), file=f, end='\n')


# 不同精度
# 不同分类器
# 不同类别
# 不同替换矩阵