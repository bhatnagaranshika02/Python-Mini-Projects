from googlesearch import search
query = "anshika"
for i in search(query,tld = "co.in",num=10,stop=10,pause=2):
    print(i)
