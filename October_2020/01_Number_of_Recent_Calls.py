class RecentCounter:

    def __init__(self):
        self.num_list = []

    def ping(self, t: int) -> int:
        count = 0
        self.num_list.append(t)
        delete = 0
        for index, i in enumerate(self.num_list):
            if(i < t - 3000):
                delete = index + 1
        del self.num_list[:delete]
        return int(len(self.num_list))


        # Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = []
param_1.append(obj.ping(1))
param_1.append(obj.ping(100))
param_1.append(obj.ping(3001))
param_1.append(obj.ping(3002))
print(param_1)
