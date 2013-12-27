def fib(n):
    print 'n = %s' % n
    if n > 1:
        return fib(n-1) * n
    else:
        print 'end of the line'
        return 1

if __name__ == "__main__":
    print fib(10)
