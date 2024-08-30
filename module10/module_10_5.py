import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for i in file.read().split('\n'):
            all_data.append(i)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = time.time()
for file in filenames:
    read_info(file)
print('line_time', time.time() - start)
# line_time 5.648810386657715

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        start1 = time.time()
        pool.map(read_info, filenames)
    print('multi_time', time.time() - start1)
# multi_time 2.8619110584259033
