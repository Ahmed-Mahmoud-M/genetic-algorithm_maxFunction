import random 




def fitness(num):
    return int(num,2) * int(num,2)



def integar_representation(num:list):
    result = []
    for element in num:
        result.append( int(element,2))

    return result


def binary_representation(num:list):
    result = []

    for element in num:
        result.append(bin(element)[2:].zfill(5))

    return result

        

def encoded(num):
    return bin(num)[2:].zfill(5)


def crossover(firstchromosome, secondchromosome,k=2):
    first_offspring,secondoffspring = firstchromosome[:k] + secondchromosome[k:], secondchromosome[:k] + firstchromosome[k:]


    return [first_offspring, secondoffspring]


# helper function to use in mutation
def flip(chromsome: str, flippingChromosome: str) -> str:
    result = list(chromsome)  
    
    for i in range(len(flippingChromosome)):  
        if flippingChromosome[i] == '1':  
            
            result[i] = '0' if chromsome[i] == '1' else '1'
    
    return "".join(result)  



    
    

def Mutations(population:list):
    Mutations_chromosome_for_flipping = ['00000','10000','00000','00101']
    

    offstring_After_Mutation = [flip(population[i],Mutations_chromosome_for_flipping[i]) for i in range(4)]
    #print(offstring_After_Mutation)


    return offstring_After_Mutation



 

def Evaluation_for_selection(population: list):
    evaluation = [fitness(x) for x in population]
    summation = sum(evaluation)
    average = summation / len(population)
    probability = [x / summation for x in evaluation]
    expected_count = [x / average for x in evaluation]
    actual_count = [round(x) for x in expected_count]
    new_population = []
    
    for count in range(len(actual_count)):
        for _ in range(actual_count[count]):
            new_population.append(population[count])

    # Ensure the new population size matches the original population size
   
    while len(new_population) < len(population):
        new_population.append(random.choice(population))  # Add random individuals if too few

    return new_population


    





def genetic_algorithm():
    # Select initial values
    initial_population = [encoded(x) for x in [12, 25, 5, 19]]
    population = Evaluation_for_selection(initial_population)
    generation = 0
    max_generations = 100000  # Maximum number of generations
    
    while generation < max_generations:
        generation += 1
        # Crossover
        offspring = (
            crossover(population[0], population[1]) +
            crossover(population[2], population[3])
        )
        # Mutation
        offspring = Mutations(offspring)
        # Selection
        population = Evaluation_for_selection(offspring)
        
        # Decode binary strings to integers for evaluation
        decoded_population = integar_representation(population)
        print(f"Generation {generation}: {decoded_population}")
        
        if 30 in decoded_population:
            print(f"Solution found in generation {generation}: {population}")
            break
    else:
        print("Max generations reached. Solution not found.")





    



  

if __name__ == '__main__':
  genetic_algorithm()
