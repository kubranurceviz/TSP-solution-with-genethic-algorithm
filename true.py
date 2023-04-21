# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:08:15 2023

@author: Kübra Nur Ceviz
"""

import random
import time
import math

start_time = time.time() # süre ölçümünün başlatılması 
# Şehirlerin koordinatları
cities = []

# Verileri dosyadan oku ve cities listesine ekle
with open("tsp_85900_1", "r") as f:
    next(f)  # İlk satırı atla
    for line in f:
        x, y = map(float, line.strip().split())
        cities.append((x, y))

# Popülasyon boyutu ve genlerin uzunluğu
POPULATION_SIZE = 100
GENE_LENGTH = len(cities)

# Fitness fonksiyonu
def fitness(individual):
    distance = 0
    for i in range(GENE_LENGTH - 1):
        city_a = cities[individual[i]]
        city_b = cities[individual[i+1]]
        distance += math.sqrt((city_a[0]-city_b[0])**2 + (city_a[1]-city_b[1])**2)
    # Başlangıç noktasına geri dönme
    city_a = cities[individual[GENE_LENGTH - 1]]
    city_b = cities[individual[0]]
    distance += math.sqrt((city_a[0]-city_b[0])**2 + (city_a[1]-city_b[1])**2)
    return distance

# Başlangıç popülasyonu oluşturma
population = []
for i in range(POPULATION_SIZE):
    individual = list(range(GENE_LENGTH))
    random.shuffle(individual)
    population.append(individual)

# Genetik algoritmayı uygulama
for generation in range(100):
    # Fitness değerlerini hesaplama
    fitness_values = [fitness(individual) for individual in population]

    # Seçilim: turnuva seçimi
    tournament_size = 5
    selected = []
    for i in range(POPULATION_SIZE):
        tournament = random.sample(range(POPULATION_SIZE), tournament_size)
        winner = tournament[0]
        for j in range(1, tournament_size):
            if fitness_values[tournament[j]] < fitness_values[winner]:
                winner = tournament[j]
        selected.append(population[winner])

    # Çaprazlama: tek noktalı çaprazlama
    offspring = []
    for i in range(0, POPULATION_SIZE, 2):
        parent_1 = selected[i]
        parent_2 = selected[i+1]
        crossover_point = random.randint(0, GENE_LENGTH-1)
        child_1 = parent_1[:crossover_point] + [x for x in parent_2 if x not in parent_1[:crossover_point]]
        child_2 = parent_2[:crossover_point] + [x for x in parent_1 if x not in parent_2[:crossover_point]]
        offspring.append(child_1)
        offspring.append(child_2)

    # Mutasyon: swap mutasyonu
    mutation_rate = 0.01
    for i in range(POPULATION_SIZE):
        if random.random() < mutation_rate:
            mutation_point_1 = random.randint(0, GENE_LENGTH-1)
            mutation_point_2 = random.randint(0, GENE_LENGTH-1)
            population[i][mutation_point_1], population[i][mutation_point_2] = population[i][mutation_point_2], population[i][mutation_point_1]


    # Yeni nesil için popülasyonu güncelleme
    population = offspring

# En iyi bireyi bulma
best_individual = min(population, key=fitness)
best_distance = fitness(best_individual)

   
        
end_time = time.time() # süre ölçümünün bitirilmesi
run_time = end_time - start_time # geçen sürenin hesaplanması
       
    
   

