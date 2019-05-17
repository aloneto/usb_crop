
import cv2


upper_left = (50, 50)
bottom_right = (300, 300)



def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()

        # Select ROI
        #r = cv2.selectROI(img)

        # Crop image
        #imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

        #Display cropped image
        #cv2.imshow("Image", imCrop)

        r = cv2.rectangle(img, upper_left, bottom_right, (100, 50, 200), 5)
        rect_img = img[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]]

        cv2.imshow("Sketcher ROI", rect_img)

        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()