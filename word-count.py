def words(arg):
    """function counts the number of occurences of 
       each word in a string"""
    
    wordlist = [] # hold tokens of split string
    wordlist = arg.split() # initial split of string delimited by space characters
    
    for i in range(len(wordlist)):
        """loop splits tokens obtained above delimited by new line character"""
        
        word = wordlist[i].split('\n') 
        if len(word) > 0:
            j = 0
            k = i
            for elem in word:
                if k == i:
                    wordlist[k] = word[j]
                else:
                    wordlist.insert(k,word[j])
                k+=1
                j+=1                
    
    for i in range(len(wordlist)):
        """loop splits tokens obtained above delimited by horizontal tab character"""
        
        word = wordlist[i].split('\t') 
        if len(word) > 0:
            j = 0
            k = i
            for elem in word:
                if k == i:
                    wordlist[k] = word[j]
                else:
                    wordlist.insert(k,word[j])
                k+=1
                j+=1   
    
    mydict = dict()
    for word1 in wordlist:
        """loop builds dictionary of key value pairs of word and number of occurences"""
        
        if len(mydict) == 0:
            if word1 in ['0','1','2','3','4','5','6','7','8','9']:
                mydict[int(word1)] = wordlist.count(word1)
            else:
                mydict[word1] = wordlist.count(word1)        
        else:
            if word1 not in mydict.keys():
                if word1 in ['0','1','2','3','4','5','6','7','8','9']:
                    mydict[int(word1)] = wordlist.count(word1)
                else:
                    mydict[word1] = wordlist.count(word1)
                
    return mydict
     
  
      

