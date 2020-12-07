import os

count = 0
# 读取所有数据
def read_all_data():
    data_of_each_family = dict()
    for dir_name,  _, all_file in os.walk("./new_data"):
        for filename in all_file:
            if 1:
                famliy_name = filename.split(".")[0]
                path = os.path.join(dir_name, filename)
                data_of_a_family = read_a_family(path)
                data_of_each_family[famliy_name] = data_of_a_family
    return data_of_each_family


# 读取一个家族的数据
def read_a_family(path):
    data_of_a_family = []
    with open(path) as f:
        for row in  f.readlines():
            if len(row) > 0 and row[0] != '>':
                data_of_a_family.append(row.strip("\n"))
                global count
                count += 1
    return data_of_a_family
