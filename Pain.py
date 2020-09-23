creds = {'name1': 'psw1', 'name2': 'psw2'}
def auth_require(func):
    def wrapper_function(*args, **kwargs):
        name = input('Enter login: ')
        psw = input('Enter password: ')
        if name in creds and psw == creds[name]:
            print('True')
        else:
            print('Authentication required')
    return wrapper_function
@auth_require
def func(a, b):
    return a + b
func(1, 2)