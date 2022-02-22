import time

class loading:
    def __init__(self) -> None:
        self.listy = range(500)
        self.ret = 0
        self.time = 0.01
        for elem in self.listy:
            self.ret += (elem + 3) % 5
            time.sleep(self.time)
            self.ft_progress()
        print()
        print(self.ret)

    def ft_progress(self):
        percent = int((self.ret/(2*len(self.listy)))*100)
        if percent < 10:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][=>         ] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")
        
        elif percent < 20:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][==>        ] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")
        
        elif percent < 30:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][===>       ] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")
        
        elif percent < 40:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][====>      ] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")
        
        elif percent < 50:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][=====>     ] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")
        
        elif percent < 60:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][======>    ] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")
        
        elif percent < 70:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][=======>   ] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")
        
        elif percent < 80:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][========>  ] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")
        
        elif percent < 90:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][=========> ] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")
        
        elif percent < 100:
            print(f"ETA: {len(self.listy)*self.time}s [{percent}%][==========>] {self.ret/2}/{len(self.listy)} | elapsed time {self.ret*self.time/2}s")


def main():
    test = loading()

main()