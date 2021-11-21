import os,sys

LOCAL=False
if os.path.exists('D:\\vimstuff'):
	LOCAL=True
if LOCAL:
	sys.stdout=open('out.txt','w')


'''


Solution :

Here there is bruteforce approach of naively checking every pair which will
have
TimeComplexity=O(n*n)
Extra_SpaceComplexity=O(1)

But in order to improve TimeComplexity we can convert dictionary into tuples, we can also use list but tuple processing is faster
So after flatting the dictionaries into tuple we will convert them to set as it is implemented by hashtable it has O(1) lookuptime
unless we don't have high load factor 

Thus using set and tuples we can achieve 
TimeComplexity of O(n) 
Extra_SpaceComplexity of O(n) for storing tuples.


'''


if __name__ == '__main__':
	#Here if command line input is 1 it will ask for custom input
	try:
		custom_inp=sys.argv[1]
	except:
		custom_inp=0
	if custom_inp:
		dict_list=[]
		try:
			key,value=input().split()
			dictionary={}
			if value.isdigit():
				value=int(value)
			dictionary[key]=value
			dict_list.append(dictionary)
		except:
			pass
	else:
		dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]
	tuple_list=[]
	for d in dict_list:
		t=()
		for keys in d:
			t+=(keys,d[keys])
		tuple_list.append(t)
	real_dict_list=[]
	for tuples in tuple_list:
		d={}
		for i in range(0,len(tuples),2):
			d[tuples[i]]=tuples[i+1]
		real_dict_list.append(d)
	print(real_dict_list)