def count_of_uppercase(word):
    c=0
    # complete this function
    for i in word:
        if i.isupper():
            c+=1
    return c


word = input()

result =count_of_uppercase(word) # Call the count_of_uppercase function

print(result)

"""
input:eXpLoRe
output:3
"""
