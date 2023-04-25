#Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
#The program will create two other text file; 
#The first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
#The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.  

#open files named: numbers.txt file (read), even.txt file (append), odd.txt file (append)
with open("numbers.txt") as main_file, open("even.txt", "a") as extracted_even_nums,  open("odd.txt", "a") as extracted_odd_nums:
    #read the numbers.txt file line by line
    for line in main_file:
        print(line.strip())
#check each lines of numbers.txt
#IF the line has even number,
    #THEN extract this number and append/write to even.txt file
#ELSE, if the line has odd number,
    #THEN extract this number and append/write to odd.txt file