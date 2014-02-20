# coding: utf-8
'''****************Private********************
	BL = blanklines '''

if __name__ == '__main__':
	f=open('D:/name.txt','r').readlines()
	print '1.judge_key(f)\n2.Copywt()\n3.list_del_list(f,xh)\n4.******\n5.split_h(f)\n6.Average_sorting.wide_line()\n6.1.Average_sorting.group_line(2,f)\n7.dowpic(pic)\n8,replace_text(raw_input(re_text:))'
	n=raw_input('please Select:')
	import Text_handle
	if n=='1':
		w=raw_input('mothod=')
		Text_handle.judge_key(f)
	elif n=='2':
		Text_handle.Copywt()
	elif n=='3':
		#两个列表作对比需要读取时，使用以下处理
		contrast=open('D:/contrast.txt','r').readlines()
		Text_handle.list_del_list(f,contrast)
	elif n=='5':
		#分割，并获取所需值
		Text_handle.split_h(f)

	#=================Average_sorting==========================
	import Average_sorting
	if n=='6':
		success_list = Average_sorting.wide_line(raw_input('wide_line:'),'D:/name.txt')
		path = raw_input('save_filename:')
		wlist(success_list,path,True)
	elif n=='6.1':
		group_list,linesum = Average_sorting.group_line(raw_input('group_line:'),f)
		wlist(group_list,'group_%d.txt' % linesum,True)

	#==================Html_handle==============================
	import Html_handle
	if n=='7':
		Html_handle.dowpic()
	elif n=='8':
		Html_handle.replace_text(open('d:/contrast.txt').read())
