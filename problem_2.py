def binary_search(start,end,input_list,number):
	
	 mid=(start+end)//2
	 if(start>end):
	 	return -1
	 if(input_list[mid]>number):
	 	if(input_list[start]>input_list[end]):
	 		if(input_list[end]<number):
	 			return binary_search(start,mid-1,input_list,number)
	 		elif(input_list[end]>number):
	 			return binary_search(mid+1,end,input_list,number)
	 		else:
	 			return end
	 	else:
	 		return binary_search(start,mid-1,input_list,number)
	 
	 elif(input_list[mid]<number):
	 	if(input_list[start]>input_list[end]):
	 		if(input_list[end]<number):
	 			return binary_search(start,mid-1,input_list,number)
	 		elif(input_list[end]>number):
	 			return binary_search(mid+1,end,input_list,number)
	 		else:
	 			return end
	 	else:
	 		return binary_search(mid+1,end,input_list,number)
	 
	 else:	 	
	 	return mid
	 	



def rotated_array_search(input_list, number):
    
    if(len(input_list)==0):
    	return -1
    start = 0
    end = len(input_list)-1
    return binary_search(start,end,input_list,number)






print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)) #prints 0
print(rotated_array_search([1, 2, 3, 4, 6, 7, 8, 9, 10], 10)) #prints 8 even though non rotated list 
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 0)) #prints -1 as number not found
print(rotated_array_search([], 0)) #prints -1 as it's empty list
