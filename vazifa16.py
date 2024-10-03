n = list(map(int, input("Sonlarni ketme ketlikda kiriting(probel bilan): ").split()))

assert all(n[i] <= n[i+1] for i in range(len(n) - 1)), "Ketma ketlikda emas"

print("Ketma ketlikda")
