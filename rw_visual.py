import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    #cria um passeio aleatorio e plota os pontos 
   
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(figsize=(10,6)) 

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = plt.cm.Blues, edgecolor ='none', s=1)
 
    #enfatiza o primeiro e o ultimo ponto 
    plt.scatter(0,0, c='green',edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #remove os eixos
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    #plt.axis('off')
    plt.show()

    keep_running = input("make another walk? (y/n):")
    if keep_running == 'n':
        break



