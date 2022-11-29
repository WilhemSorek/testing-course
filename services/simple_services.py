def say_hello(name):
    hello = "hello %s !" % name

    return hello

def are_you_sure(yesOrNot):
    if yesOrNot:
        return "I'm sure!"
    else:
        return "Not sure!"

def has_permissions(user_permissions, asked_permission):
    return asked_permission in user_permissions    

def add_permission(user_permissions, asked_permission):
    if has_permissions(user_permissions, asked_permission):
        return user_permissions

    return has_permissions.append(asked_permission)
