def reverseVowelInString(s):
    vowels = "aeiouAEIOU"
    s_list = list(s)
    i=0 
    j = length = len(s)-1
    while i<j:
        print(s_list[i],s_list[j])
        if s_list[i] in vowels and s_list[j] in vowels:
            print ("inside", s_list[i],s_list[j],i,j)
            temp = s_list[i]
            s_list[i] = s_list[j]
            s_list[j] = temp
            j -=1
        i +=1
               
    return "".join(s_list)

print(reverseVowelInString("leetcode"))