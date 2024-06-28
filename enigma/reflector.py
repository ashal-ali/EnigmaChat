class Reflector: 
    def __init__(self, wiring):
        '''
        Initialize the Reflector class
        ''' 
        self.wiring = wiring 
    
    def reflect(self,input):
        '''
        The reflect method gets the index of the char in the alphabet and then gets the corresponding char from wiring.
        '''
        index = (ord(input.upper()) - ord('A')) % 26  # Get index of char in alphabet
        result = self.wiring[index]
        return result
    


    