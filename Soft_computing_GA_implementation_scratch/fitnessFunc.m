function fitness = fitnessFunc(x)

%Sphere
 fitness=sum(x(1)^2+x(2)^2+x(3)^2);
 fitness=1/(1+fitness)
 

end