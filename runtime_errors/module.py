def isdigit(string):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
   
   #if the string has any letters return false
    for char in string:
        if char in digits:
            return True
        if char !in digits:
            return False
   #if the string has only numbers return true