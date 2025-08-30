def is_isbn(isbn:str)->bool:

    """
    Checks if a given ISBN-10 string is valid.
    
    Parameters:
    isbn (str): The ISBN-10 string to validate. Can contain hyphens.
    
    Returns:
    bool: True if valid, False otherwise.
    """
    isbn = isbn.replace('-','')
    if len(isbn) != 10:
        return False

    total = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        else:
            total += int(isbn[i])* (10-i)

    if isbn[9]=='X':
        total +=10
    elif isbn[9].isdigit():
        total += int(isbn[9])
    else:
        return False
    
    return total %11 ==0


#Example Useage
if __name__ =="__main__":

   test_cases = [
    "3-598-21508-9",
    "3-598-21508-8",
    "359821507X",
    "359821507A"
   ]
   for test in test_cases:
        print(f"{test} is verified ISBN: {is_isbn(test)}")



    