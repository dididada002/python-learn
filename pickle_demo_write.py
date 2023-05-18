# -*- coding: UTF-8 -*-
# pickle模块:序列和反序列化
import pickle

data1 = {'a':[1,2.0,3,4+6j],'b':('string',u'Unicode string'),'c':None}
selfref_list = [1,2,3]
selfref_list.append(selfref_list)
output = open('data.pk1', 'wb')
pickle.dump(data1,output)
pickle.dump(selfref_list,output,-1)
output.close()