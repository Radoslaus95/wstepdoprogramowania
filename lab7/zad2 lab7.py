import numpy as np
macierz = np.random.randint(low = 0, high = 10, size = (5,5))
print(macierz)
print('Max: ', macierz.max())
print('Min: ', macierz.min())

print('Max in rows: ',macierz.max(axis=1))
print('Min in cols: ',macierz.min(axis=0))

print('Sum in rows: ',macierz.sum(axis=1))
