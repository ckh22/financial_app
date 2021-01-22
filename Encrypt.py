import bcrypt
import uuid
password = "wwaaxxdd55297"
bpassword = b"wwaaxxdd55297"
hashed = bcrypt.hashpw(bpassword, bcrypt.gensalt())
print(hashed)
print(password)
print(hashed.decode("utf-8"))
if bcrypt.checkpw(bpassword, hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")

id = uuid.uuid1()
print(id)