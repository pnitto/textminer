import re


def phone_numbers(text):
    phone_number =  r'\(\d{3}\) ?\d{3}-\d{4}'
    return re.findall(phone_number, text)




def emails(text):
    test_emails = r'[\w.\w]+@\w+.\w{3}'
    return re.findall(test_emails, text)
