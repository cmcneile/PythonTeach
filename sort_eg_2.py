##
##  https://developers.google.com/edu/python/sorting
##

strs = ['aa', 'BB', 'zz', 'CC']
print sorted(strs)  
print sorted(strs, reverse=True)   
## "key" argument specifying str.lower 
## function to use for sorting
print sorted(strs, key=str.lower)  

