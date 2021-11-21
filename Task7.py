import os,sys,re

LOCAL=False
if os.path.exists('D:\\vimstuff'):
	LOCAL=True
if LOCAL:
	sys.stdout=open('out.txt','w')

'''


Solution :

Bruteforce is to check wether string has
Timecomplexity=O(len(string))
Extra_SpaceComplexity=O(26+10+len(special_characters))

Better Solution is to use regex in order to reduce space complexity
as special_charracters may vary so 
TimeComplexity=O(len(string))
Extra_SpaceComplexity=O(1)


'''

if __name__ == '__main__':
	#Here if command line input is 1 it will ask for custom input
	try:
		custom_inp=sys.argv[1]
	except:
		custom_inp=0
	if custom_inp:
		string=input()
	else:
		string='aA@123[\]{|}'
	exp = ('''^(?=.*[a-z])(?=.''' +
             '''*[A-Z])(?=.*\\d)''' +
             '''(?=.*[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]).+$''')
	check=re.compile(exp)
	if(re.search(check,string) and len(string)>=6 and len(string)<=16):
		print('Valid Password')
	else:
		print('Invalid Password')
