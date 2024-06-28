class Rotor: 
    def __init__(self, wiring, notch): 
        """
        Initialize the rotor with its wiring and notch position.
        """
        self.wiring = wiring 
        self.notch = notch 
        self.position = 0 
    
    def step(self): 
        """
        Advance the rotor by one position.
        """
        self.position = (self.position + 1) % 26  # wrap around to 0 
        return self.position == self.notch 

    def encode(self, c, reverse=False): 
        """
        Encode a character through the rotor.
        """
        if reverse:
            index = (ord(c) - ord('A') + self.position) % 26
            wiring_index = self.wiring.index(chr(index + ord('A')))
            result_index = (wiring_index - self.position + 26) % 26
        else:
            index = (ord(c) - ord('A') + self.position) % 26
            wiring_char = self.wiring[index]
            result_index = (ord(wiring_char) - ord('A') - self.position + 26) % 26
        return chr(result_index + ord('A'))

    def reverse_encode(self, c):
        """
        Encode a character through the rotor in reverse direction.
        """
        return self.encode(c, reverse=True)

