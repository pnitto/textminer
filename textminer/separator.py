import re


def words(w):
    if len(re.findall(r"[a-zA-Z]", w)) > 0:
        return w.split()

def phone_number(v):
    return re.fullmatch(r'[\d({3})\d{3}\d{4}]', v)


def money(x):
    if len(x) < 2:
        return None
    if re.fullmatch(r"\$.*\.\d{1}|\$.*\.\d{3}|\${2}\d.*|\$\d*,\d{1,2}|\d+", x):
        return None
    else:
        cleantext = ''.join((re.findall(r"[\d\.]", x)))
        print(cleantext)
        return{"currency": "$", "amount": float(cleantext)}


def zip_code(address):
       if len(re.findall(r"[\d]", address)) == 9 or len(re.findall(r"[\d]", address)) == 5:
        cleantext = ''.join((re.findall(r"[\d]", address)))
        print(cleantext)
        zip = re.findall(r"^\d{5}", cleantext)
        number = cleantext[5:]
        if number == '':
            number = None
        else:
            number = ''.join(number)
        return {"zip": ''.join(zip), "plus4": number}

def date(d):
    date = re.search(r'(\d+/\d+/\d+)', d)
    return date

def emails(w):
     return re.findall(r"[a-z\.]*\@[a-z\.]*", w)
