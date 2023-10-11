#Generator obrazków

def main():
    
    resolution = (1920, 1080)

    pixel = {
        "R": 138,
        "G": 0,
        "B": 255
    }
    
    pixel_array = list([pixel for _ in range(resolution[0])] for _ in range(resolution[1]))

    content = [
        "P3\n",
        "# Testowy plik \".PPM\".\n",
        "# Każda linijka jest zarezerwowana dla jednego piksela.\n",
        "{} {}\n".format(resolution[0], resolution[1]),
        "255\n"
    ]

    for row_of_pixels in pixel_array:
        for single_pixel in row_of_pixels:
                content.append("{} {} {}\n".format(single_pixel["R"], single_pixel["G"], single_pixel["B"]))

    with open("D:\\Programowanie\\Projekty\\Python\\Image generator\\data\\Image.ppm", "w+", encoding="utf-8") as image_file:
        for line in content:
            image_file.write(line)

if __name__ == "__main__":
    main()