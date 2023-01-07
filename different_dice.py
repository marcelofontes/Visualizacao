from die import Die
import pygal

#cria um D6 e um D10

die_1 = Die()
die_2 = Die(10)

#faz alguns lançamentos  e armazena os resultados em uma lista
results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analisa os resultados
frequencies = []
max_reusult = die_1.num_sides + die_2.num_sides
for value in range(1, max_reusult+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualiza os resultados
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = ['','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice.svg')
hist.render_in_browser()