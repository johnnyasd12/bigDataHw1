import pandas
import time
import numpy
#from numpy import *
from sklearn.ensemble import ExtraTreesClassifier

start_time=time.clock()
encodings = ['Big5','utf-8-sig','utf-8','latin-1','windows-1250','windows-1252']
#============使用編碼 (windows超愛big5跟utf8(BOM)
e = 'utf-8'
'''
for e in encodings: #偵測文件編碼,必要時啟用
	try: #encoding
		df = pandas.read_csv(self.ipath,encoding=e,converters={'Source':str,'Destination':str})
		fh = open(fname,'r',encoding=e)
		fh.readlines()
		fh.seek(0)
	except UnicodeDecodeError:
		print('got unicode decode error with %s, trying different coding..' % e)
	else:
		print('opening the file with encoding: %s' % e)
		break
'''
#read Data
#trainPath = ("dataset/train/largeTrain.csv")
trainPath = ("largeTrain.csv")
df = pandas.read_csv(trainPath,encoding=e,converters={'Class':str})
print("read training data time: %s sec"%(time.clock()-start_time))

#get X(feature content) and Y(target content)
X=numpy.array(df.drop('Class',axis=1))#X is features so we delete the Class column
Y = numpy.array(df['Class'])
forest = ExtraTreesClassifier(n_estimators=250,random_state=0)							  
forest.fit(X,Y)
importances = forest.feature_importances_
std = numpy.std([tree.feature_importances_ for tree in forest.estimators_],axis=0)#???????
indices = numpy.argsort(importances)[::-1]

featureNames = list(df.columns.values)#feature list
# Print the feature ranking
print("Feature ranking:")
# print first 10 features
print("The most useful features: ")
for f in range(10):
	print("%d. feature%d:\t%s (%f)" % (f + 1, indices[f], featureNames[indices[f]], importances[indices[f]]))
#print last 10 features
print("\nThe least useful features: ")
for f in range(X.shape[1]-10,X.shape[1]):
	print("%d. feature%d:\t%s (%f)" % (f + 1, indices[f], featureNames[indices[f]], importances[indices[f]]))

	
print('entire program took %s seconds' % (time.clock()-start_time))
