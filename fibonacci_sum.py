SEQUENCE_TERM = 50


def sum_fibonacci(n):
    """
    Takes n (term of sequence) and adds up the numbers of the
    fibonacci series up to term n
    """

    # fib series is the list for storing the terms of the fibonacci series
    # as they are calculated
    fib_series = []

    # n + 1 is used for the range so it includes the term n in calculating
    # the fibonacci series list
    for i in range(n + 1):
        if i == 0:
            fib_series.append(0)
        elif i == 1:
            fib_series.append(1)
        else:
            fib_series.append(fib_series[i-1] + fib_series[i-2])

    return sum(fib_series)


sum_result = sum_fibonacci(SEQUENCE_TERM)

print(f"Sum of first {
      SEQUENCE_TERM} terms of the fibonacci series: ", sum_result)
