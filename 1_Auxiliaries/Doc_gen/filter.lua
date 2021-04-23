function Inlines(inlines1)
    for it1 = #inlines1 - 1, 1, -1 do
        if (inlines1[it1].text == "\\" and inlines1[it1 + 1].tag == "LineBreak") then 		   
            inlines1[it1] = pandoc.LineBreak()
        end
    end
    return inlines1
end