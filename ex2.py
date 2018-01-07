#!/bin/python
user = {'admin': False, 'active': False, 'name': 'somesh' }
if user["admin"]:
        print("ADMIN %s" % user["name"])
else:
        print("%s is not ADMIN" % user["name"])

if user["admin"] and user["active"]:
        print("ADMIN and active %s" % user["name"])
else:
        print("%s is either not admin or active" % user["name"])
if not user["admin"] and not user["active"]:
        print("%s is neither not admin nor active" % user["name"])
