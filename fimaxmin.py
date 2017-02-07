def find_max_min(arg):
    """function returns a list of min and max 
       numbers from input or one number if min == max"""
       
    min_num = ''
    max_num = ''
    mylist = []
    
    min_num = min(arg)
    max_num = max(arg)
    
    if min_num == max_num:
       mylist.append(min_num)
       return mylist
       
    else:
        mylist.append(min_num);
        mylist.append(max_num)  
        return mylist        
        
#print(find_max_min([1,1,1]))        