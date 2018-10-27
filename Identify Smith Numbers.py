
def is_prime(n):

    is_it = True

    for x in range(2, int(n)):
        if n % x == 0:
            is_it = False
            break

    return is_it


t = int(input())
t2 = t
x = 0
gcdS = ""

if is_prime(t2) is True:
    print(0)

else:

    while is_prime(t) is False:

        for x in range(2, int(t)):

            if is_prime(x) is True and t % x == 0:
                t /= x
                gcdS += str(int(x))
                break

    gcdS += str(int(t))

    sum1 = 0
    sum2 = 0

    for nums in str(t2):
        sum1 += int(nums)

    for nums in gcdS:
        sum2 += int(nums)

    if sum1 == sum2:
        print(1)
    else:
        print(0)
