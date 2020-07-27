
game_started = True
start_count = 0
stop_count = 0
# Mosh used while True:
while game_started:
    case = input(">")
    if case.lower() == "start":
        stop_count = 0
        if start_count == 0:
            print("Car started...Ready to go!")
            start_count += 1
        else:
            print("Car is already started! ")
    elif case.lower() == "stop":
        start_count = 0
        if stop_count == 0:
            print("Car stopped.")
            stop_count += 1
        else:
            print("Car is already stopped! ")
    elif case.lower() == "help":
        """ This is what i did 
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit") """

        # Mosh
        print("""
start - to start the ca
stop - to stop the car
quit - to exit
        """)
    elif case.lower() == "quit":
        break
    else:
        print("I dont understand that...")

        """
        TO add the already started and stopped mosh used
        boolean 
        started = False
        if case == "start:
            if started:
                print("Car is already started!")
            else:
                started = True
                print("Car started...")
            
        elif case == "stop":
            if not started:
                print("Car is already stopped")
            else:
                started = False
                print("Car stopped")
                
        
        """