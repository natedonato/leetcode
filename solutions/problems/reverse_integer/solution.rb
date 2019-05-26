# @param {Integer} x
# @return {Integer}
def reverse(x)
    y = x.to_s.reverse.to_i
    if y >= 2**31
        return 0
    end
    return -y if x < 0
    y
end