import os,sys,re

LOCAL=False
if os.path.exists('D:\\vimstuff'):
	LOCAL=True
if LOCAL:
	sys.stdout=open('out.txt','w')


if __name__ == '__main__':
	d1 = {'a': 100, 'b': 200, 'c':300}
	d2 = {'a': 300, 'b': 200, 'd':400}
	hsh={}
	for keys in d1:
		hsh[keys]=d1[keys]
	for keys in d2:
		if hsh.get(keys)!=None:
			hsh[keys]+=d2[keys]
		else:
			hsh[keys]=d2[keys]
	print(hsh)
