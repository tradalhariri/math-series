def fibonacci(n):
    """
    This function computes the nth value in fibonacci series
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    This function computes the nth value in lucas series
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    a = 2
    b = 1
    nth = 0
    for i in range(2,n+1):
        nth = a+b
        a=b
        b=nth
    return nth


    # lucasSeries = [2,1]
    # for i in range(2,n+1):
    #     lucasSeries.append(lucasSeries[i-1]+lucasSeries[i-2])
    # return lucasSeries[-1]


def sumSeries(n,first=0,second=1):
    """
    This function computes the nth value in any series if you provide it with a and b values,
     else it will compute the nth value in fibonacci series.
    """
    if n == 0:
        return first
    if n == 1:
        return second
    return sumSeries(n - 1,first,second) + sumSeries(n - 2,first,second)

    