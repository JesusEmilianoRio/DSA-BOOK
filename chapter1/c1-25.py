def replace_char(string):
    replace_letters= ',.'
 
    for chars in string:
        if chars in replace_letters:
            string = string.replace(chars, "")
   
    return string
