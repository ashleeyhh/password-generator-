import random
import string
def generate_pass(min,num=True,specialc=True):
  letters= string.ascii_letters
  digits= string.digits
  special = string.punctuation
  characters=letters
  if num:
    characters+=digits
  if specialc:
    characters+=special
  passw = ""
  criteria= False
  hasnum= False
  hasspecial= False
  while not criteria or len(passw)< min:
    new_char = random.choice(characters)
    passw+= new_char
    if new_char in digits:
      hasnum= True
    elif new_char in special:
      hasspecial= True 
    criteria= True
    if num:
      criteria = hasnum
    if specialc:
      criteria = hasnum and hasspecial 
  return passw 
passw = generate_pass(7)
print(passw)
     