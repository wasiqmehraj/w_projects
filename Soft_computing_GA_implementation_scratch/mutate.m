function mutant=mutate(pop,del)
% MUTATION function to performs the process of a 
% randomized mutation
r= rand           %random number used in mutation (0 to 1)

mutant=pop+((r-0.5)*del)

end