try:
    print(2/'0')
except ZeroDivisionError:
    print('ZeroDivisionError')
except Exception:
    print('Exception')
