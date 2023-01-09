
alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7,
            'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
            'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21,
            'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

def encrypt(message, n):
    ''' '''
    
    words_lst = message.strip().split()
    new_lst = []
    
    for word in words_lst:
        
        new_word = ''
        
        for letter in word.strip():
            
            num = alphabet[letter]
            num_shift = num + n
            
            if num_shift > 26:
                num_shift -= (26*(num_shift // 26))
                            
            for item in alphabet.items():
                if item[1] == num_shift:
                    new_word += item[0]
                    
        new_lst.append(new_word)
    
    return " ".join(new_lst)
                    


# encrypt("ghost", 4)
# encrypt('klswx', 22)
            
        
        
    
    