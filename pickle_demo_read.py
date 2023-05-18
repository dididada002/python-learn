# -*- coding: UTF-8 -*-
# pickle模块:序列和反序列化

import pprint,pickle

pkl_file = open('data.pk1','rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()