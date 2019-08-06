
# 
# Your previous JavaScript content is preserved below:
# 
# /*
# Please write a function to generate a random password:
# It should contain 2 lowercase letters, 2 uppercase letters, two numerals,
# and two special characters of !@#$%^&*
# 
# It should be sufficiently scrambled so that the different categories are not located next to each other.
# 
# Example good result: 8&bN6!zU
# Example bad result: AByu74$^ (categories adjacent to one another)
# */
# 
# 
# 
# 7yUj6b^&

import random 

def generate_pass():  
    password_list = []
    res = ''
    password_list.append(random.choice(lower))
    
    password_list.append(random.choice(upper))
    password_list.append(random.choice(lower))
    
    password_list.append(random.choice(number))
    password_list.append(random.choice(upper))
        
    password_list.append(random.choice(special))
    password_list.append(random.choice(number))
    password_list.append(random.choice(special))

    prev = ''
    while(len(password_list) != 0):        
        char = random.choice(password_list)   
        if is_valid_char_v2(char, prev):
            prev = char
            res+=char        
            password_list.remove(char)
        elif not is_valid_char_v2(char, prev) and len(res) == 7:
            res = char + res
            password_list.remove(char)
        
    return res        
'''
def is_valid_char(char, prev):
    if prev != '':
            if ord('0') <= ord(char) <= ord('9'):
                if ord('0') <= ord(prev) <= ord('9'):
                    return False
                
            if ord('A') <= ord(char) <= ord('Z'):                
                if ord('A') <= ord(prev) <= ord('Z'):
                    return False
                                
            if ord('a') <= ord(char) <= ord('z'):
                if ord('a') <= ord(prev) <= ord('z'):
                    return False
                
            if ord('!') <= ord(char) <= ord('$') or char == '@':
                if ord('!') <= ord(prev) <= ord('$') or prev == '@':
                    return False                                
    return True
'''
def is_valid_char_v2(char, prev):
    if prev == '':
        return True
    
    if char in lower_dict and prev in lower_dict:
        return False
                
    if char in upper_dict and prev in upper_dict:
        return False
    
    if char in number_dict and prev in number_dict:
        return False
    
    if char in special_dict and prev in special_dict:
        return False
        
    return True

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '1234567890'
special = '!@#$%^&*'

lower_dict = {}
upper_dict = {}
number_dict = {}
special_dict = {}

for c in lower:
    lower_dict[c] = 1
    
for c in upper:
    upper_dict[c] = 1

for c in number:
    number_dict[c] = 1

for c in special:
    special_dict[c] = 1
    
  
for _ in range(10):
    print(generate_pass())
    
    
    



