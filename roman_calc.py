def input_numbers():
    i = 0
    r_num = []
    while True:
        r_num.append(input(f" Gib die {i+1}. Zahl ein. Wenn du fertig bist, drücke Enter ohne eine Eingabe\n"))
        if r_num[i] == "":
            r_num.pop() #removes last item 
            break
        i += 1
    print(r_num)
    return(r_num)

def convert_to_roman(deci_numbers, roman_numbers, input_num):
    converted_numbers = []
    for i_r_num in input_num:        
        d_num_raw = []
        for letter in i_r_num: #going trough string
            for i in roman_numbers: #going through list
                if letter == i:
                    d_num_raw.append(deci_numbers[roman_numbers.index(i)])
                    break

        if len(i_r_num) != len(d_num_raw):
            print("Error")
            return(False)

        biggest_number = 0
        for i in d_num_raw: #finding biggest number to subtract everything before
            if i > biggest_number:
                biggest_number = i 
            biggest_number_index = d_num_raw.index(biggest_number)

        subtract = 0
        if biggest_number_index > 0:
            for number in range(biggest_number_index): #adding every number before the biggest number
                subtract = subtract + d_num_raw[number] #+1 to compensate stating to count at 0

        value = 0
        for number in range(biggest_number_index, len(d_num_raw)):
            value += d_num_raw[number]

        d_num_final = value - subtract
        converted_numbers.append(d_num_final)
    print(f"Converted numbers are:")
    for numbers in converted_numbers:
        print(numbers)
    return(converted_numbers)   

def calc(numbers):
    result = 0
    for i in numbers:
        result += i
    print(f"Das Ergebnis ist {result} (in Dezimal)")
    return(result)

def conversion(deci_numbers, roman_numbers, roman_list, deci_result, index):
    times_index = deci_result // deci_numbers[index]
    for i in range(times_index):
        roman_list.append(roman_numbers[index])
    deci_result = deci_result % deci_numbers[index]
    return(roman_list, deci_result)

def convert_to_deci(deci_numbers, roman_numbers, deci_result):
    roman_list = []    
    for i in reversed(range(len(roman_numbers))):
        try:
            roman_list, deci_result = conversion(deci_numbers, roman_numbers, roman_list, deci_result, i)
        except: 
            pass
    output = "".join(roman_list)
    return(output)

def main(deci_numbers, roman_numbers):
    usr_input = input_numbers()
    converted_numbers = convert_to_roman(deci_numbers, roman_numbers, usr_input)
    deci_result = calc(converted_numbers)
    output = convert_to_deci(deci_numbers, roman_numbers, deci_result)
    print(f"Das Ergebnis ist:", output)

if __name__ == "__main__":
    deci_numbers = [1,5,10,50,100,500,1000]
    roman_numbers = ["I","V","X","L","C","D","M"]
    main(deci_numbers, roman_numbers)

