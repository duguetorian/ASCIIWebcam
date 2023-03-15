import os
import sys
import cv2
import ascii_conversion

if __name__ == '__main__':

    if "--help" in sys.argv:
        print("Options:\n --color : the ascii caracters are in color\n --size <divide factor> : divide the size of the terminal by the factor entered")
        sys.exit()

    if "--size" in sys.argv:
        idx = sys.argv.index("--size")
        try:
            ds = float(sys.argv[idx+1])
        except ValueError:
            print("You must enter the division factor as a float after --size")
            sys.exit()
        except IndexError:
            print("You must enter the division factor after --size")
            sys.exit()
        if ds < 1:
            print("The size factor must be greater than 1")
            sys.exit()

    else:
        ds = 1


    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        dim = (int(os.get_terminal_size().columns//ds), int((os.get_terminal_size().lines - 1)//ds))
        print(dim)
        frame = cv2.resize(frame, dim)
        print(ascii_conversion.ascii_conversion(frame, "--color" in sys.argv))
