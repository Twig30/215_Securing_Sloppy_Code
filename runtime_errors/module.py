def isdigit(string):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    index = 0
   
   #if the string has any letters return false
    while index <= len(string)-1:
     number = string[index].lower()
     print(number)
     if number in digits:
        count+=1
        return True
    
     else: 
        return False

    index += 1
    return count
   
    '''for char in string:
        if char in digits:
            return True
        if char !in digits:
            return False'''
   #if the string has only numbers return true