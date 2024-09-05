#        Hallo, Stafan, Roland & Andreas, ich hab hier nochmal die Aufgabe durch gearbeitet und 
#        habe herrausgefunden, warum das gestern so Probleme gab. Denn man mag es sich kaum vorstellen,
#        aber ich habe tatsächlich If-Else-Statements vergessen. Das ist mir dann tatsächlich erst am späten
#        Abend aufgefallen. Ich habe mich dann heute morgen rangesetzt und angefangen einfach mal runterzuschreiben.
#        Zur Transparenz: ich habe die Funktion .pop, .join & reversed() gegooglet. 

def input_numbers():
    i = 0
    r_num = []
    while True:
        r_num.append(input(f" Gib die {i+1}. Zahl ein. Wenn du fertig bist, drücke Enter ohne eine Eingabe\n"))
        if r_num[i] == "": # breaks if user wants to proceed
            r_num.pop() #removes last item (created empty item to proceed due to pressing enter)
            break
        i += 1
    return(r_num)

def convert_from_roman(deci_numbers, roman_numbers, input_num): #converting numbers from roman to decimal, through comparing them with indexes in lists
    converted_numbers = []
    for i_r_num in input_num:        
        d_num_raw = []
        for letter in i_r_num: #going trough string
            for i in roman_numbers: #going through list
                if letter == i:
                    d_num_raw.append(deci_numbers[roman_numbers.index(i)]) # adding converted numers to a list to later add later
                    break

        if len(i_r_num) != len(d_num_raw): #to validate, if something goes horrobly wrong, it breaks here.
            print("Error")
            return(False)

        biggest_number = 0
        for i in d_num_raw: #finding biggest number to subtract everything before
            if i > biggest_number:
                biggest_number = i 
            biggest_number_index = d_num_raw.index(biggest_number)

        subtract = 0
        if biggest_number_index > 0: #if the biggest nummer is in first place (f. e. XIII) nothing needs to be subtracted
            for number in range(biggest_number_index): #adding every number before the biggest number
                subtract = subtract + d_num_raw[number] #+1 to compensate stating to count at 0

        value = 0 #initialising variable
        for number in range(biggest_number_index, len(d_num_raw)): # adding numbers after and including biggest number
            value += d_num_raw[number]

        d_num_final = value - subtract #subtracting suffix (if needed)
        converted_numbers.append(d_num_final) #appending converted number to list and start over
    print(f"Converted numbers are:")
    for numbers in converted_numbers:
        print(numbers)
    return(converted_numbers)   

def calc(numbers):
    result = 0
    for i in numbers: #simply add every number together 
        result += i
    print(f"Das Ergebnis ist {result} (in Dezimal)")
    return(result)

def conversion(deci_numbers, roman_numbers, roman_list, deci_result, index): #method to convert the numbers back to decimal, could also be done with 6 if-statements, but i decided to do it dynamicly with the try-except method, so it will fail, get catched, and start over with the next index
    times_index = deci_result // deci_numbers[index] #deviding while rounding down
    for i in range(times_index): #adding the letter to a list, how many times it is available
        roman_list.append(roman_numbers[index])
    deci_result = deci_result % deci_numbers[index]
    return(roman_list, deci_result)

def convert_from_deci(deci_numbers, roman_numbers, deci_result):
    roman_list = []    
    for i in reversed(range(len(roman_numbers))): # getting length of list of roman numbers, in this case 6. reverse it and use it in a for loop
        try:
            roman_list, deci_result = conversion(deci_numbers, roman_numbers, roman_list, deci_result, i) # index gets passed, if index is 6, it devides by 1000 and uses letter M cause both are at index 6. Then counting down until were deviding by 1, and finishes
        except: 
            pass
    output = "".join(roman_list) #converting list to string 
    return(output) #and outputs

def main(deci_numbers, roman_numbers):
    usr_input = input_numbers() # gets user input
    converted_numbers = convert_from_roman(deci_numbers, roman_numbers, usr_input) #starts conversion from roman to decimal
    deci_result = calc(converted_numbers) #starts calculation/adding process
    output = convert_from_deci(deci_numbers, roman_numbers, deci_result) #converting back
    print(f"Das Ergebnis ist:", output) #and outputting result

if __name__ == "__main__":
    deci_numbers = [1,5,10,50,100,500,1000]
    roman_numbers = ["I","V","X","L","C","D","M"]
    main(deci_numbers, roman_numbers)

