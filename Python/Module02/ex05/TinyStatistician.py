from math import sqrt


class TynyStatistician:

    def __init__(self) -> None:
        pass

    def mean(self,x : list[int]) -> float:
        sum : int = 0
        for m,value in enumerate(x):
            sum = sum + value
        return sum/(m+1)
    
    def median(self,x: list[int]) -> float:
        x.sort()
        n = len(x)
        if n % 2 == 0:
            n = int(n/2)
            return float(x[n-1]+x[0-n])/2
        else:
            n = int(n/2)
            return float(x[n])
    
    def quartiles(self,x : list[int], percentile : int) -> float:
        x.sort()
        if percentile == 0:
            return float(x[0])

        elif percentile == 25:
            rang = (len(x) + 3)
            if rang % 4 == 0:
                rang = int(rang/4)
                return float(x[rang])
            else:
                rang = int(rang/4)
                return float(x[int(rang)-1]+x[int(rang)])/2
        elif percentile == 50:
            return self.median(x)

        elif percentile == 75:
            rang = (3*len(x) + 1)
            if rang % 4 == 0:
                rang = int(rang/4)
                return float(x[rang-1])
            else:
                rang = int(rang/4)
                return float(x[rang-1]+x[rang])/2

        elif percentile == 100:
            return float(x[-1])

    def var(self,x : list[int]) -> float:
        sum_1 : int = 0 
        mean_ = self.mean(x)
        for value in x:
            sum_1 = sum_1 + ((value - mean_) ** 2)
        
        return float(sum_1/len(x))

    def std(self,x : list[int]) -> float:
        return sqrt(self.var(x))


t = TynyStatistician()
a = [1,42,300,10,59]
print(
    t.mean(a),
    t.median(a),
    t.quartiles(a,25),
    t.quartiles(a,75),
    t.var(a), 
    t.std(a),sep='\n'
)