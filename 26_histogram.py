def histogram(items):
    for n in items:
        output = ''
        times = n
        while(times > 0):
            output += '*'
            times = times - 1
        print(output)
histogram([1,2,3,4,5,6,7, 6, 5, 4, 3, 2, 1])