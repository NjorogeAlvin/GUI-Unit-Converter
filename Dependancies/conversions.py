class LengthConverter:
        def __init__(self, metres):
            self.metres = metres
            
        def metres_to_kilometres(self,):
            return self.metres / 1000
    
        def metres_to_centimetres(self,):
            return self.metres * 100
    
        def metres_to_feet(self,):
            return self.metres * 3.28084

        def metres_to_inches(self,):
            return self.metres * 39.370
        
        def metres_to_yards(self,):
            return self.metres * 1.09361

