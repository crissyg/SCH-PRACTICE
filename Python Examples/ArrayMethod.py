def biggestValue(values):
    biggest = values[0]
    for num in values:
        if (num > biggest):
            biggest = num
    return biggest

