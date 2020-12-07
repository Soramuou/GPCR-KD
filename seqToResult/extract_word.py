from functools import lru_cache

from read_config import CONFIG, AMINO_ACID, REPLACE_MATRIX
from collections import defaultdict
from my_heap import heap


# 提取所有特征
def extract_feature(data_of_all_family):
    result = set()
    features = []
    family_nums = len(data_of_all_family)

    all_feature_seqs = extract_all_word(data_of_all_family)  # 提取所有满足条件的特征序列
    all_main_seqs = extract_all_main_seq(all_feature_seqs)  # 提取所有主序列
    return list(all_main_seqs)


# 提取所有子序列 -- 返回set
def extract_all_word(data_of_all_family):
    seqs = []
    for family_name, family_data in data_of_all_family.items():
        if len(family_data) <= 3:
            continue
        seqs += list(extract_one_feature(family_data))

    # 去除识别性的的序列,并返回结果
    return remove_low_seq(seqs, len(data_of_all_family))

# 去除识别性低的序列--已测试
def remove_low_seq(feature_seqs, seqs_num):
    seqs_set = set(feature_seqs)
    will_remove = []
    for seq in seqs_set:
        if feature_seqs.count(seq) >= seqs_num * CONFIG.b:
            will_remove.append(seq)
    for seq in will_remove:
        seqs_set.remove(seq)

    return seqs_set

# 提取一个类别的所有子序列--返回set--已测试
def extract_one_feature(data):
    result = set()
    sites = []
    position = []

    # 提取满足条件的位点
    for i in range(len(min(data,key=len))):
        record = defaultdict(int)
        for sequence in data:
            record[sequence[i]] += 1
        max_site = max(record, key=record.get)
        max_num = record[max_site]
        if max_num >= len(data) * CONFIG.a and max_site != '-':
            sites.append(max_site)
            position.append(i)

    # 将连续的位点组合为序列
    start,end = 0, 0
    for i in range(1,len(position)):
        if position[i] - position[i-1] == 1:
            end += 1
        else:
            if end-start+1 >= CONFIG.min_lens:
                result.add("".join(sites[start:end+1]))
            start, end = i, i
    return result


# 提取所有主序列
def extract_all_main_seq(all_feature_seqs):
    # 首先将所有特征序列按长度分组
    feature_seqs_by_len = defaultdict(list)
    for seq in all_feature_seqs:
        feature_seqs_by_len[len(seq)].append(seq)

    all_main_seqs = []
    for _, seqs in feature_seqs_by_len.items():
        all_main_seqs += extract_main_seq(seqs)
    return all_main_seqs


# 提取固定长度的主序列
def extract_main_seq(k_len_seqs):
    # 首先将序列按照是否可以相互转化分组
    groups = split_group(k_len_seqs)

    # 提取每一组的主序列
    main_seqs = set()
    for group in groups:
        main_seq = max(group, key=cal_pm)
        main_seqs.add(main_seq)
    return main_seqs


# 将相同长度的子序列分组
def split_group(same_len_word):
    result = []
    used = set()
    same_len_word = set(same_len_word)
    for word in same_len_word:
        if word not in used:
            group = {word}
            for replace_word in same_len_word:
                if can_translate(word, replace_word):
                    group.add(replace_word)
            used.add(word)
            result.append(group)
    return result


# 判断是否可相互转化
@lru_cache()
def can_translate(f_word, s_word):
    for i in range(len(f_word)):
        if f_word[i] == '-' or s_word[i] == '-':
            continue
        if get_trans_rate(f_word[i], s_word[i]) < 0:
            return False
    if cal_SM(f_word, s_word) < CONFIG.T:
        return False
    return True


# 两个氨基酸的转化率
def get_trans_rate(f_aa, s_aa):
    try:
        if f_aa == "-" or s_aa == "-" or f_aa == "X" or s_aa == "X":
            return 0
        f_index = AMINO_ACID.index(f_aa)
        s_index = AMINO_ACID.index(s_aa)
        return REPLACE_MATRIX[f_index][s_index]
    except Exception:
        return 0


# 计算Pm
def cal_pm(word):
    product = 1
    for aa in word:
        product *= cal_p(aa)
    return 1 - product


# 计算P, 计算Pm的中间步骤
def cal_p(aa):
    positive_sum = 0
    for another_aa in AMINO_ACID:
        rate = get_trans_rate(aa, another_aa)
        if rate > 0:
            positive_sum += rate
    return get_trans_rate(aa, aa) / positive_sum


def cal_SP(M1, M2):
    return cal_SM(M1, M2) / cal_SM(M1, M1)


def cal_SM(M1, M2):
    return sum(get_trans_rate(M1[i], M2[i]) for i in range(len(M1)))


# 查询功能相同的子序列, 返回一个列表, 列中中的每项为相应Index的可以转化的氨基酸
def search_same_word(word):
    result = []
    for aa in word:
        same_aa = {another_aa for another_aa in AMINO_ACID if get_trans_rate(
            aa, another_aa) >= 0}
        result.append(same_aa)
    return result


if __name__ == "__main__":
    data = [
        "RLYIEQKTNLPALNRFC",
        "RLYIEQKTNLPALNRFC",
        "RLYLQQKTGTAPLGRLC",
        "RLYIEQKTTLPALNRFC",
        "RLYIEENTSWAKLDSSC",
        "RLYIEQKKSMAAFNRFC",
    ]
    print(extract_one_feature(data))

    print(remove_low_seq([1, 1, 1, 1,2,2,2,3,4,4], 4))
