
#T# user defined function

function [retVal1_1 retVal1_2 retVal1_3] = S1_10_Aux01(arg1,arg2,arg3)
% help string for the function in this file
% create a function with the syntax shown

#T# use a global variable in a function with the global keyword
    global gVar1;
    
    retVal1_1 = 2 * arg1;

#T# call private function
    retVal1_2 = S1_10_Aux01(arg2);

#T# call subfunction
    retVal1_3 = subFun1(arg3);

    if (gVar1 == 12)
        retVal1_1 = 3;
        retVal1_2 = 2;
        retVal1_3 = 1;
    end

end

#T# create subfunctions in a function's file
function retValX = subFun1(a1)
    retValX = a1 * 5;
end