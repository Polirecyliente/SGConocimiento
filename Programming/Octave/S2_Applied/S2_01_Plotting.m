#!/usr/local/bin/octave
%{
    Plotting
%}

cd "/home/jul/SGConocimiento/Octave/S2_Applied"
x = [0:3:24];
y1 = x.^2;
y2 = x.^(1/2);

#T# plot functions with plot(), xlabel(), ylabel(), title(), grid, axis, legend()
plot(x,y1,'m',x,y2,'.-g'),xlabel('indep vals'),ylabel('dep vals'),
title('Square funcs'),grid on,axis equal,legend('square pow','square root')

#T# save the plot with print()
print("S2_01_Aux01.svg")

#T# set axis limits with axis([xmin,xmax,ymin,ymax])
plot(x,y2,'--y'),axis([-1 10 -5 8])
print("S2_01_Aux01.svg")

#T# put several plots together with subplot()
subplot(1,2,1),plot(x,y1)
subplot(1,2,2),plot(x,y2)
print("S2_01_Aux01.svg")

#T# create a new figure with figure
figure

#T# create a bar chart with bar()
bar(x,y2)
print("S2_01_Aux01.svg")

#T# use meshgrid() to easily create a two variables function
[x1,y1] = meshgrid([0 1 2 3],[0 1 2 3]);
g = x1 + y1;

#T# create a contour graphic with contour()
[Cont1,fig1] = contour(x1,y1,g); axis equal;

#T# set a figure's parameters with set()
set(fig1,'ShowText','on');
print("S2_01_Aux01.svg")

#T# create a surface plot with surf(), or a mesh with mesh()
surf(x1,y1,g)
print("S2_01_Aux01.svg")
mesh(x1,y1,g)
print("S2_01_Aux01.svg")