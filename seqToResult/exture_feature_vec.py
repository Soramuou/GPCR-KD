from extract_word import can_translate


# 提取一条序列的特征向量
def extract_feature_of_a_seq(seq, features):
    vector = []
    for feature in features:
        count = 0
        for start in range(len(seq) - len(feature)):
            end = start + len(feature)
            if can_translate(feature, seq[start:end]):
                count += 1
        vector.append(count)
    return vector
