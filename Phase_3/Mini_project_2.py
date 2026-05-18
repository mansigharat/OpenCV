import cv2
import sys

def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return val
        except ValueError:
            print("Invalid input, enter a number")

def get_color():
    b = get_int("Enter Blue value (0-255): ", 0, 255)
    g = get_int("Enter Green value (0-255): ", 0, 255)
    r = get_int("Enter Red value (0-255): ", 0, 255)
    return (b, g, r) 

def get_thickness():
    return get_int("Enter thickness (-1 for filled): ", -1)

def show(img):
    cv2.imshow("Drawing", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_line(img):
    x1 = get_int("X1: ")
    y1 = get_int("Y1: ")
    x2 = get_int("X2: ")
    y2 = get_int("Y2: ")
    color = get_color()
    thickness = get_thickness()
    cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def draw_rectangle(img):
    x1 = get_int("X1: ")
    y1 = get_int("Y1: ")
    x2 = get_int("X2: ")
    y2 = get_int("Y2: ")
    color = get_color()
    thickness = get_thickness()
    cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

def draw_circle(img):
    cx = get_int("Center X: ")
    cy = get_int("Center Y: ")
    r = get_int("Radius: ", 1)
    color = get_color()
    thickness = get_thickness()
    cv2.circle(img, (cx, cy), r, color, thickness)

FONT_MAP = {
    "simplex": cv2.FONT_HERSHEY_SIMPLEX,
    "plain": cv2.FONT_HERSHEY_PLAIN,
    "duplex": cv2.FONT_HERSHEY_DUPLEX,
    "complex": cv2.FONT_HERSHEY_COMPLEX,
    "triplex": cv2.FONT_HERSHEY_TRIPLEX,
}

def add_text(img):
    text = input("Text to add: ")
    x = get_int("X position: ")
    y = get_int("Y position: ")

    print("Available fonts:", ", ".join(FONT_MAP.keys()))
    font_name = input("Font name: ").strip().lower()
    font = FONT_MAP.get(font_name, cv2.FONT_HERSHEY_SIMPLEX)
    if font_name not in FONT_MAP:
        print(f"Unknown font, using 'simplex'")

    try:
        size = float(input("Font size: "))
    except ValueError:
        print("Invalid size, using 1.0")
        size = 1.0

    color = get_color()
    thickness = get_thickness()
    cv2.putText(img, text, (x, y), font, size, color, thickness)

OPERATIONS = {
    1: ("Line", draw_line),
    2: ("Rectangle", draw_rectangle),
    3: ("Circle", draw_circle),
    4: ("Add Text", add_text),
}

def main():
    path = input("Image path: ").strip()
    img = cv2.imread(path)

    if img is None:
        print(f"Error: could not load image at '{path}'")
        sys.exit(1)

    while True:
        print("\nOperations:")
        for k, (name, _) in OPERATIONS.items():
            print(f"  {k}. {name}")
        print("  0. Done")

        choice = get_int("Choice: ", 0, len(OPERATIONS))
        if choice == 0:
            break

        _, fn = OPERATIONS[choice]
        fn(img)

    print("\n1. Show\n2. Save\n3. Both")
    out = get_int("Output: ", 1, 3)

    if out in (1, 3):
        show(img)
    if out in (2, 3):
        save_path = input("Save path: ").strip()
        if cv2.imwrite(save_path, img):
            print(f"Saved to {save_path}")
        else:
            print("Error: failed to save")

if __name__ == "__main__":
    main()