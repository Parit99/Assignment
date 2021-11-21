import sys,os,itertools

LOCAL=False
if os.path.exists('D:\\vimstuff'):
	LOCAL=True
if LOCAL:
	sys.stdout=open('out.txt','w')


'''


Solution :

Here generate_sentence function checks for all possible combinations of string of len n
which is O(2^max(n)) max(n) is maximum length among different strings.
we will then count number of brackets in given utterance_list sentence by sentence
than we will traverse through generated combinations and replace it with the brackets in the sentence

If utterance_list has maximum sentence length of m

Then TC=O(2^max(n)*m*no_of_sentence_in_utterance_list)

Better approach is we can use bitmask and also reduce the timecomplexity to lowerbound of O(2^32*m*no_of_sentence_in_utterance_list) if there are combinations with size fits in 32 bits i.e. (4GB)

Here we can also use rasa and identify intent of generated sentence and sentence with brackets and compare their similarities and only keep those which has highest similarity.


'''



def generate_sentence():
	sentences=[]
	for sent in utterance_list:
		brackets=sent.count("<>")
		l=list(itertools.permutations(Entities_list,brackets))
		for k in range(0,len(l)):
			tuples=l[k]
			cnter=0
			string=''
			for i in range(0,len(sent)):
				if i+1<len(sent) and sent[i]=='<' and sent[i+1]=='>':
					string+=tuples[cnter]
					cnter+=1
				elif sent[i]!='>':
					string+=sent[i]
			sentences.append(string)
	return sentences

if __name__ == '__main__':
	Entities_list=["kolkata", "delhi"]
	utterance_list=["How far is <> from <>", "How is the weather in <>"]
	print(*generate_sentence(),sep="\n")

