import cv2

path = input("Give location of image to fetch : ")

image = cv2.imread(path)

if image is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

choice = int(input("Give choice \n1. Show Image \n2. Save Image\n"))

if choice == 1:

    cv2.imshow("Image Show", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == 2:

    path_image = input("Give path to save image : ")

    success = cv2.imwrite(path_image, gray)

    if success:
        print(f"Image saved successfully at {path_image}")

else:
    print("Invalid choice")