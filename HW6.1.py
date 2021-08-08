
with open("nginx_logs.txt", "r", encoding="utf-8") as logs:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in logs)
    for i in content:
        print(i)