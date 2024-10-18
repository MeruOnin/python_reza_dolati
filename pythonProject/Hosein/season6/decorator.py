# تغییر رمز در یک دیکشنری
# from functools import wraps
password = {"hossein": "9120834", "anahita": '98327843', "darya": '21749', "amir ali": '21984', "hady": '89236159'}
black_list = {"darya", "amir ali", "hady"}
#
#
# def dec(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         if args[0] in black_list:
#             return "sorry can not change password!"
#         else:
#             return func(*args, **kwargs)
#     return inner
#
#
# def show_password(user_name):
#     return user_name+": "+password.get(user_name.lower())
#
#
# @dec
# def change_password(user_name, new_password):
#     """This function is change password"""
#     password[user_name.lower()] = new_password
#     return user_name+": "+password[user_name.lower()]
#
#
# print(change_password.__doc__)
# print(change_password("hady", "654"))

# محاسبه زمان اجرای یک تابع
from time import perf_counter
from functools import wraps


def dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        first_counter = perf_counter()
        show = func(*args, **kwargs)
        last_counter = perf_counter()
        run_time = last_counter-first_counter
        print(round(run_time, 2))
        return show
    return inner


@dec
def change_password(user_name, new_password):
    """This function is change password"""
    password[user_name.lower()] = new_password
    return user_name+": "+password[user_name.lower()]


print(change_password("hossein", "76"))
print(password)


