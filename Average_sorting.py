# coding: utf-8
import rw

success_list=[] #Meet the requirements of the combined group
    
def max_min_mark(var):
    max_min=[]  #Max ad min volue save var;[function_name : max_min_mark]
    for i in var:
        length=len(i)
        max_min.append(length)
    return max_min


def merger_group(textdir):
    textlines = open(textdir,'r').readlines()
    b_split=[]
    for i in xrange(0,len(textlines)):
        if i%2!=0:
            if len(x)+len(textlines[i])>35:
                b_split.append(x)
                b_split.append(textlines[i])
            else:
                success_list.append(x.replace('\n','')+' '+textlines[i])
        else:
            x=textlines[i]
    return b_split

def best_value(b_split):
    max_min=max_min_mark(b_split)
    min_value_location=max_min.index(min(max_min))
    while min_value_location:
        max_value_location=max_min.index(max(max_min))
        if max_min[max_value_location]+max_min[min_value_location]>35:
            success_list.append(b_split[max_value_location])
            success_list.append(b_split[max_value_location])
            max_min[max_value_location]=None
        else:
            success_list.append(b_split[max_value_location].replace('\n','')+' '+b_split[min_value_location])
            max_min[max_value_location]=None
            max_min[min_value_location]=None
            min_value_location=max_min.index(min(max_min))

def main(textdir):
    path=raw_input('save_filename:')
    best_value(merger_group(textdir))
    rw.handle(success_list,path)
        


if __name__ == '__main__':
    textdir = 'd:/name.txt'
    main(textdir)
