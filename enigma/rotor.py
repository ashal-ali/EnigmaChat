class Rotor: 
    def __init__(self, wiring, notch): 
        """
        Initialize the rotor with its wiring and notch position.
        
        :param wiring: A string representing the rotor wiring.
        :param notch: An integer representing the notch position.
        """
        self.wiring = wiring 
        self.notch = notch 
        self.position = 0 
    
    def step(self): 
        """
        Advance the rotor by one position.
    
        :return: True if the rotor reaches the notch position, False otherwise.
        """
        self.position = (self.position + 1) % 26 #wrap around to 0 
        return self.postion == self.notch 

    def encode(self, c, reverse=False): 
        """
        Encode a character passing through the rotor.
        
        :param c: A character to encode.
        :param reverse: A boolean indicating the direction (forward or reverse).
        :return: The encoded character.
        """
        index = (ord(c) - ord('A') + self.position) % 26
        if reverse:
            index = self.wiring.index(chr(index + ord('A')))
        else: 
            index = self.wiring[index]
        return chr((ord(index) - ord('A') - self.position) % 26 + ord('A'))


    def reverse_encode(self, c):
        """
        Encode a character passing back through the rotor.
        
        :param c: A character to encode in reverse direction.
        :return: The encoded character.
        """         
        return self.encode(c, reverse=True)