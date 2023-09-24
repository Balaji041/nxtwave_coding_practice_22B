def calculate_percentage(number):
    
    # complete this function
    if number<1000:
        return((number/100)*5)
    else:
        return((number/100)*10)



number = int(input())

result =calculate_percentage(number) 
# Call the calculate_percentage function

print(result)

"""
input:500
output:25.0
"""
