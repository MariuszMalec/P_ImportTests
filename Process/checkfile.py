import os, sys

module = os.path.join(os.getcwd(), r'Logger')
sys.path.insert(0, module) #to musi byc jesli mamy modul w innym katalogu
import P_Logger

def Check(file):
    if not (os.path.exists(file)):
        P_Logger.logger.error("Brak pliku => " + file)
        exit(1)

def main():    
    file = r'./Source/B12345651.SPF'
    Check(file)

if __name__ == '__main__':
    main()        
