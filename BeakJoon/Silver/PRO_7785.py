import sys
n = int(sys.stdin.readline())
company = set()
for _ in range(n):
    member,log = map(str,sys.stdin.readline().split())
    if log=='enter':
        company.add(member)
    else:
        if member in company: company.remove(member)
        else: continue
company = sorted(list(company),reverse=True)
for mem in company:
    print(mem)
