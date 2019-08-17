def sort_012(input_list):
    start = 0
    end = len(input_list)-1
    if(end==-1):
    	return "Empty input list"
    i=0
    
    while(i<len(input_list)):
    	if(input_list[start]==0):    		
    		if(start==i):    			
    			i+=1
    		start+=1
    		
    		continue
    	if(input_list[end]==2):
    		end-=1
    		continue
    	
    	if(i>end or start>end):
    		break
    	if(input_list[i]==0):   		
    		input_list[i],input_list[start] = input_list[start],input_list[i]
    		if(input_list[i]!=0):
    			if(input_list[i]==2):
    				input_list[i],input_list[end] = input_list[end],input_list[i]
    				end-=1
    			i+=1
    		start+=1
    			
    	elif(input_list[i]==2):
    		input_list[i],input_list[end] = input_list[end],input_list[i]
    		if(input_list[i]!=2):
    			if(input_list[i]==0):
    				input_list[i],input_list[start] = input_list[start],input_list[i]
    				start+=1    		
    			i+=1
    		end-=1
    	else:
    		i+=1
    return input_list
    

#prints [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])) 

#Empty list input
print(sort_012([])) #prints Empty input list 

#already sorted input
print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
#prints [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]