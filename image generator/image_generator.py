#Generator obrazków

def main():
    
    resolution = 600, 600
    
    red = []
    green = []
    blue = []

    for i in range(resolution[0]):
        red.append([])
        green.append([])
        blue.append([])
        for j in range(resolution[1]):
            red[i].append(255)
            green[i].append(100)
            blue[i].append(50)

    print("P3")
    print("# Testowy plik \".PPM\"")
    print("{} {}".format(resolution[0], resolution[1]))
    print("255")
    for i in range(resolution[0]):
        for j in range(resolution[1]):
            if j < resolution[1] - 1:
                end_print = " "
            else:
                end_print = "\n"
            print("{} {} {}".format(red[i][j], green[i][j], blue[i][j]), end=end_print)

if __name__ == "__main__":
    main()