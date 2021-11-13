from replit import db
for i in db.keys():
    print(i)
    print(db[i])
    del db[i]