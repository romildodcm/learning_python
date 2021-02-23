#plotando seno

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')

# gerando os dados 
# (inicio, final, step)
x = np.arange(0.0, 2.0, 0.01)
y = np.sin(2*np.pi*x)

#plt.figure(figsize = (10,10))
# Titulos
plt.title('Exemplos de uso da Matplotlib: Função seno')
plt.xlabel('x')
plt.ylabel('Sin(x)')
plt.grid(True)

plt.plot(x, y)
#plt.plot(x, y, color= 'red')
plt.show()

# quero apontar o máximo
# plt.annotate('Máximo', xy=(1.5, 1), xytext=(1.75, 1),
#             arrowprops=dict(facecolor='black', shrink=0.05,
#             )

#plt.show()