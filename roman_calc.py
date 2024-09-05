#        Hallo, Stefan, Roland & Andreas, ich habe hier nochmal die Aufgabe von gestern durchgearbeitet und 
#        habe herausgefunden, warum es gestern so Probleme gab. Denn man mag es sich kaum vorstellen,
#        aber ich habe unter dieser Prüfungssituation tatsächlich vergessen, dass If-Else-Statements existieren. 
#        Ich versuchte durchgehend krampfhaft zu überlegen, wie ich 2 Werte vergleichen könnte. Das ist mir dann leider 
#        erst am späten Abend aufgefallen. Ich habe mich heute Morgen rangesetzt und angefangen einfach mal runterzuschreiben.
#
#        Zur Transparenz: ich habe die Funktion .pop(), .join() & reversed() gegooglet, der Rest ist auswendig entstanden.
#
#        Ihr haben meine Telefonnummer, falls Fragen oder Hinweise bestehen, bitte ich um einen Anruf.
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
        d_num_raw = [] # The idea is to convert every letter to it corresponding number, one by one, therefore we initalize the decimal_numbers_raw list
        for letter in i_r_num: #going trough string
            for i in roman_numbers: #going through list of Roman Letters
                if letter == i:
                    d_num_raw.append(deci_numbers[roman_numbers.index(i)]) # adding converted numers to a list to add them together later
                    break # exits the loop after finding the correlationg number
        #Uncomment the following line to see each letter be converted to it's corresponding number
        #print(f"Deine Übersetzung lautet: {d_num_raw}")    
        
        if len(i_r_num) != len(d_num_raw): #to validate. if something goes horrobly wrong, it quits here.
            print("Error")
            quit()

        biggest_number = 0 # creating variable
        for i in d_num_raw: #finding biggest number in list. If we know the biggest number (f.e. [I,I,V]), we can add all the number in front of it, and substract them from the "main" number
            if i > biggest_number: 
                biggest_number = i 
        biggest_number_index = d_num_raw.index(biggest_number) # using built in .index method to find the biggest number in the d_num_raw list (f.e. [1,4,5]), therefore the command would be d_num_raw.index(5) and it would return 2
                                                                # could have also been done with a counter in the loop, but i thought that to be more readalbe
        subtract = 0 #creating var 
        if biggest_number_index > 0: #if the biggest nummer is in first place (f. e. XIII) nothing needs to be subtracted
            for number in range(biggest_number_index): 
                subtract = subtract + d_num_raw[number] #adding every number before the biggest number

        value = 0 #initialising variable
        for number in range(biggest_number_index, len(d_num_raw)): # adding numbers after the biggest to a value. len() gets the length of a list/string
            value += d_num_raw[number]

        d_num_final = value - subtract #subtracting prefix (if not needed, subtract variable has the value 0, so i didn't bother to implment a check there)
        converted_numbers.append(d_num_final) #appending converted number to list and start over with the next input
    return(converted_numbers)   # if everything is done a list of everything converted gets returned (f.e. ["VII", "XVI", "M"] -> [7, 16, 1000]

def calc(numbers): #simple method for adding all the elements/numbers of the (converted)number list together
    result = 0
    for i in numbers: # itterating through every number and adding it 
        result += i
    print(f"Das Ergebnis ist {result} (in Dezimal)") # was initialy there for debuging, but it turned out to be a nice feature
    return(result)

def conversion(deci_numbers, roman_numbers, roman_list, deci_result, index): #method to convert the numbers back to decimal, could also be done with 6 if-statements, but i decided to do it dynamicly with the try-except method, so it WILL fail (if final number < 1000), get catched, and start over with the next "index" 
    times_index = deci_result // deci_numbers[index] #deviding while rounding down (using //). times_index is to be interpreted as times_M for 1000 or times_D for 500.
    for i in range(times_index): #adding the letter to a list, how many times it is available (f.e. Number is 5000, then 5 M get added)
        roman_list.append(roman_numbers[index])
    deci_result = deci_result % deci_numbers[index] # using Modulo to get the remainder of the devision and setting it as the new number to convert
    return(roman_list, deci_result) # and pass it on to the next round until we finaly devided by 1 /index 0 / letter I, could be prevented in following for-loop that triggers this method, but is not present for readability purposes

def convert_from_deci(deci_numbers, roman_numbers, deci_result):
    roman_list = [] # init list to add every single letter, later it will be merged  to a string
    for i in reversed(range(len(roman_numbers))): # getting length of the list 'roman_numbers', which is 6, reverses them  it and use it in a for loop. So instead of 0,1,2,3,4,5,6 , the reversed() method changes the order to 6,5,4,3,2,1,0. Again, 0 could be left out by using the args 'for i in reversed(range(1, len(roman_numbers))):'
        try:
            roman_list, deci_result = conversion(deci_numbers, roman_numbers, roman_list, deci_result, i) #triggers the method explained above. index of for-loop gets passed, if index is 6, it devides by 1000 and uses letter M cause both are at index 6. Then counting down until after deviding by 1, and finishes the loop
        except: 
            pass
    output = "".join(roman_list) #converting list to string 
    return(output) #and returns the final result in Roman numbers / letters

def main(deci_numbers, roman_numbers): # just triggers each method
    usr_input = input_numbers() # gets user input
    converted_numbers = convert_from_roman(deci_numbers, roman_numbers, usr_input) #starts conversion from roman to decimal
    deci_result = calc(converted_numbers) #starts calculation/adding process
    output = convert_from_deci(deci_numbers, roman_numbers, deci_result) #converting from decimal to roman
    print(f"Das Ergebnis ist:", output) #and outputting result

if __name__ == "__main__": #defining constants and starting the programm
    deci_numbers = [1,5,10,50,100,500,1000]
    roman_numbers = ["I","V","X","L","C","D","M"]
    main(deci_numbers, roman_numbers)
