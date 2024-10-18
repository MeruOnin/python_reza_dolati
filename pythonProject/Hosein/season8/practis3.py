from data_analysis import statistics
Input = input("Enter your list numbers (pls split with -,-): ")

numbers = Input.split(',')

lis = [int(i) for i in numbers]

print(statistics.avg(lis))
