def add(numbers):
    if numbers == "":
        return 0
    
    num= numbers.split(",")
    total_sum=0
    for i in num:
        total_sum += int(i)
    return total_sum    
