# encoding:UTF-8
# 九九乘法表

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={} '.format(i, j, i*j), end='')
    print('')
