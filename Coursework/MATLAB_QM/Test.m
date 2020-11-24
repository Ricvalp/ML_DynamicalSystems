%% Test for the function Mybubblesort
%To test the function we compare it to the Matlab built-in sort() by
%applying both of them to the same array of random numbers and plotting the
%result on the same axis.

%Length of the array of random numbers
L = 50;
%X-axis
x = [1:L];
%Array of random numbers
yrand = randi(L,1,L);
%Sorted arrays
Mysort = Mybubblesort(yrand);
ysort = sort(yrand);
figure
%Current axes
ax1=gca;
%Generating the plot
plot(x,yrand,'-.O', x, Mysort,'-.c*', x, ysort, '--x')
%Labelling the axes
ylabel('y')
xlabel('x')
%setting y limits
ax1.YLim=[0 L+10];
%Removing the box outline around the current axes 
ax1.Box='off';
title('Randomly generated numbers')
%Displaying grid lines
grid on
%Legend dispalyed on the top-right corner
legend('Random','Sorted by Mybubblesort','Sorted using sort','Position',[0.6 0.8 0.1 0.1])
hold off
%% Test for the function Mysqrt
%To test the function we compare it to the Matlab built-in sqrt() by
%applying both of them to the same values. The results are plotted on the same
%axis.

%Array of 50 values
x = linspace(0,12,100);
figure
%Current axes
ax1=gca;
%Generating the plot
plot(x,sqrt(x), '--' , x, arrayfun(@Mysqrt,x), 'x')
hold on;
%Labelling the axes
ylabel('y')
xlabel('x')
%Removing the box outline around the current axes 
ax1.Box='off';
title('Square root')
%Displaying grid lines
grid on
%Legend displayed on the top-left corner
legend('Built-in function','Mysqrt','Position',[0.3 0.8 0.1 0.1])
hold off