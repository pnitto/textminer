import re

def binary(v):
    regr = re.findall(r'\b[01]+\b',v)
    if len(v) == 0:
        return False
    if len(regr) > 0:
        return True

def binary_even(v):
    even_binary = r'[0-1]+0$'
    if re.match(even_binary,v):
        return True


def hex(hexnum):
  answer = bool
  express = re.findall(r"[a-fA-F0-9]", hexnum)
  original = [_ for _ in hexnum]
  new = [_ for _ in express]
  if len(hexnum) == 0:
      answer = False
  else:
      answer = len(original) == len(new)
  return answer

def word(single):
    return re.search(r'^[A-Za-z\d/-]+[A-Za-z]$', single)

def phone_number(number):
  answer = bool
  new = re.findall(r'[\d{3}\d{3}\d{4}]', number)
  print(new)
  if len(new) == 10:
      answer = True
  else:
      answer = False
  return answer

def zipcode(z):
    postal_code = re.match('^\d{5}(-\d{4})?$', z)
    return postal_code

def money(y):
    if len(y) < 2:
        return False
    if re.fullmatch(r"\$.*\.\d{1}|\$.*\.\d{3}|\${2}\d.*|\$\d*,\d{1,2}|\d+", y):
        return False
    else:
        return True

def words(x):
    pass

def date(dates):
    return re.search(r'^(\d{1,4}[/-]){2}\d{1,4}$', dates)
