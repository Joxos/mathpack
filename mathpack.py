def ceil(x):
    """
    返回 x 的上限，即大于或者等于 x 的最小整数。如果 x 不是一个浮点数，则委托 x.__ceil__(), 返回一个 Integral 类的值。
    """
    if type(x) == float:
        if int(x) == x:
            # to prevent things like 3.00->4
            return int(x)
        else:
            return int(x+1)
    else:
        return x.__ceil__()


def comb(n, k):
    """
    返回不重复且无顺序地从 n 项中选择 k 项的方式总数。
    当 k <= n 时取值为 n! / (k! * (n - k)!)；当 k > n 时取值为零。
    也称为二项式系数，因为它等价于表达式 (1 + x) ** n 的多项式展开中第 k 项的系数。
    如果任一参数不为整数则会引发 TypeError。 如果任一参数为负数则会引发 ValueError。
    """
    if type(n) != int or type(k) != int:
        raise TypeError
    elif n < 0 or k < 0:
        raise ValueError
    else:
        if k <= n:
            return factorial(n)/(factorial(k)*factorial(n-k))
        else:
            return 0


def fabs(x):
    """
    返回 x 的绝对值。
    仅支持 int 和 float 类型的运算。
    """
    if type(x) == int or type(x) == float:
        if x < 0:
            return -x
        else:
            return x
    else:
        raise TypeError


def factorial(x):
    """
    以一个整数返回 x 的阶乘。 如果 x 不是整数或为负数时则将引发 ValueError。
    """
    if type(x) != int or x < 0:
        raise ValueError
    else:
        bfn = 1
        counter = 1
        while x > counter:
            counter += 1
            bfn *= counter
        return bfn


def floor(x):
    """
    返回 x 的向下取整，小于或等于 x 的最大整数。如果 x 不是浮点数，则委托 x.__floor__() ，它应返回 Integral 值。
    """
    if type(x) == float:
        return int(x)
    else:
        return x.__floor__()


def fmod(x, y):
    if type(x) != float or type(y) != float:
        raise TypeError
    else:
        n = 0
        min = x-n*y
        while min >= fabs(y):
            n += 1
            min = x-n*y
        return min
