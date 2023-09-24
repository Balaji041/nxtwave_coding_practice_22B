def get_speed_status(speed):
    # Complete this function
    if speed<60:
        return "Normal"
    elif speed>=60 and speed<80:
        return "Warning"
    else:
        return "Over Speed"

speed = int(input())
# Call the get_speed_status function
print(get_speed_status(speed))

"""
input:75
output:Warning

"""
