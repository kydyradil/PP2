def histogram(lst):
    for num in lst:
        print('*' * num)  


nums = list(map(int, input(" ").split()))


histogram(nums)