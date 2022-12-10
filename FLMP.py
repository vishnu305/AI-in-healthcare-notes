
def FLMPsearch(pat,txt):
    # collecting windows (preprocessing phase)
    m=len(pat)
    n=len(txt)
    window_index=[] # containes the 'start index' of windows which are having the first and last values as same
    count=0
    num_window=0 # this variable containes the number of windows created in preprocessing phase
    while count<=n-m:
        if txt[count]==pat[0] and txt[count+m-1]==pat[m-1]:
            window_index.append(count)
            num_window += 1
        count += 1
    
    #matching phase , here we compare the between elements of the founded windows
    count = 0
    num_match=0
    match_index=[]
    while count<num_window:
        s = window_index[count]
        c=1
        while c<=m-2:
            if pat[c] != txt[s+c]:
                break
            c += 1
        if c== m-1:
            match_index.append(s)
            num_match += 1
        count += 1
    
    if num_match>0:
        for i in match_index:
            print("Given pattern is found in the given text at position: ",i)
    else:
        print("Given pattern is not available in the given text")

        
import time
start = time.time()

txt = "ABABDABACDABABCABABBBDAMDABABCABAB"
pat = "ABABCABAB"
FLMPsearch(pat, txt)

end = time.time()
print("Time taken is: ",end-start)