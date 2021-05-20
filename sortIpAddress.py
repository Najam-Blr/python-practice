

if __name__ == '__main__':
    ipAddr = []
    with open("C:\\Users\\najam\\Desktop\\ipAddress.txt", "r", encoding="utf-8") as f:
        ipAddr = list(map(str, f.readline().split(",")))

    for i in range(len(ipAddr)-1):
        for j in range(i+1, len(ipAddr)):
            if ipAddr[i] > ipAddr[j]:
                temp = ipAddr[i]
                ipAddr[i] = ipAddr[j]
                ipAddr[j] = temp

    print("\n".join(ipAddr))
    f.close()
