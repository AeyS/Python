# coding: utf-8

class Average_sorting(object):
    """docstring for Average_sorting"""
    def __init__(self, widenum, textdir):
        super(Average_sorting, self).__init__()
        self.widenum = int(widenum)
        self.textdir = textdir
        self.success_list=[] #Meet the requirements of the combined group
        self.b_split=[]
    
    def max_min_mark(self):
        self.max_min=[]  #Max ad min volue save var;[function_name : max_min_mark]
        for i in self.b_split:
            length=len(i)
            self.max_min.append(length)

    def del_list_value(self,list1,list2,n):
        del list1[n]
        del list2[n]
        #Each time run get max_min
        self.max_min_mark()

    def merger_group(self):
        textlines = open(self.textdir,'r').readlines()
        for i in xrange(0,len(textlines)):
            if i%2!=0:
                if len(x)+len(textlines[i])>self.widenum:
                    self.b_split.append(x)
                    self.b_split.append(textlines[i])
                else:
                    self.success_list.append(x.replace('\n','')+' '+textlines[i])
            else:
                x=textlines[i]

    def best_value(self):
        self.merger_group()
        self.max_min_mark()
        if len(self.max_min) == 0:
            raise ValueError("self.max_min list is Null,\nPlease check whether the file is empty!")
        min_value=self.max_min.index(min(self.max_min))
        while len(self.max_min) != 1:
            print 'Every line widenum_list: %s' % self.max_min
            max_value=self.max_min.index(max(self.max_min))
            print 'list max_seat:  %s min_seat:  %s' % (max_value,min_value)
            if len(self.b_split[max_value])+len(self.b_split[min_value])>self.widenum:
                self.success_list.append(self.b_split[max_value])
                self.del_list_value(self.max_min,self.b_split,max_value)
                print "Single"
            else:
                self.success_list.append(self.b_split[max_value].replace('\n','')+' '+self.b_split[min_value]+'\n')
                self.del_list_value(self.max_min,self.b_split,max_value)
                min_value=self.max_min.index(min(self.max_min))
                self.del_list_value(self.max_min,self.b_split,min_value)
                print "Double"
            min_value=self.max_min.index(min(self.max_min))
        
        print 'list max_seat:  %s min_seat:  %s' % (max_value,min_value)
        self.success_list.append(self.b_split[0])
        return self.success_list


def main(widenum, textdir):
    path = raw_input('save_filename:')
    if widenum == '':
        widenum = 35
    asg = Average_sorting(widenum, textdir)
    success_list = asg.best_value()
    import rw
    rw.handle(success_list,path)


if __name__ == '__main__':
    textdir = 'd:/name.txt'
    main(35, textdir)
