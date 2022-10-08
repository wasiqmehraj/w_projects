function offspring=crossover(male,female)
% CROSSOVER function to perform crossover of parent genomes to 
% produce offspring
alpha=0.6;
beta=0.4;
offspring=(alpha*male)+(beta*female);
end