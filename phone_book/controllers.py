from views import render_template

from models import User, Phone



def default_controller(data=None, cls=True):
    """Default controller"""
    render_template(context={}, template="default.jinja2", cls=cls)
    return (input(), None)


def exit_controller(data=None, cls=True):
    render_template(context={}, template="exit.jinja2", cls=cls)
    exit()


def all_users_controller(data=None, cls=True):
    users = User.all()
    render_template(context={'users':users}, template="all_users.jinja2", cls=cls)
    input("Продолжить?")
    return 'main', None # (next state, data)


def add_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    username = input()
    user = User.add(username)
    return 21, user # (next state, data)


def add_phone_controller(user, cls=True):
    render_template(context={}, template="add_phone.jinja2", cls=cls)
    phone_number = input()
    phone = Phone.add(phone_number, user)
    return 212, user # (next state, data)


def add_more_controller(user, cls=True):
    render_template(context={}, template="add_more.jinja2", cls=cls)
    answer = input()
    if answer == 'Y':
        return 21, user
    return 51, user # (next state, data)


def select_for_update_controller(data=None, cls=True):
    render_template(context={}, template="select_more.jinja2", cls=cls)
    user = input()
    return 31, user # (next state, data)


def select_user_controller(data=None, cls=True):
    render_template(context={}, template="select_more.jinja2", cls=cls)
    user = input()
    return 51, user # (next state, data)


def show_user_controller(user_name, cls=True):
    user = User.select(user_name)
    render_template(context={'user':user}, template="show_user.jinja2", cls=cls)
    input('Нажмите enter, чтобы продолжить')
    return 'main', None # (next state, data)


def update_user_controller(old_name, cls=True):
    render_template(context={}, template="update_user.jinja2", cls=cls)
    new_name = input()
    User.update(old_name, new_name)
    return 51, new_name # (next state, data)

def delete_user_controller(data=None, cls=True):
    render_template(context={}, template="delete_user.jinja2", cls=cls)
    user = input()
    User.delete(user)
    return 'main', None # (next state, data)

def get_controller(state):
    return controllers_dict.get(state, default_controller)


controllers_dict = { # use dict type instead of if else chain
    '0': exit_controller,
    '1': all_users_controller,
    '2': add_user_controller,
    '3': select_for_update_controller,
    '4': delete_user_controller,
    '5': select_user_controller,
    21: add_phone_controller, # user can't enter 21 of int type
    212: add_more_controller,
    31: update_user_controller,
    51: show_user_controller
}