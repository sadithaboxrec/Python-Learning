import time

def main():
    timerCal()
    print("Time is Over")


def timerCal():

    while True:
        try:
            timer=int(input("Enter the time in seconds: "))

            if timer < 0:
                print("Enter a positive number")
                continue

            break

        except ValueError:
            print("Enter an Number")


    # for i in reversed(range(0,timer)):
    for i in range(timer, 0, -1):

        seconds = i % 60  # getting actual seconds
        minutes = int(i / 60) % 60   # If i = 500: 500 / 60 = 8.33 → int = 8     8 % 60 = 8 minutes
        hours = int(i / 3600)        # 3665 / 3600 ≈ 1.01 → int = 1 hour

        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)


main()
