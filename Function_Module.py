import time
import random
class computator:
    def __init__(self):
        print("Computator Class Created Correct")
    def modulework(count_of_numbers):
        start_time = time.time()
        sumfile = open('sumfile1.txt', 'w')
        for x in range(count_of_numbers):
            sumfile.write(str(random.randrange(1, 101, 1)) + "\n")
        sumfile.close()
        sumr = 0.0
        averr = 1.0
        i: int = 0
        sf = open('sumfile1.txt', 'r+')
        numbers_set = []
        for x in sf.readlines():
            numbers_set.append(x)
            float(numbers_set[i])
            sumr = sumr + float(numbers_set[i])
            averr = sumr / (i + 1)
            i = i + 1
        print("sum is ", sumr, " and average is ", averr)
        print('End time: ', time.time() - start_time)
    def tester():
        if __name__ == '__main__':
            print('Programm working in module')
        else:
            print('Programm import')
    tester()
