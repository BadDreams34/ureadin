import time
import os
import datetime
print("YOOUR POMO FRIEND")
import pathlib
# must counts how many pomos i did today and store them in a .txt file UMM
# and this log should be there always and in this timer i must have the
# option to make the timer stoop so whenver i stop just log that time
# and enter the number of minutes for which to keep the timer and also
# YEAHH ?
BREAK_MIN = 5
FILE = pathlib.Path(__file__).parent / "files" / "progress.txt"
mins_foc= 0


def main():
    global mins_foc
    try:

        while True:
            t = input("How many minutes are you going to study !? ")
            if t.isdecimal():
                print(f" NOOOT Alright, Good Luck your next 50 minutes ? !!!! IS A HECKING WRONG SHIT LOL !!!\n"
                      f"Alright, ... ! ")
                t = int(t)
                break

        # ok start the timer or rather start in BREAK_MIN minutes
        i = 60 * BREAK_MIN
        while i>=0:
            # print hours mins and seconds bro
            time_format(i)
            print(" "*5) 
            i -=1
            time.sleep(1)
        # just set i = desired t

        FOCUS_TIME = t * 60
        ft = FOCUS_TIME
        while mins_foc <=FOCUS_TIME:
            time_format(ft)
            ft -=1
            print(" "* 5)
            mins_foc+= 1

            time.sleep(1)

        with open(FILE, "a+") as file:
            tim = datetime.datetime.now()
            date_time = tim.strftime("%D, %H:%M:%S")
            file.write(f"{date_time}\n{t} mins\n")
            file.write("\n-------------------------------------\n")

    except KeyboardInterrupt:
        print(" You Quitted, Dont worry Your focus minutes has been saved !")

        with open(FILE, "a+") as file:
            tim = datetime.datetime.now()
            date_time = tim.strftime("%D, %H:%M:%S")
            file.write(f"{date_time}\n{mins_foc//60} mins\n")
            file.write("\n-------------------------------------\n")


def time_format(sec):
    H = sec // 3600
    M = (sec % 3600) // 60
    S = sec % (3600) % 60
    print(f"{H:02d}:{M:02d}:{S:02d}")

if __name__ == "__main__":
    main()
