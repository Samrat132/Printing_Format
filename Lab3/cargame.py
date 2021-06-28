'''
  Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
          >start
           Car had already started!!
        > stop
          Car stopped..
          >stop
           Car had already stopped!!
        > quit
'''
value = ""
started = False

while True:
    value = input("> ").lower()
    if value == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif value == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif value == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
    """)
    elif value == "quit":
        break
    else:
        print("Sorry, I don't understand that.")