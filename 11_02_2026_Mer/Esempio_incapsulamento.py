class Computer:
    def __init__(self):
        self.__processore = "intel i5" #Attributo privato
        
    def get_processore(self):
        return self.__processore
    
    def set_processore(self, processore):
        self.__processore= processore