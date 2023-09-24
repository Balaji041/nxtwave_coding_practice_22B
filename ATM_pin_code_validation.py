def validate_atm_pin_code(pin):
    # Complete this function
    if len(pin)==4 or len(pin)==6 and pin.isupper():
        return "Valid PIN Code"
    else:
        return "Invalid PIN Code"
        

pin = input()
# Call the validate_atm_pin_code function
print(validate_atm_pin_code(pin))

"""
input:9837
output:Valid PIN Code

"""
