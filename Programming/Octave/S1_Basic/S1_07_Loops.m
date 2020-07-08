#!/usr/local/bin/octave
%{
    Loops
%}

#T# A1(2,2) = 0
A1 = [3 4 1;9 0 2];
#T# while block
while(A1)
    disp("Unreacheable code");
end

#T# for block
for i = A1
    disp(i);
end

i = 0;
#T# loop nesting
while (i < 12)
    for i = 1:2:11
        if (i == 3)

#T# continue statement
            continue;
        end
        disp(i);
    end
    if(i == 11)

#T# break statement
        break;
    end
end