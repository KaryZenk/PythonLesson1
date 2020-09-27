def my_range(start, stop):
    i = start
    while i < stop:
        if i % 3 == 0:
            yield "Vasilyi"
        else:
            yield i
        i += 1
results = list(my_range(1, 7))
print(f'{results}')