function newP=limiter(P,VarHigh,VarLow)
% LIMITER Function to perfrom range limit operation on the solution
% to be within the search space bounds
%to see if the offspring genes are within bounds

newP=P;

for i=1:length(P)
    if newP(i)>VarHigh(i)
        newP(i)=VarHigh(i);
    elseif newP(i)<VarLow(i)
        newP(i)=VarLow(i);
    end
end
 

end