import random
class LoadBalancer:
    def __init__(self, in_lst):
        self.in_array = in_lst

    def get_server(self):
        max_val = 0
        out_id = -1
        for id, val in enumerate(self.in_array):
            val = (val/100)* random.random()
            if val > max_val:
                max_val = val
                out_id = id
        return out_id


if __name__ == '__main__':
    lb = LoadBalancer([10,40,50])
    print(lb.get_server())