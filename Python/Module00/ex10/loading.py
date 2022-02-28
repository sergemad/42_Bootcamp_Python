import time

def loading() -> None:
    listy = range(500)
    ret = 0
    time_to_sleep = 0.01
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(time_to_sleep)
        first_str = '['
        percent = int((ret/(2*len(listy)))*100)
        print(f"ETA: {len(listy)*time_to_sleep}s [{percent}%]" , end='')
        print(first_str.ljust(int(percent/10),'=') , end = '>')
        print(''.ljust(10 - int(percent/10),' ') , end= '')
        print(f"] {ret/2}/{len(listy)} | elapsed time {ret*time_to_sleep/2}s")
    print(ret)

def ft_progress(list):
    for i in list:
        yield i

def main():
    loading()

main()