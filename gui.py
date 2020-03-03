def encrypt(message):
    """A function that encrypts a message given a set of crypts\n
       param: message(string) a string we wish to encrypt
       
       :rtype:  res(a string) with the vowels shifted one position to the right"""
    vowels = {"a" : "e",
              "e" : "i",
              "i" : "o",
              "o" : "u",
              "u" : "a"}
    res = "".join([vowels[char] if char in vowels.keys() else char for char in message.lower()])
    return res