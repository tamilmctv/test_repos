def get_soln(str1, str2):
        
    str1_len = 0
    for i in str1:
       str1_len += 1
    
    str2_len = 0
    for i in str2:
        str2_len += 1
    
    if str1_len != str2_len:
        return "no"

    for i in str1:
        if i not in str2:
            return "no"
    
    return "yes"
str1 = input()
str2 = input()

print(get_soln(str1,str2))