#Generator obrazków

def main():
    
    resolution = (1920, 1080)

    pixel = {
        "R": 12,
        "G": 56,
        "B": 100
    }
    
    pixel_array = list([pixel for _ in range(resolution[0])] for _ in range(resolution[1]))

    print("P3")
    print("# Testowy plik \".PPM\".")
    print("# Każda linijka jest zarezerwowana dla jednego piksela.")
    print("{} {}".format(resolution[0], resolution[1]))
    print("255")
    for row_of_pixels in pixel_array:
        for single_pixel in row_of_pixels:
            print("{} {} {}".format(single_pixel["R"], single_pixel["G"], single_pixel["B"]))

if __name__ == "__main__":
    main()