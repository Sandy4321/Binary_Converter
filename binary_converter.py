# binary converter
# Just for fun. It would be nice to get rid of that big ugly dictionary in the middle of the code.
# -*- coding: utf-8 -*-
"""
@author: Kris Eberwein
"""

user_input = raw_input('What number or phrase do you want me to convert to binary?')
try:
    int(user_input)
except ValueError:
    number = False
else:
    number = True 

if number == False:
    #Converts letter to binary using dictionary
    def convert_letter(input):	
    	for letter in input:
    		print 'Your converted letter is...'
    		print master_dict[input]
    #Converts sentence into binary		
    def convert_sent(input):	
    	sentence_to_convert = []	
    	for i in input:
    		sentence_to_convert.append(i)	
    	print 'Your converted sentence is...'	
    	for letter in sentence_to_convert:
    		print master_dict[letter]

    global master_dict
    master_dict = {
    'a':	"01100001",
    'b':	"01100010",
    'c':	"01100011",
    'd':	"01100100",
    'e':	"01100101",
    'f':	"01100110",
    'g':	"01100111",
    'h':	"01101000",
    'i':	"01101010",
    'k':	"01101011",
    'l':	"01101100",
    'm':	"01101101",
    'n':	"01101110",
    'o':	"01101111",
    'p':	"01110000",
    'q':	"01110001",
    'r':	"01110010",
    's':	"01110011",
    't':	"01110100",
    'u':	"01110101",
    'v':	"01110110",
    'w':	"01110111",
    'x':	"01111000",
    'y':	"01111001",
    'z':	"01111010",
    'A':	"01000001",
    'B':	"01000010",
    'C':	"01000011",
    'D':	"01000100",
    'E':	"01000101",
    'F':	"01000110",
    'G':	"01000111",
    'H':    "01001000",
    'I':	"01001001",
    'J':	"01001010",
    'K':	"01001011",
    'L':	"01001100",
    'M':	"01001101",
    'O':	"01001111",
    'P':	"01010000",
    'Q':	"01010001",
    'R':	"01010010",
    'S':	"01010011",
    'T':	"01010100",
    'U':	"01010101",
    'V':	"01010110",
    'W':	"01010111",
    'X':	"01011000",
    'Y':	"01011001",
    'Z':	"01011010",
    ' ':    "00100000",}

    #Figure out what kind of input user decides, decimal, letter or sentence
    def length():
    	if user_input.__len__() == 1:
    		#print user_input.__len__()
    		convert_letter(user_input)
    	else :
    		#print user_input.__len__()
    		convert_sent(user_input)
    length()
else:
#Converts decimal into binary
    def convert_num():
    #Loop over P and divide by 2 until we find a whole number
        p = 0
        user_num = float(user_input)
        while ((2**p)*user_num)%1 != 0:
            print('Remainder = ' + str((2**p)*user_num - int((2**p)*user_num)))
            p += 1
    #Whole number is found, multiply to 2 to the power of P
        num = int(user_num*(2**p))
    #Divide by 2, moving the decimal
        result = ''
        if num == 0:
            result = '0'
        while num > 0:
            result = str(num%2) + result
            num = num/2
        for i in range(p - len(result)):
            result = '0' + result
        result = result[0:-p] + '.' + result[-p:]
        print('Your converted number is... ' + str(user_input) + ' is ' + str(result))
    convert_num()



