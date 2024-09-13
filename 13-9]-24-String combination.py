def get_soln(word):

    let_count = 0
    for i in word:
    
        let_count += 1
    
    print(fact(let_count))

def fact(n):
    if n==0 or n ==1:
        return 1
    return n * fact(n-1)





    # result = 1
    
    # while let_count>0:
       
    #     result *= let_count
    #     let_count-=1
  
  
    # return result

word = input("Enter a string: ")

get_soln(word)



# ln 13 = mat

# ln 15: calls functions 
# mat 
# let_count =3