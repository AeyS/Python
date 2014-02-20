#coding: utf-8

def filepath(fp,mothod=False):
	#将文件保存的路径做一个预处理，已给出路径调用时只需填写文件名即可！
	if fp=='xh':
		path='D:/临时/ali/'+fp+'.txt'
	elif fp=='jg':
		path='D:/临时/ali/'+fp+'.txt'
	elif '/' in fp:
		path = fp
	else:
		path='D:/临时/ali/pump/'+fp+'.txt'
	uipath = unicode(path, "utf8")
	f2=judge_file(uipath, mothod)
	return f2,uipath

def Copywt():
	'''Copy text written to file.'''
	#关键词重复写入n遍到文件里
	path=raw_input('filepath:')
	result = []
	while True:
		con=raw_input('please:')
		if con == '': break
		nx=raw_input('sum:')
		for x in xrange(0,int(nx)):
			result.append('%s\n' % con)
	wlist(result, path, True)

def judge_file(path,mothod):
	'''If have old file,del old file,creatr new file.

		mothod = a+,w [and so on...]
		return file handle'''
	if mothod == False: mothod = 'a+'
	elif mothod == True: raise IOError('Must is a+,w [and so on...]')
	#获取文件路径，及文件名。
	import os
	dirname,filename=os.path.split(path)
	if os.path.isdir(dirname)==False: os.makedirs(dirname)
	if os.path.isfile(path):
		os.remove(path)
	else:
		print 'This is new file!  >>" %s "' % path
	f1=open(path,mothod)
	return f1

def getlines(files,start,end=False):
	'''Gets the specified row.

		files = a list
		start = start rows
		end = end rows'''
	getline = []
	if type(files) != list: raise TypeError('Parameter 1 not a list')
	if end is False: end=start+1
	for line in files[start:end]:
		getline.append(line)
	return getline

def wlist(list_a,ad,overflow=False,mothod=False):
	#将列表写入文档
	def wt(list,f):
		for x in xrange(0,len(list)):
			f.writelines(list[x])
		return x
	f2,path=filepath(ad,mothod)
	overflows = ''
	n = wt(list_a,f2)
	if overflow:
		Exdo = open('Exdo.txt','r').readlines()
		overflows = getlines(Exdo,1)
		f2.write(overflows[0])
		overflows = '\n>>Add endlines\t%s' % unicode(overflows[0] , "gbk")
		n += 1
	f2.close()
	print 'Generate %s line: %d %s' % (path, n, overflows)


def del_BL(list):
	#删除空白行
	list_a=[]
	for i in [line for line in list if len(line)>2]:
		if len(i.replace('"',''))>2: list_a.append(i)
	return list_a

def judge_key(list,w=0):
	#处理列表里的带数字关键词,judge pump have sum,if have jump out
	#0 flist是返回一个关键词里含数字除外的列表
	#2 flist_list是返回一个抛弃所有包含关键词的列表
	#1 flist_t是将被剔除的内容写入以用来判断的关键词命名的文档
	judge_key=raw_input('judge_key:')
	flist=[]
	flist_t=[]
	flist_list=[]
	w=int(w)
	key = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
	for line in [line for line in list if len(line)>3]:
		if judge_key in line:
			if [k for k in key if k in line]:
				print "%s Have Sum" % judge_key
				flist_t.append(line)
				break
			print "%s Not Sum" % judge_key
			flist.append(line)
			flist_t.append(line)
		else:
			flist.append(line)
			flist_list.append(line)

	if w is 1:
		print 'w=%s Get Single Keyword Mode' % w
		wlist(flist_t,'d:/name_%s.txt' % judge_key)
	elif w is 2:
		print 'w=%s Discard single keyword mode' % w
		return flist_list
	else:
		print 'w=%s In addition to figures contain keywords' % w
		return flist
	
'''************************************'''

def list_del_list(list_a,list_b):
	#提供价格列表，坐参考删除型号列表内容及几个列表自身的内容
	#list_b需要处理的文件，list_a用来对比的文件
	path_xh='D:/file_contrast.txt'
	path_jg='D:/file_handle.txt'
	sum_list=[]
	jg_list=[]
	n_jg=0
	for x in list_a:
		if len(x) <3:
			#以长度小于3来判断‘/’空白项的位置，并收集在sum_list里
			sum_list.append(n_jg)
			print n_jg,x,
		else:
			#这份价格列表就剔除了‘/’空白项
			jg_list.append(x)
		n_jg+=1
	n=0
	for k in sum_list:
		#这份型号列表就剔除了‘/’空白项，因为每删除一项，列表总数就减少1，所以删除一项的位置就得通过-n次来获取。
		k=k-n
		del list_b[k]
		print 'del%s' % k
		n+=1
	wlist(jg_list,path_jg)
	wlist(list_b,path_xh)

def split_h(f):
	path=raw_input('path:')
	var=raw_input('split(...):')
	location_sum=raw_input('location_sum:')
	result = []
	for i in f:
		content=i.split(var)[int(location_sum)]
		result.append('%s\n' % content.replace('\n',''))
	wlist(result,path)
