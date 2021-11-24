class Shortening:
    def __init__(self,n):
        # TODO

    def add_edge(self,a,b,x):
        # TODO

    def check(self,a,b):
        # TODO

if __name__ == "__main__":
    s = Shortening(5)
    print(s.check(1,3)) # False
    s.add_edge(1,2,5)
    s.add_edge(2,3,-2)
    print(s.check(1,3)) # False
    s.add_edge(2,4,1)
    s.add_edge(4,2,-2)
    print(s.check(1,3)) # True