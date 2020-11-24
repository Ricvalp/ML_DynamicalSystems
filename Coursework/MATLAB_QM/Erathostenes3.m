%This script determine all prime numbers between 1 and n using the Seive of
%the Eratosthenes. 

n = input('Determine all prime numbers between 1 and n = '); %input n
numberArray = [1:n];      % initialize the vector
numberArray(1) = 0;    % setting the first element to zero


for k = 2:sqrt(n) %it's sufficient to iterate over all the numbers between 2 (the smallest prime) and sqrt(n)
    for m = 2:n/k
        numberArray(m*k)=0;
    end
end

primeNumbers = []; % initialization of the vector

% This loop collects only the primes in a new vector primeNumbers.
for i = 1:1:n
    if numberArray(i) ~=0
        primeNumbers = [primeNumbers, i];
    end
end

fmt=[repmat(' %1.0u, ' , 1 , numel(primeNumbers))];
fprintf('List of all prime numbers between 1 and %u: ', n)
fprintf(fmt,primeNumbers(1:end-1))
fprintf('%u:', primeNumbers(end))