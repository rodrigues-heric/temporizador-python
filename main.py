import time

def count_time(unity):
    time.sleep(1)
    return unity - 1

def main():
    hours = int(input('Hours: '))
    minutes = int(input('Minutes: '))
    seconds = int(input('Seconds: '))
    time_left = True 

    while time_left:
        print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

        # seconds left
        if seconds != 0:
            seconds = count_time(seconds)

        # if minutes left
        else:
            if minutes != 0:
                minutes = count_time(minutes)
                seconds = 59

            # if hours left
            else:
                if hours != 0:
                    hours = count_time(hours)
                    seconds = minutes = 59

                # time is over
                else:
                    time_left = False

if __name__ == '__main__':
    main()