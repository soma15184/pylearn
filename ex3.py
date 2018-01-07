#!/bin/python
users = [{'admin': True, 'active': True, 'name': 'somesh'}, {'admin': True, 'active': False, 'name': 'lovelet'},{'admin':False,'active': False, 'name': 'bala'}]
for user in users:
    if user["admin"] and user["active"]:
            print("user is admin and active both %s" % user["name"])
    elif user["admin"]:
            print("user is admin %s" % user["name"])
    elif user["active"]:
            print("user is active %s" % user["name"])
    else:
            print("user is neither active not admin %s" % user["name"])

