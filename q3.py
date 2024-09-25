

# if a day does not have income, it will be considered as None in the list


def min_value(daily_incomes):
    if len(daily_incomes) == 0:
        return None
    result = daily_incomes[0]
    for income in daily_incomes:
        if income is not None and (result is None or income < result):
            result = income
    return result

def max_value(daily_incomes):
    if len(daily_incomes) == 0:
        return None
    result = daily_incomes[0]
    for income in daily_incomes:
        if income is not None and (result is None or income > result):
            result = income
    return result


def _mean(daily_incomes):
    sum = 0
    num_of_items = 0
    for income in daily_incomes:
        if income is not None:
            sum += income
            num_of_items += 1
    if num_of_items == 0:
        return None
    return sum / num_of_items

def days_with_income_greater_than_mean(daily_incomes):
    yearly_mean = _mean(daily_incomes) 
    if yearly_mean is None:
        return 0 
    result = 0
    for income in daily_incomes:
        if income is not None and income > yearly_mean:
            result += 1
    return result

def program(daily_incomes):
    return min_value(daily_incomes), max_value(daily_incomes), days_with_income_greater_than_mean(daily_incomes)

def _test(v, expected):
    assert expected == program(v), f'T1 Failed for {v}'
    print('.', end='')

def main():
    # test cases
    _test([], (None, None, 0)) 
    _test([None], (None, None, 0))
    _test([10.90], (10.9, 10.9, 0))
    _test([None, None], (None, None, 0))
    _test([0, None], (0, 0, 0))
    _test([None, 0], (0, 0, 0))
    _test([-1, 0, 1, None, 1], (-1, 1, 2)) # mean = 0.25
    _test([1, 1, 1, 1, 1, 1, 1], (1, 1, 0)) 
    _test([1, 1.01, 1, 1, 1, 1, 1], (1, 1.01, 1)) 
    _test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (1, 10, 5)) 

    print('')
    print('Tests passed!')


if __name__=='__main__':
    main()

