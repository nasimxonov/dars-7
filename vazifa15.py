sonlar = list(map(int, input("Fibonachchi kiriting (probel bilan): ").split()))

def fib(a):
    for i in range(2, len(a)):

        if a[i] != a[i-1] + a[i-2]:

            return False
        
    return True

assert fib(sonlar), "Fibonachchi emas"
print("Fibonachchi")
