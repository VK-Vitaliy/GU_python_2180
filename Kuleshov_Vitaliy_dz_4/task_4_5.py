import task_4_3 as utils

if __name__ == '__main__':
    import sys

    try:
        argv = sys.argv[1]
        exit(utils.currency_rates(argv))
    except IndexError:
        print(utils.currency_rates('USD'))
        print(utils.currency_rates('EUR'))
        print(utils.currency_rates('CNY'))
