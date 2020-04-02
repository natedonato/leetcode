def is_happy(n)
  seen = {n=> true}
  while n != 1
    n = iterate(n)
    if(seen[n] == true)
      return false
    end

    seen[n] = true
  end  
  
  return true  
end




def iterate(n)
    sum = 0
    
    n.digits.each do |digit|
        sum += digit * digit
    end
    
    return sum
end