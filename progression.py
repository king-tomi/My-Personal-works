class Progression:
    
    def __init__(self,start=0):
        self.current = start
        
    def advance(self):
        self.current += 1
        
    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            answer = self.current
            self.advance()
            return answer
            
    def __iter__(self):
        return self
        
    def print_progression(self):
        print(" ".join(str(next(self) for j in range(self.current))))
        
    
    
class ArithmeticProgression(Progression):
    
    def __init__(self,start,increment=1):
        super().__init__(start)
        self.increment = increment
        
    def advance(self):
        self.current += self.increment
        
        
class GeometricProgression(Progression):
    
    def __init__(self,start,base=2):
        super().__init__(start)
        self.increment = base
        
    def advance(self):
        self.current *= self.increment
        
        
        
        
        
        
if __name__ == "__main__":
    progress = Progression(5)
    arith = ArithmeticProgression(start=5)
    progress.advance()
    arith.advance()
    i = iter(progress)
    j = iter(arith)
    for k in i:
        print(k)