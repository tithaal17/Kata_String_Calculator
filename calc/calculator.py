def add(numbers):
    if numbers == "":
        return 0
    
    delimiter="," 
  
    if numbers.startswith("//"):
        Split =numbers.split("\n")   
        delimiter= Split[0][2:] 
        numbers=Split[1]

    num= numbers.split(delimiter)
    total_sum=0
    for i in num:
        total_sum += int(i)
    return total_sum    
