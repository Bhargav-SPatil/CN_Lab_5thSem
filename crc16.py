def division(a_data):
    rem = a_data[:16]
    i = 16
    div = ""
    while i < 23:
        rem = rem + a_data[i]
        temp = ""
        if rem[0] == "1":
            div = divisor
        else:
            div = "00000000000000000"
        
        j = 0
        for j in range(1, 17):
            if (rem[j] == "0" and div[j] == "0") or (rem[j] == "1" and div[j] == "1"):
                temp = temp + "0"
            elif (rem[j] == "0" and div[j] == "1") or (rem[j] == "1" and div[j] == "0"):
                temp = temp + "1"
        
        rem = ""
        rem = temp
        i += 1
    return rem
    
data = "1011101"
divisor = "10001000000100001"

m_data = data + "0000000000000000"

rem = division(m_data)
print("CRC: ", rem);
t_data = data + rem
print("Data transmitted: ", t_data)

rem = division(t_data)

if rem == "0000000000000000":
    print("No error in data recieved")
else:
    print("One or more error in data recieved")
# rem = t_data[:16]
# i = 16
# div = ""
# while i < 23:
#     rem = rem + t_data[i]
#     temp = ""
#     if rem[0] == "1":
#         div = divisor
#     else:
#         div = "00000000000000000"
    
#     j = 0
#     for j in range(1, 17):
#         if (rem[j] == "0" and div[j] == "0") or (rem[j] == "1" and div[j] == "1"):
#             temp = temp + "0"
#         elif (rem[j] == "0" and div[j] == "1") or (rem[j] == "1" and div[j] == "0"):
#             temp = temp + "1"
    
#     rem = ""
#     rem = temp
#     i += 1

# print("CRC: ", rem);

# r_data = input("Enter the data recieved: ")

# if r_data == t_data:
#     print("Data recieved is correct")
# else:
#     print("One or more bits are incorrect")
