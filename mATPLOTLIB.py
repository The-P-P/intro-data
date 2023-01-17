import matplotlib.pyplot as plt
x = list(range(1, 9))
print(x)
notas_matematica = [8, 7, 7, 8, 9, 3, 2, 8]
y = notas_matematica
print(y)

plt.plot(x,y, marker = 'o')
plt.title('notas de matematica')
plt.xlabel('provas')
plt.ylabel('notas')
plt.show()  