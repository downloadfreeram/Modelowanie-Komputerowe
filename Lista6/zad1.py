import numpy as np
import matplotlib.pyplot as plt

# np wykorzystuje algorytm Mersenne-Twistera do generowania losowych liczb
vals = np.random.rand(1_000_000)

# Artykuł Linear congruential generator z wikipedii oraz wartości przykładowe do wzoru dla Borland Delphi, Virtual Pascal
a = 134775813
c = 1
m = 2**32
seed = 1
vals2 = []

for _ in range(1_000_000):
    seed = (a * seed + c) % m
    vals2.append(seed/m)

plt.subplot(1,2,1)
plt.hist(vals, bins = 10000)
plt.title("Histogram 1mln Mersene-Twister")
plt.xlabel("Wartosc")
plt.ylabel("Liczba wystapien")

plt.subplot(1,2,2)
plt.hist(vals2, bins = 10000)
plt.title("Histogram 1mln algorytmem modulo")
plt.xlabel("Wartosc")
plt.ylabel("Liczba wystapien")
plt.show()
