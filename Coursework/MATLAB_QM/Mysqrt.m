%Mysqrt   square root.
%   Mysqrt(x) is the square root of the positive real number x

function xout = Mysqrt(x)
msg = 'The argument must be positive';

if x < 0
    error(msg);
end

if x==0
   xout = 0; 
else
    y_old = 0;
    y_new = 1;
    while abs(y_new-y_old)/y_new > 12*eps
        y_old = y_new;
        y_new = (y_new + x/y_new)/2;
    end
xout = y_new;
end