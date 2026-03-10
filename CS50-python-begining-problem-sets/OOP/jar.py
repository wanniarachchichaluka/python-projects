import sys
class Jar:
    def __init__(self,capacity=12):
        self.capacity=int(capacity)
        self._size=0

    def __str__(self):
        return f"{self.size*'🍪'}"
    
    def deposit(self,n):
        n=int(n)
        if self._size+n>self.capacity:
            raise ValueError("too much size")
        self._size+=n

    def withdraw(self,n):
        n=int(n)
        if self._size<n:
            raise ValueError("Not that much size")
        self._size-=n

    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self,capacity):
        if int(capacity) <0:
            raise ValueError("Capacity should be a non-negative int")
        self._capacity=int(capacity)  

def main():
    try:
        capacity = input("Capacity: ")
        n = input("cookies: ")
        m = input("eating: ")
        jar = Jar(capacity)
        jar.deposit(n)
        jar.withdraw(m)
        print(jar)
    except ValueError as e:
        sys.exit(e)

if __name__=="__main__":
    main()
