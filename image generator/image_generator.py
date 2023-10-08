#Generator obrazków

def main():
    
    resolution = (1920, 1080)

    pixel = {
        "R": 128,
        "G": 0,
        "B": 255
    }
    
    pixel_array = list([pixel for _ in range(resolution[0])] for _ in range(resolution[1]))

    with open("D:/Programowanie/Projekty/Python/Image generator/data/Image.ppm", "w+", encoding="utf-8") as image_file:
        image_file.write("P3\n")
        image_file.write("# Testowy plik \".PPM\".\n")
        image_file.write("# Każda linijka jest zarezerwowana dla jednego piksela.\n")
        image_file.write("{} {}\n".format(resolution[0], resolution[1]))
        image_file.write("255\n")
        for row_of_pixels in pixel_array:
            for single_pixel in row_of_pixels:
                image_file.write("{} {} {}\n".format(single_pixel["R"], single_pixel["G"], single_pixel["B"]))

if __name__ == "__main__":
    main()