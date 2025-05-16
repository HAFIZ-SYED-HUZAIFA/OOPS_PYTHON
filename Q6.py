class Logger :

    def __init__(self):
        print("Logger object is created")
    
    def __del__(self):
        print("logger object is destroyed")

log1 = Logger()