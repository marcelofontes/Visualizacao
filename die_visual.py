import pygal
from die import Die

#cria cria dois dados D6

die_1 = Die()
die_2 = Die()

#faz alguns lançamentos e armazena os resultados em uma lista
results= []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    print(results)

#analisa os resultados de frequencias
frequencies = []
max_reusult = die_1.num_sides + die_2.num_sides
for value in range(1, max_reusult+1):
    frequency = results.count(value)
    frequencies.append(frequency)

    #visualiza os resultados
hist = pygal.Bar()
hist.title = "Results for rolling one D6 100 times."
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title= "Frequency of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
