#        Hallo, Stefan, Roland & Andreas, ich hab hier nochmal die Aufgabe von gestern durch gearbeitet und 
#        habe herrausgefunden, warum das gestern so Probleme gab. Denn man mag es sich kaum vorstellen,
#        aber ich habe unter dieser Stresssituation tatsächlich vergessen dass If-Else-Statements existieren. 
#        Ich versuchte durchgehend krampfhaft zu überlegen, wie ich 2 Werte verleich. Das ist mir dann tatsächlich 
#        erst am späten Abend aufgefallen. Ich habe mich dann heute morgen rangesetzt und angefangen einfach mal runterzuschreiben.
#
#        Zur Transparenz: ich habe die Funktion .pop, .join & reversed() gegooglet, der Rest ist völlig mein Werk.
#
#        Beste Grüße Boas

def input_numbers():
    i = 0
    r_num = []
    while True:
        r_num.append(input(f"Gib die {i+1}. Zahl ein. Wenn du fertig bist, drücke Enter ohne eine Eingabe\n"))
        if r_num[i] == "": # breaks if user wants to proceed
            r_num.pop() #removes last item (created empty item to proceed due to pressing enter)
            break
        i += 1
    return(r_num)

def convert_from_roman(deci_numbers, roman_numbers, input_num): #converting numbers from roman to decimal, through comparing them with indexes in lists
    converted_numbers = []
    for i_r_num in input_num:        
        d_num_raw = [] # The idea is to convert every letter to it corresponding number, therefore we initalize the decimal_numbers_raw list
        for letter in i_r_num: #going trough string
            for i in roman_numbers: #going through list of Roman Letters
                if letter == i:
                    d_num_raw.append(deci_numbers[roman_numbers.index(i)]) # adding converted numers to a list to add them together later
                    break # exits the loop after finding the correlationg number

        if len(i_r_num) != len(d_num_raw): #to validate, if something goes horrobly wrong, it breaks here.
            print("Error")
            return(False)

        biggest_number = 0 # initializing variable
        for i in d_num_raw: #finding biggest number to subtract everything before
            if i > biggest_number: 
                biggest_number = i 
            biggest_number_index = d_num_raw.index(biggest_number) # using built in .index function to find the biggest number in the d_num_raw list (f.e. [1,4,5]), therefore the command would be d_num_raw.index(5) and it would return 2

        subtract = 0 #init var 
        if biggest_number_index > 0: #if the biggest nummer is in first place (f. e. XIII) nothing needs to be subtracted
            for number in range(biggest_number_index): #adding every number before the biggest number
                subtract = subtract + d_num_raw[number] #+1 to compensate stating to count at 0

        value = 0 #initialising variable
        for number in range(biggest_number_index, len(d_num_raw)): # adding numbers after, and including the biggest number
            value += d_num_raw[number]

        d_num_final = value - subtract #subtracting predfix (if needed, if not, i subtracts 0)
        converted_numbers.append(d_num_final) #appending converted number to list and start over
    return(converted_numbers)   

def calc(numbers): #simple method for adding all the nubers together
    result = 0
    for i in numbers: # itterating through every number and adding it 
        result += i
    print(f"Das Ergebnis ist {result} (in Dezimal)")
    return(result)

def conversion(deci_numbers, roman_numbers, roman_list, deci_result, index): #method to convert the numbers back to decimal, could also be done with 6 if-statements, but i decided to do it dynamicly with the try-except method, so it will fail, get catched, and start over with the next index
    times_index = deci_result // deci_numbers[index] #deviding while rounding down (using //)
    for i in range(times_index): #adding the letter to a list, how many times it is available
        roman_list.append(roman_numbers[index])
    deci_result = deci_result % deci_numbers[index] # using Modulo to get the remainder of the devision
    return(roman_list, deci_result) # and pass it on to the next method

def convert_from_deci(deci_numbers, roman_numbers, deci_result):
    roman_list = [] # init list to add every single letter, later it will be merged  to a string
    for i in reversed(range(len(roman_numbers))): # getting length of list of roman numbers, in this case 6. reverse it and use it in a for loop
        try:
            roman_list, deci_result = conversion(deci_numbers, roman_numbers, roman_list, deci_result, i) # index gets passed, if index is 6, it devides by 1000 and uses letter M cause both are at index 6. Then counting down until were deviding by 1, and finishes
        except: 
            pass
    output = "".join(roman_list) #converting list to string 
    return(output) #and outputs the combined string

def main(deci_numbers, roman_numbers):
    usr_input = input_numbers() # gets user input
    converted_numbers = convert_from_roman(deci_numbers, roman_numbers, usr_input) #starts conversion from roman to decimal
    deci_result = calc(converted_numbers) #starts calculation/adding process
    output = convert_from_deci(deci_numbers, roman_numbers, deci_result) #converting from decimal to roman
    print(f"Das Ergebnis ist:", output) #and outputting result

if __name__ == "__main__": #defining constants and starting the programm
    deci_numbers = [1,5,10,50,100,500,1000]
    roman_numbers = ["I","V","X","L","C","D","M"]
    main(deci_numbers, roman_numbers)
