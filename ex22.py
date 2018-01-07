#!/bin/python
user = {'admin': "rrue", 'active': False, 'name': 'somesh' }
if user["admin"] and user["active"]:
        print("ADMIN and active %s" % user["name"])
elif user["admin"]:
        print("only Admin")
elif user["active"]:
        print("only active")
else:
        print("nothing")

