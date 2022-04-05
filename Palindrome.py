def is_it_palindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

zmienna = is_it_palindrome("kajak")
print(zmienna)