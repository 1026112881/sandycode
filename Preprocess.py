import io

vocabfile="vocab.txt"
outputfile="qk.evaluation.ctf"

qi=0
ki=1

vocab={}

for line in open(vocabfile):
	line=line.strip()
	ls=line.split('\t');
	vocab[ls[0]]=int(ls[1])

outf=open(outputfile,'w')

def word2triletter(word):
	"convert word to triletter codes dictionary"
	word="#"+word+"#"
	wd={}
	for i in range(0,len(word)-3+1):
		if vocab.keys().__contains__(word[i:i+3])==False:
			continue
		ind=vocab[word[i:i+3]]
		if wd.keys().__contains__(ind)==True:
			wd[ind]=wd[ind]+1
		else:
			wd[ind]=1
	return wd

def mergeDic(dic1,dic2):
	""
	dic3=dic1.copy()
	for (k,v) in dic2.items():
		if dic3.keys().__contains__(k)==True:
			dic3[k]=dic3[k]+v
		else:
			dic3[k]=v
	return dic3

def dssmcode(sentence):
	dic={}
	for word in q.split(' '):
		dic_t=word2triletter(word)
		dic=mergeDic(dic,dic_t)
	return dic

def cdssmcode

for line in open("hrs_update.288.tsv"):
	line=line.strip()
	ls=line.split('\t')
	q=ls[qi]
	k=ls[ki]
	dic={}
	for word in q.split(' '):
		dic_t=word2triletter(word)
		dic=mergeDic(dic,dic_t)
	#print(dic)


