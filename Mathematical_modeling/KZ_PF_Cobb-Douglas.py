import numpy as np

''' Kirill Zakharov
    Cobb-Douglas production function'''

#data
listY = np.array([83278,90884,83743,91530,101313,116415,127434,136274,146470,\
145052,140288,142022,149895,147122,163620])
listL = np.array([234236,254890,217606,221746,228757,250238,266469,266154,\
269520,263098,252357,262536,285700,277522,307946])
listK = np.array([73426,77568,70460,75131,79694,89276,97056,101633,100124,\
94920,96671,100072,101304,96784,100352])

#linearization with Ln
lnY = np.log(listY)
lnK = np.log(listK)
lnL = np.log(listL)

#add additional parameters
lnK2 = lnK*lnK
lnL2 = lnL*lnL
lnKlnL = lnK*lnL
lnYlnK = lnY*lnK
lnYlnL = lnY*lnL

#calculate the sums
sumY = np.sum(lnY)
sumK = np.sum(lnK)
sumL = np.sum(lnL)
sumK2 = np.sum(lnK2)
sumL2 = np.sum(lnL2)
sumYK = np.sum(lnYlnK)
sumYL = np.sum(lnYlnL)
sumKL = np.sum(lnKlnL)

#preparing the data
coef_matrix = np.array([[len(listY), sumK, sumL],
                        [sumK, sumK2, sumKL],
                        [sumL, sumKL, sumL2]])

vector = np.array([sumY, sumYK, sumYL]).T

#solve the system
inv_matrix = np.linalg.inv(coef_matrix)

solution = np.dot(inv_matrix, vector)

print(f'A: {np.exp(solution[0])}\nalpha: {solution[1]}\nbeta: {solution[2]}')
