def fizzbuzz():
    for i in range (1,100):
        if i % 3 == 0 or i % 5 == 0:
            line = ""
            if i % 3 == 0:
                line = "Fizz"
            if i % 5 == 0:
                line += "Buzz"
            print line
        else:
            print i

print fizzbuzz()
