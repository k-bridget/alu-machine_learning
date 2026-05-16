#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

people = ['Farrah', 'Fred', 'Felicia']
apples, bananas, oranges, peaches = fruit

x = np.arange(len(people))
width = 0.5

plt.bar(x, apples, width, color='red', label='Apples')
plt.bar(x, bananas, width, bottom=apples, color='yellow', label='Bananas')
plt.bar(x, oranges, width, bottom=apples + bananas, color='#ff8000', label='Oranges')
plt.bar(x, peaches, width, bottom=apples + bananas + oranges, color='#ffe5b4', label='Peaches')

plt.xticks(x, people)
plt.ylabel("Quantity of Fruit")
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.title("Number of Fruit per Person")
plt.legend()

plt.show()
