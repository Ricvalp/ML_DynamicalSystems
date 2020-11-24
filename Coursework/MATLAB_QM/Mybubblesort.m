%Mybubblesort sorts an input vector to ascending order by means of the
%Bubble algorithm. The input is a vector. The output is the vector with the
%elements sorted in ascending order.

function xout = Mybubblesort(x)
for j = 1:length(x)
    for i = 1:length(x)-1
        if x(i) > x(i+1)
            c = x(i);
            x(i) = x(i+1);
            x(i+1) = c;
        end     
    end   
end
xout = x; 
end