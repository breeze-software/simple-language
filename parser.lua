local lpeg = require("lpeg")
local white = lpeg.S(" \t\r\n") ^ 0

local integer = white * lpeg.R("09") ^ 1 / tonumber
local muldiv = white * lpeg.C(lpeg.S("/*"))
local addsub = white * lpeg.C(lpeg.S("+-"))

local function node(p)
  return p / function(left, op, right)
    return { op, left, right }
  end
end

local calculator = lpeg.P({
  "input",
  input = lpeg.V("exp") * -1,
  exp = lpeg.V("term") + lpeg.V("factor") + integer,
  term = node((lpeg.V("factor") + integer) * addsub * lpeg.V("exp")),
  factor = node(integer * muldiv * (lpeg.V("factor") + integer))
})
