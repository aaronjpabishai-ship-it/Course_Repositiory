#nested if statements

is_logged_in = True
is_admin = True


if is_logged_in:
    print("User is logged in")
    if is_admin:
        print("Show admin panel")
    else:
        print("Show Regular Dashboard")
else:
    print("Redirect to login page")