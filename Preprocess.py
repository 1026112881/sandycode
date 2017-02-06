import io

def load_vocab(filename):
	vocab={}
	c=1
	for line in open(filename):
		line=line.strip()
		ls=line.split('\t');
		vocab[ls[0]]=int(c)
		c+=1
	return vocab

def word2triletter(word,vocab):
	"convert word to triletter codes dictionary"
	word="#"+word+"#"
	wd={}
	for i in range(0,len(word)-3+1):
		#if vocab.keys().__contains__(word[i:i+3])==False:
		if word[i:i+3] not in vocab:
			continue
		ind=vocab[word[i:i+3]]
		#if wd.keys().__contains__(ind)==True:
		if ind in wd:
			wd[ind]=wd[ind]+1
		else:
			wd[ind]=1
	return wd

def mergeDic(dic3,dic2):
	""
	#dic3=dic1.copy()
	for (k,v) in dic2.items():
		if k in dic3:
			dic3[k]=dic3[k]+v
		else:
			dic3[k]=v
	return dic3

def dssmcode(sentence,vocab):
	"dssmcode: return dssm triletter code"
	dic={}
	for word in sentence.split(' '):
		dic_t=word2triletter(word,vocab)
		dic=mergeDic(dic,dic_t)
	return dic

def cdssmcode(sentence,vocab):
	"cdssmcode: return sequence of triletter codes"
	seq=[]
	for word in sentence.split(' '):
		dic_t=word2triletter(word,vocab)
		seq.append(dic_t)
	return seq

def dic2str(dic):
	"convert dic to cntk format input string"
	s=""
	for (k,v) in dic.items():
		s+=str(k)+":"+str(v)+" "
	return s

def TriLetter_LSTM():
	vocabfile="vocab.txt"
	outputfile="qk.evaluation.2.ctf"
	inputfile="D:/MS/data/hrs_update.288.tsv"
	qi=0
	ki=1
	vocab=load_vocab(vocabfile)
	outf=open(outputfile,'w')

	#Convert CDSSM Input
	count=1
	for line in open(inputfile):
		line=line.strip()
		ls=line.split('\t')
		q='# '+ls[qi]+' #'
		k='# '+ls[ki]+' #'
		q_seqcodes=cdssmcode(q,vocab)
		k_seqcodes=cdssmcode(k,vocab)

		q_len=len(q_seqcodes)
		k_len=len(k_seqcodes)

		length=max(q_len,k_len)

		for i in range(0,(int)(length)):
			outf.write(str(count)+" ")
			if i<q_len:
				outf.write("|Q "+dic2str(q_seqcodes[i])+" ")
			if i<k_len:
				outf.write("|K "+dic2str((k_seqcodes[i]))+" ")
			if i==0:
				outf.write("|L 1")
			outf.write("\n")

		count+=1
		if count%10000==0:
			print(count)
		#print(dic)
	outf.close()

	#Covert DSSM Input
	# for line in open(inputfile):
	# 	line=line.strip()
	# 	ls=line.split('\t')
	# 	q=ls[qi]
	# 	k=ls[ki]
	# 	codes=dssmcode(q)
	# 	outf.write(dic2str(codes)+"\n")
	# 	#print(dic)
	# outf.close()

def triletterCount():
	vocabfile="vocab.txt"
	outputfile="qk.evaluation.ctf"
	inputfile="D:/MS/data/QK.ClkGt1.txt"
	qi=0
	ki=1
	vocab=load_vocab(vocabfile)
	outf=open(outputfile,'w')

	#Convert CDSSM Input
	count=0
	dic={}
	for line in open(inputfile):
		line=line.strip()
		ls=line.split('\t')
		q=ls[qi]
		k=ls[ki]
		codes=dssmcode(q,vocab)
		dic=mergeDic(dic,codes)
		count+=1
		if count%100000==0:
			c=0
			print("-------------------------------------------------")
			for key, value in sorted(dic.iteritems(), key=lambda (k,v): (-1*v,k)):
				c+=1
				if c==11:
					print("...")
				if c>10 and c<1139:
					continue
				if c>1149:
					break
				print "%s: %s" % (key, value)


TriLetter_LSTM()