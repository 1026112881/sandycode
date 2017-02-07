import numpy
import sys
from sklearn import metrics
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

def AUC(path):
	Qf= numpy.loadtxt(path+'.qf')
	Df= numpy.loadtxt(path+'.df')
	s=10000

	Qf2=Qf**2
	Df2=Df**2

	Qf2S=(Qf2.sum(axis=1)**0.5)
	Df2S=(Df2.sum(axis=1)**0.5)

	Qf2S=numpy.dot(Qf2S.reshape(s,1),numpy.ones((1,64)))
	Df2S=numpy.dot(Df2S.reshape(s,1),numpy.ones((1,64)))

	QfN=Qf/Qf2S
	DfN=Df/Df2S

	PositiveScore=(QfN*DfN).sum(axis=1)

	arr=numpy.arange(s)
	numpy.random.shuffle(arr)
	DfN_Shuffle=DfN[arr,:]

	NegativeScore=(QfN*DfN_Shuffle).sum(axis=1)

	Score=numpy.concatenate((PositiveScore,NegativeScore),axis=0)
	Label=numpy.concatenate((numpy.ones((s,1)),0*numpy.ones((s,1))),axis=0)

	fpr, tpr, thresholds = metrics.roc_curve(Label, Score, pos_label=1)

	auc=metrics.auc(fpr, tpr)
	print auc
	return [auc,fpr,tpr]

[auc1,fpr1,tpr1]=AUC('./Data/Result/Validation10K')
[auc2,fpr2,tpr2]=AUC('./Data/Result/Validation10K_neg5')
[auc3,fpr3,tpr3]=AUC('./Data/Result/Validation10K_neg5_binary')
[auc4,fpr4,tpr4]=AUC('./Data/Result/Validation10K_neg5_binary_1')

plt.figure(1)
plt.gca().set_color_cycle(['red', 'green', 'blue', 'gray'])
plt.plot(fpr1,tpr1)
plt.plot(fpr2,tpr2)
plt.plot(fpr3,tpr3)
plt.plot(fpr4,tpr4)

ax = plt.gca()
plt.legend(['P:N=1:1', 'P:N=1:5','Binary'], loc='lower right')

ax.grid()
plt.show()