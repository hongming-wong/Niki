from replit import db
for i in db.keys():
    print(i, db[i])
    del db[i]