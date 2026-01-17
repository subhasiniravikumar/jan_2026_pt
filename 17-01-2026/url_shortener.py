import string

db = {}
base = string.ascii_letters + string.digits

def encode(url):
    key = str(len(db) + 1)
    db[key] = url
    return "short.ly/" + key

def decode(short_url):
    key = short_url.split("/")[-1]
    return db.get(key, "URL not found")

u = input("Enter URL: ")
short = encode(u)
print("Short URL:", short)
print("Original URL:", decode(short))
