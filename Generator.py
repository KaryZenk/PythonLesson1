def my_range(start=1):
    while True:
        if start % 3 == 0:
            yield 'Vasilyi'
        else: 
            yield start
        start += 1
results = list(my_range(1, 7))
print(f'results={results}')
