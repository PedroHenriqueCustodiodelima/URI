n = int(input())
cameras = []
for i in range(n+1):
    row = list(map(int, input().split()))
    cameras.append(row)

for k in range(n):
    for l in range(n):
        totalCameras = 0
        if cameras[k][l] == 1:
            totalCameras += 1
        if cameras[k+1][l] == 1:
            totalCameras += 1
        if cameras[k][l+1] == 1:
            totalCameras += 1
        if cameras[k+1][l+1] == 1:
            totalCameras += 1
        if totalCameras >= 2:
            print("S", end="")
        else:
            print("U", end="")
    print()
