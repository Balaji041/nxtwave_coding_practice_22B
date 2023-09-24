def count_the_vowels(word):
    # Complete this function
    v=0
    for i in word:
        if i == "A" or i=="a" or i=="E" or i== "e" or i=="i" or i== "I" or i=='o' or i=="O" or  i=="U" or i=="u":
            v+=1
    return v
    
        

word = input()
# Call the count_the_vowels function
print(count_the_vowels(word))

"""
input:suggestions
output:4
"""
