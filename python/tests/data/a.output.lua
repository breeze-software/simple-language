local aaa = require "aaa"
local bbb = require "bbb"
local ccc = require "ccc"


function something(a, b) do
    return 4
end


function something_else_2(a, b) do
    if aaa then
        local a = b
        return 7
    elseif 30 then
        return 2
    else
        local c = 40
        return 3
    end
    return 444
end
