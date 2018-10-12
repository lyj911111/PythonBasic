list = [100, 20, 50, 80, 60]

class Max_Min_Avg:

    def __init__(self):
        self.result = 0

    def Max(self,list):
        list.sort
        Max = list[0]
        self.result = Max
        return self.result

    def Min(self,list):
        list.sort
        Min = list[-1]
        self.result = Min
        return self.result

    def Avg(self,list):
        sum = 0
        for i in range(len(list)):
            sum = sum + list[i]
        avg = sum / len(list)
        return avg

result = Max_Min_Avg()

print(result.Max(list))
print(result.Min(list))
print(result.Avg(list))