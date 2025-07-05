def add(numbers):
    if numbers == "":
        return 0
    
    total_sum=0
    delimiter="," 
  
    if numbers.startswith("//"):
        Split =numbers.split("\n")   
        delimiter= Split[0][2:] 
        numbers=Split[1]
        
    num= numbers.split(delimiter)
    negative =[]
    
    for i in num:
        n= int(i)
        if n < 0 :
            negative.append(n)
        elif n>1000:
            continue
        total_sum+= n
    
    if negative:
        raise Exception(f"Negative numbers are not allowed: {', '.join(map(str, negative))}")
    
   
    return total_sum    
