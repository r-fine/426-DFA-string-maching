import pandas as pd

total_alph = 26
dct = {
    'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25
}

def computeTransFun(pattern, m, transFun):

    longest = 0 
    for x in range(total_alph):
    	transFun[0][x] = 0
    transFun[0][dct[pattern[0]]] = 1  
    for i in range(1, m+1): 
    	for x in range(total_alph):
    		transFun[i][x] = transFun[longest][x]   
    	if (i < m):
            transFun[i][dct[pattern[i]]] = i + 1  
            longest = transFun[longest][dct[pattern[i]]]

    # print(pd.DataFrame(transFun))

def search(pattern, text, t):
    m = len(pattern)
    n = len(text)
    transFun = [[0 for i in range(total_alph)] for j in range(m + 1)]
    computeTransFun(pattern, m, transFun) 
    j = 0
    c = 0
    for i in range(n):
        j = transFun[j][dct[text[i]]]
        if (j == m):
            c+=1
            # print("pattern found at index", i - m + 1)
    
    print(f"pattern found for T{t} {c} times")


texts = ["abababcabababcabababc" , "ababdabacdababacbab", "acbcbababcbacbcacbcaca", "bcbacbabcbabbbabcabbcabbcabcbababa"]
pattern = "ababa"

for t, text in enumerate(texts):
    search(pattern, text, t)
