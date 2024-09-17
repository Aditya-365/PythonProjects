print("This program converts any number you enter from to_base 10 to any to_base you want : ")
print("")

number = (input("Enter number : "))
from_base = int(input("From Base : "))
to_base = int(input("To Base : "))
ans_list = []
base_dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

if from_base == 10 :
    if (0 < to_base <= 16) and number > 0 :
        remainder = int(number)%to_base
        quotient = int(number/to_base)
        if remainder >= 10 :
            for i in base_dict.keys() :
                    if remainder == i :
                        remainder = base_dict[i]
                        ans_list.append(remainder)
        else :
            ans_list.append(remainder)

        while quotient > 0 :
            number = int(quotient)
            remainder = number%to_base
            quotient = number/to_base

            if remainder >= 10 :
                for i in base_dict.keys() :
                    if remainder == i :
                        remainder = base_dict[i]
                        ans_list.append(remainder)

            else :
                ans_list.append(remainder)

        j = -2

        for i in range(len(ans_list)) :
            if i == len(ans_list) - 1 :
                break
            else :
                print(ans_list[j],end="")
                j = j-1
    else :
        print("One or more of your inputs is invalid.")


if to_base == 10 :
    if (0 < from_base < 10) and number > 0 :
        num_list = list(str(number))
        count = len(num_list)
        j = -1
        x = 0
        total_value = 0
        while count > 0 :
            digit = int(int(num_list[j]) * ((from_base)**x))
            x = x + 1
            j = j - 1
            total_value = int(total_value) + digit 
            count = count - 1

    elif (10<= from_base <= 16) :
        num_list = list(str(number))
        count_1 = -1
        for i in num_list :
            count_1 = count_1 + 1
            for j in base_dict.values() :
                if i == j :
                    num_list[count_1] = base_dict.keys
                    print(num_list)
                
        count = len(num_list)
        z = -1
        x = 0
        total_value = 0
        while count > 0 :
            digit = int(int(num_list[z]) * ((from_base)**x))
            x = x + 1
            z = z - 1
            total_value = int(total_value) + digit 
            count = count - 1
            
    print(total_value)
     
else : 
    print("One or more of your inputs is invalid. ")