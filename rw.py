# coding: utf-8
import os
import sys
import re
import Average_sorting
'''****************Private********************
	BL = blanklines
'''
def __list_del_BL_group(list):
	#剔除空行，并将关键词合并
	key_list=[]
	nn=0
	for x in list:
		n=len(x)
		if n<2:
			pass
		elif nn%2==0:
			text=x.replace('\n','')+' '
		else:
			#计算关键词的长度，如果过长将被拆分成两句！
			if len(text+x)>35:
				key_list.append('%s\n%s' % (text,x))
			else:
				key_list.append(text+x)
		nn+=1
	return key_list

def __list_w(list,f):
	n=0
	for i in list:
		f.write(i)
		print i,
		n+=1
	return n

def filepath(fp,var=False):
	#将文件保存的路径坐一个预处理，调用时只需填写文件名即可！
	if fp=='xh':
		path='D:/临时/ali/'+fp+'.txt'
	elif fp=='jg':
		path='D:/临时/ali/'+fp+'.txt'
	else:
		path='D:/临时/ali/pump/'+fp+'.txt'
	uipath = unicode(path , "utf8")
	f2=__judge_file(uipath)
	return f2,path

def wr():
	#关键词重复*遍写入到文件
	f,path=filepath(raw_input('filepath:'))
	n=0
	while True:
		con=raw_input('please:')
		if con in'close':
			f.close()
			break
		nx=raw_input('sum:')
		f.write('%s\n' % con*int(nx))
		n=n+int(nx)
	print 'Generate %s line: %d' % (path, n)

def __judge_file(path):
	'''del old file,creatr new file.'''
	#获取文件路径，及文件名。
	dirname,filename=os.path.split(path)
	if os.path.isdir(dirname)==False:
		os.makedirs(dirname)
	if os.path.isfile(path):
		os.remove(path)
	else:
		print 'This is new file!'
	f1=open(path,'a+')
	return f1

def handle(list_a,ad):
	#将列表写入文档
	f2,path=filepath(ad)
	n=0
	for i in list_a:
		f2.writelines(i)
		n+=1
	f2.close()
	print 'Generate %s line: %d' % (path, n)

def __del_BL(list):
	#删除空白行
	list_a=[]
	for i in list:
		n=len(i)
		if n<2:
			pass
		# elif '/' in i:
		# 	pass
		else:
			i=i.replace('"','')
			if len(i)<2:
				pass
			else:
				list_a.append(i)
	return list_a

def judge_name(list,w=0):
	#处理列表里的带数字关键词,judge pump have sum,if have jump out
	#0 flist是返回一个关键词里含数字除外的列表
	#2 flist_list是返回一个抛弃所有包含关键词的列表
	#1 flist_t是将被剔除的内容写入以用来判断的关键词命名的文档
	judge_name=raw_input('judge_name:')
	flist=[]
	flist_t=[]
	flist_list=[]
	w=int(w)
	nn=1
	key = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
	for x in list:
		n=len(x)
		if n<3:
			pass
		elif judge_name in x:
			for ii in key:
				if ii in x:
					print "%s Have Sum" % judge_name
					m=1
					flist_t.append(x)
					break
				else:
					m=0

			if m==0:
				print "%s Not Sum" % judge_name
				flist.append(x)
				flist_t.append(x)
		else:
			flist.append(x)
			flist_list.append(x)
		nn+=1

	if w is 1:
		print 'w=%s Get Single Keyword Mode' % w
		f=__judge_file('d:/name_%s.txt' % judge_name)
		for i in flist_t:
			f.writelines(i)
		f.close()
	elif w is 2:
		print 'w=%s Discard single keyword mode' % w
		return flist_list
	else:
		print 'w=%s In addition to figures contain keywords' % w
		return flist

'''************************************'''

def handle_list(list):
	#先判断列表项是否合法
	#然后合并两个关键词为一行，再计算每行长度是否违规，如是便拆分词组为单独一行
	path='D:/name_list.txt'
	f1=__judge_file(path)
	jn=judge_name(list)
	n=0
	# list=jn(jn(jn(jn(jn(list,model),'ih'),'ir'),'w'),'v')
	for i in __list_del_BL_group(jn):
		f1.write(i)
		n+=1
	f1.close
	print 'Generate %s line: %d' % (path, n)

def list_del_list(list_a,list_b):
	#提供价格列表，坐参考删除型号列表内容及几个列表自身的内容
	#list_b需要处理的文件，list_a用来对比的文件
	path_xh='D:/file_contrast.txt'
	path_jg='D:/file_handle.txt'
	f1=__judge_file(path_xh)
	f2=__judge_file(path_jg)
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

	n=__list_w(jg_list,f2)
	print 'Generate %s line: %d' % (path_jg, n_jg)
	n=__list_w(list_b,f1)
	print 'Generate %s line: %d' % (path_xh, n)

	f1.close
	f2.close

def del_BL_w(f):
	#处理文件空行并生成文本。
	ad=raw_input('filepath:')
	handle(__del_BL(f),ad)

def split_h(f):
	f1,path=filepath(raw_input('path:'))
	var=raw_input('split(...):')
	location_sum=raw_input('location_sum:')
	n=0
	for i in f:
		content=i.split(var)[int(location_sum)]
		f1.write('%s\n' % content.replace('\n',''))
		n+=1
	print 'Generate %s line: %d' % (path, n)

if __name__ == '__main__':
	f=open('D:/name.txt','r').readlines()
	print '1.judge_name(f)\n2.handle_list(f)\n3.list_del_list(f,xh)\n4.del_BL_w(f)\n5.split_h(f)\n6.Average_sorting.main(raw_input(textdir:)'
	n=raw_input('please Select:')
	if n=='1':
		w=raw_input('mothod=')
		judge_name(f)
	elif n=='2':
		#生成有效name.txt文件
		handle_list(f)
	elif n=='3':
		#两个列表作对比需要读取时，使用以下处理
		contrast=open('D:/contrast.txt','r').readlines()
		list_del_list(f,contrast)
	elif n=='4':
		#删除空白行
		del_BL_w(f)
	elif n=='5':
		#分割，并获取所需值
		split_h(f)
	elif n=='6':
		Average_sorting.main('D:/name.txt')
	else:
		print 'Input error!'
