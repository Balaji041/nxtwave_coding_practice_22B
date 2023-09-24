def valid_string(string):
    
    # complete this function
    length=len(string)>6
    string_=string[0].isdigit()
    if length or string_:
        return("Valid String")
    else:
        return("Invalid String")


string = input()

result = valid_string(string)# Call the valid_string function

print(result)

"""
input:test
output:Invalid String

"""
