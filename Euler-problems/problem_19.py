import sys


def fact(n):
    res = [None] * 500
    res[0] = 1
    res_size = 1
    x = 2
    while x <= n:
        res_size =multiply(x, res, res_size)
        x = x + 1
    print("Factorial of given number is")
    i = res_size - 1
    while i >= 0:
        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
        i = i - 1
    return res


def multiply(x, res, res_size):
    carry = 0  # Initialize carry

    # One by one multiply n with individual
    # digits of res[]
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10;  # Store last digit of
        # 'prod' in res[]
        # make sure floor division is used
        carry = prod // 10;  # Put rest in carry
        i = i + 1

    # Put carry in res and increase result size
    while (carry):
        res[res_size] = carry % 10
        # make sure floor division is used
        # to avoid floating value
        carry = carry // 10
        res_size = res_size + 1

    return res_size


re = fact(5)

print(re)

sum = 0
d = '93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000'
for i in d:
    sum += int(i)
print(sum)