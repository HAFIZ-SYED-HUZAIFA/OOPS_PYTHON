class Counter :
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls,) :
        print(f"Total object is:",cls.count)

c1 = Counter()
c2 = Counter()
c3 = Counter()

c1.show_count()
        