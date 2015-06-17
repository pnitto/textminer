import re


def words(input):
    word = r'\w+\d*\w'
    return re.findall(word,input)
##might need re.split()

#def phone_numbers(input):
 #   phone_number = r'(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})'
 #   print({"area_code" : " ", "number" : " "})
 #   return re.findall(phone_number, input)


def money(input):
    money_1 =