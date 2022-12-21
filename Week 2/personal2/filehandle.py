
with open ("message.txt","r") as f:
    fcontent=f.read()
    print(fcontent)

    # with is the context manager 
    # by with keyword file closes automatically
 # if we donot close the file it causes 
 # leaks that cause to run over the maximum 
# allowed file descriptors on system and program may throw error
#  so its mandatory  to close a file 

##pass keyword 
'''
 Python, the pass keyword is an 
 entirestatement in itself
This statement doesn't do anything: 
it's discarded during the byte-compile 
 phase. But for a statement that does
'''
