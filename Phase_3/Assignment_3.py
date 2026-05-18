import cv2

path_image = input("Enter the File Location : ")
image = cv2.imread(path_image)

def show():
    cv2.imshow("Drawing" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if image is not None:
    choice = int(input("Enter you choice : \n1. Line \n2. Rectangle \n3. Circle \n4. Adding Text\n" ))
    if choice == 1:

        x_pt1 = int(input("Enter the coordinate of X Point 1 : "))
        y_pt1 = int(input("Enter the coordinate of Y Point 1 : "))
        x_pt2 = int(input("Enter the coordinate of X Point 2 : "))
        y_pt2 = int(input("Enter the coordinate of Y Point 2 : "))

        color_r = int(input("Enter the Red color value from 0 to 255 : "))
        color_g = int(input("Enter the Green color value from 0 to 255 : "))
        color_b = int(input("Enter the Blue color value from 0 to 255 : "))

        thickness = int(input("Enter the thickness of line : "))

        cv2.line(image,(x_pt1,y_pt1),(x_pt2,y_pt2),(color_r,color_g,color_b),thickness)
   

    elif choice == 2:

        x_pt1 = int(input("Enter the coordinate of X Point 1 : "))
        y_pt1 = int(input("Enter the coordinate of Y Point 1 : "))
        x_pt2 = int(input("Enter the coordinate of X Point 2 : "))
        y_pt2 = int(input("Enter the coordinate of Y Point 2 : "))

        color_r = int(input("Enter the Red color value from 0 to 255 : "))
        color_g = int(input("Enter the Green color value from 0 to 255 : "))
        color_b = int(input("Enter the Blue color value from 0 to 255 : "))

        thickness = int(input("Enter the thickness of line : "))

        cv2.rectangle(image,(x_pt1,y_pt1),(x_pt2,y_pt2),(color_r,color_g,color_b),thickness)
       
    elif choice == 3:

        center_x = int(input("Enter the coordinate of X center: "))
        center_y = int(input("Enter the coordinate of Y center : "))

        radius = int(input("Enter the Radius : "))

        color_r = int(input("Enter the Red color value from 0 to 255 : "))
        color_g = int(input("Enter the Green color value from 0 to 255 : "))
        color_b = int(input("Enter the Blue color value from 0 to 255 : "))

        thickness = int(input("Enter the thickness of line : "))

        cv2.circle(image,(center_x,center_y),radius,(color_r,color_g,color_b),thickness)
        
    
    elif choice == 4:

        text = input("Enter Text to overwrite on image : ")
        center_x = int(input("Enter the coordinate of X : "))
        center_y = int(input("Enter the coordinate of Y : "))
        font = input("Enter the Font name : ")
        fontSize = float(input("Enter font Size : "))

        color_r = int(input("Enter the Red color value from 0 to 255 : "))
        color_g = int(input("Enter the Green color value from 0 to 255 : "))
        color_b = int(input("Enter the Blue color value from 0 to 255 : "))
        thickness = int(input("Enter the thickness of line : "))

        cv2.putText(image,text, (center_x,center_y),cv2.FONT_HERSHEY_SIMPLEX, fontSize,(color_r,color_g,color_b),thickness)
        
    else:
        print("Invalid Choice, try again")

    Output_choice = int(input("Enter you choice \n1. Show \n2. Save\n"))

    if Output_choice == 1:
        show()
    elif Output_choice == 2:
        pathSave = input("Enter the path location to save : ")
        cv2.imwrite(pathSave ,image)
        print("File Save Successfully at location ",pathSave)
    else:
         print("Invalid Choice, try again")
else:
    print("Error : Could not load image")