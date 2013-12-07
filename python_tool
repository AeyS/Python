# coding: utf-8
import os
import sys
'''****************Private********************
	BL = blanklines
'''
def __list_del_BL_group(list):
	f=__judge_file('d:/log.log')
	nn=0
	for x in list:
		n=len(x)
		if n<2:
			pass
		elif nn%2==0:
			f.write(x.replace('\n','')+' ')
		else:
			f.write(x)
		nn+=1
	f.close()
	key_list=open('d:/log.log').readlines()
	return key_list

def __list_len_grouping(key_list):
	nn=1
	key_list_split=[]
	for x in key_list:
		n=len(x)
		if n>38:
			print 'n>38'
			key=x.split(' ')
			key_list_split.append(key[0]+'\n')
			key_list_split.append(key[1])
		else:
			key_list_split.append(x)
		nn+=1
	return key_list_split

def __list_w(list,f):
	for i in list:
		f.write(i)
		print i,

def __judge_file(path):
	if os.path.isfile(path):
		os.remove(path)
	f1=open(path,'a+')
	return f1

def __handle(list_a):
	path='d:/namess.txt'
	f2=__judge_file(path)
	for i in list_a:
		f2.writelines(i)
	f2.close()
	print 'Generate %s' % path

def __del_BL(list):
	list_a=[]
	for i in list:
		n=len(i)
		if n<3:
			pass
		else:
			i=i.replace('"','')
			list_a.append(i)
	return list_a

def judge_name(list,judge_name,w=0):
	#处理列表里的带数字关键词,judge pump have sum,if have jump out
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

def handle_list(list,model):
	#先判断列表项是否合法
	#然后合并两个关键词为一行，再计算每行长度是否违规，如是便拆分词组为单独一行
	path='D:/name_list.txt'
	f1=__judge_file(path)
	jn=judge_name
	# list=jn(jn(jn(jn(jn(list,model),'ih'),'ir'),'w'),'v')
	for i in __list_len_grouping(__list_del_BL_group(list)):
		f1.write(i)
	f1.close
	print 'Generate %s' % path

def list_del_list(list_a,list_b):
	#提供价格列表，坐参考删除型号列表内容及几个列表自身的内容
	path_xh='D:/handle_xh.txt'
	path_jg='D:/handle_jg.txt'
	f1=__judge_file(path_xh)
	f2=__judge_file(path_jg)
	sum_list=[]
	jg_list=[]
	n=0
	for x in list_a:
		if len(x) <3:
			#以长度小于3来判断‘/’空白项的位置，并收集在sum_list里
			sum_list.append(n)
			print n,x,
		else:
			#这份价格列表就剔除了‘/’空白项
			jg_list.append(x)
		n+=1
	n=0
	for k in sum_list:
		#这份型号列表就剔除了‘/’空白项，因为每删除一项，列表总数就减少1，所以删除一项的位置就得通过-n次来获取。
		k=k-n
		del list_b[k]
		print 'del%s' % k
		n+=1

	__list_w(list_b,f1)
	print 'Generate %s' % path_xh
	__list_w(jg_list,f2)
	print 'Generate %s' % path_jg


	f1.close
	f2.close

def del_BL_w(f):
	#处理文件空行并生成文本。
	__handle(__del_BL(f))

if __name__ == '__main__':
	f=open('D:/name.txt','r').readlines()
	judge_name(f,'is',1)
	#生成有效name.txt文件
	# handle_list(f,'is')
	#两个列表作对比需要读取时，使用以下处理
	# xh=open('D:/xh.txt','r').readlines()
	# list_del_list(f,xh)
