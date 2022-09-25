import numpy as np
import random

g_no = 2  # int(input('Number of genes you want to have in your individual?\n'))
p_no = 5  # int(input('Population?\n'))
r_max = 5  # int(input('Select MAX value of gene: '))
r_min = -5  # int(input('Select MIN value of gene: '))
f = 0.5  # Scaling Factor
p_cr = 0.7  # Crossover Probability
t = 7 # number of iterations of DE you want to run.

def in_there_func(j, i_bag):
    in_there = False
    for element in i_bag:
        if j == element:
            in_there = True
    return in_there


def cromo_fitness(cromo):
    fit = (cromo[0]) ** 2 + (cromo[1]) ** 2
    return fit


def fitness(pop_mat):
    i = 0
    fit_list_main = []
    while i < p_no:
        cromo = pop_mat[i]
        fit = cromo_fitness(cromo)
        fit_list_main.append(fit)
        i += 1
    return fit_list_main


def select(i):
    """This function is to produce different elements in the vector called players here"""
    # players=[par_i, tar_i, rs1_i, rs2_i]
    players = [i]
    count = 0
    bag = []
    while count < p_no:
        bag.append(count)
        count += 1
    # bag = [0 1 2 3 .. p_no]

    bag.remove(players[0])  # remove players[0] = i from bag

    tar_i = random.choice(bag)
    players.append(tar_i)  # append players ----> players =[i,tar_i]
    bag.remove(tar_i)  # remove tar_i from bag

    rs1_i = random.choice(bag)
    players.append(rs1_i)  # append players -----> players=[i,tar_i, rs_1]
    bag.remove(rs1_i)  # remove rs_1 from bag

    rs2_i = random.choice(bag)
    players.append(rs2_i)  # append players -----> players=[i,tar_i, rs_1, rs_2]

    return players


def cromo_mutation(i, pop_mat):
    players = select(i)
    # We have selected different index for parent, target vector, rand_sel_sol_1, rand_sel_sol_2
    trial_vect = np.subtract(pop_mat[players[2]], pop_mat[players[3]])
    trial_vect = np.multiply(f, trial_vect)
    trial_vect = np.add(trial_vect, pop_mat[players[1]])
    return trial_vect


def mutation(pop_mat):
    i = 0
    trial_vect_mat = []
    while i <= p_no - 1:
        trial_vect = cromo_mutation(i, pop_mat)
        trial_vect_mat.append(trial_vect)
        i += 1
    return trial_vect_mat


def crossover(trial_vect_mat, pop_mat):
    '''It will give offspring'''
    #  Do not leave it to luck that random will put something in it. If it becomes phi then no DE will occur.
    i_bag = [1]
    for j in range(g_no):
        in_there = in_there_func(j, i_bag)
        if random.random() < p_cr and in_there == False:
            i_bag.append(j)

    offspring = pop_mat
    for i in range(p_no):
        for j in range(g_no):
            in_there = in_there_func(j, i_bag)
            if in_there:
                offspring[i][j] = trial_vect_mat[i][j]
    # Greedy Selection
    for i in range(p_no):
        if cromo_fitness(offspring[i]) > cromo_fitness(pop_mat[i]):
            offspring[i] = pop_mat[i]

    return offspring


def diff_evolution(pop_mat,itrs):
    trial_vect_mat = mutation(pop_mat)  # This is to perform mutation
    offspring = crossover(trial_vect_mat, pop_mat)  # This is to perform crossover

    # print(f"Offspring generation : {itrs}\n", offspring)
    # print(f"Fitness matrix for iteration {itrs}: \n", fitness(offspring))
    print(f"Min Fitness matrix for iteration: {itrs}: ", min(fitness(offspring)))

    return offspring


# Initialize population matrix :
pop_mat = np.random.randint(r_min, r_max, size=(p_no, g_no))
# print("initial population is : ", pop_mat)
# print("Fitness for iteration: 0 \n", fitness(pop_mat))
print(f"Min Fitness matrix for iteration 0 : ", min(fitness(pop_mat)))
print('*****************************************************************')

itrs = 1
while itrs <= t:
    offspring = diff_evolution(pop_mat, itrs)
    pop_mat = offspring
    itrs += 1
    print('*****************************************************************')

print('This tool is awesome!!')