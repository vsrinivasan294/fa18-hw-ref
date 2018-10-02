# All code written assuming there are no checks for side effeects beacause it was not mentioned otherwise anywhere



"""
matrix_multiply

Given two 2-D input arrays `arr0`, `arr1`, return the matrix product arr0 * arr1.
Return None if the matrix product does not exist.

As with math, assume that indices are in [row][column] format, so each inner list is a row.
"""

def matrix_multiply(arr0, arr1):
    pass
    
"""
nth_largest_element

Given an input list `arr`, and index `n`, return the nth largest element.
Avoid using built-in sorting methods.
"""
def nth_largest_element(arr, n):
    
    if (arr == None):
        return None
    
    if (len(arr) == 0):
        return None
    
    check =[]
    for x in range (n):
        check.append(max(arr))
        max_val = arr.index(max(arr))
        arr.pop(max_val)
        
    return check[n-1]


"""

Alternate solution with recursion

def nth_largest_element(arr, n):
    if n == 1:
        return max(arr)
    maximum = max(arr)
    arr_new = list(filter(lambda a: a != maximum, arr))
    return nth_largest_element(arr_new, n-1)


"""


"""
reverse_block

Given an input list `arr`, and a block size `n` > 0, reverse the list in blocks of n.

Example:
	Arguments:
		[1,2,3, 4,5,6, 7], 3
	Return:
		[3,2,1, 6,5,4, 7]
	(spacing added for emphasis)

"""
def reverse_block(arr, n):
    
    if (arr == None):
        return None
    
    if (len(arr) == 0):
        return None
    
    i = 0
    
    while(i<len(arr)): 
      
        val_one = i  
        val_two = min(i + n - 1, len(arr) - 1)
        check = (val_two - val_one)/2
        while (check > 0): 
           
            arr[val_one], arr[val_two] = arr[val_two], arr[val_one] 
            val_one = val_one + 1 
            val_two = val_two - 1
            check = check - 1
            
        i+= n      
    return arr
    
"""
subset_sum

Given an input list `arr`, and a number `target`, return whether or not any possible subset of the values in `arr` could sum to `target`.

Example 1:
	Arguments:
		[1,2,3,4,5,7], 13
		7 + 4 + 2 = 13
	Return:
		True

Example 2:
	Arguments:
		[1,2,-1,5,4,-196], 196
	Return:
		False
"""
def checker(arr ,arr_length, target) : 
    
    if (arr == None):
        return None
    
    if (len(arr) == 0):
        return None
    
    
    if (target == 0) : 
        return True
    elif (arr_length == 0 and target != 0): 
        return False
   
    elif (arr[arr_length - 1] > target) : 
        return checker(arr, arr_length - 1, target) 
   
    else :
        return checker(arr, arr_length-1, target) or checker(arr, arr_length-1, target - arr[arr_length-1]) 

def subset_sum(arr, target):
    return checker(arr, len(arr), target)
"""
spiral_matrix

Given an input 2-D array, return a list with the values obtained by following a clockwise spiral path, starting from [0][0], then proceeding to [0][n], [m][n], [m][0], then going inwards:

Example:
	Argument:
		[[a,b,c,d,e],
		 [f,g,h,i,j],
		 [k,l,m,n,o],
		 [p,q,r,s,t],
		 [u,v,w,x,y]]
	Return:
		[a,b,c,d,e, j,o,t,y, x,w,v,u, p,k,f, g,h,i, n,s, r,q, l, m]
"""
def spiral_matrix(arr):
   

    if (arr is None):
        return None
    if (len(arr) == 0):
        return None
    
    #Stores the output list
    output = []
    
    #Counts the number of Rows completed
    row_count = 0
    
    #Counts the number of Columns completed
    column_count = 0
    
    #The number of Rows
    last_row = len(arr) - 1
    
    #The number of columns
    last_column = len(arr[0]) - 1

    while True:
        for x in range(column_count, last_column + 1):
            output.append((arr[row_count][x]))
        
        # If the row count is larger than the maximum number of rows, it is a L, so return whatever I have already
        row_count += 1
        if (row_count > last_row):
            return output

        for x in range(row_count, last_row + 1):
            output.append((arr[x][last_column]))
       
        #If the column count is greater than the number of columns it is a L, so return whatever I have already
        last_column -= 1
        if  (column_count > last_column):
            return output

        # This works when it is needed to check the values backwards when the rotation happens
        for x in range(column_count, last_column + 1)[::-1]:
            output.append((arr[last_row][x]))
        
        # If the row count is larger than the maximum number of rows, it is a L, so return whatever I have already
        last_row -= 1
        if (row_count > last_row):
            return output

        # This works when it is needed to check the values backwards when the rotation happens
        for x in range(row_count, last_row + 1)[::-1]:
            output.append((arr[x][column_count]))
        
        #If the column count is greater than the number of columns it is a L, so return whatever I have already    
        column_count += 1
        if (column_count > last_column):
            return output
        


