import cv2
import random


def get_lifetime_video():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) == ord('c'):
            cv2.imwrite(f'imgs/me{random.randint(0, 11111)}.jpg', frame)
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    get_lifetime_video()


if __name__ == '__main__':
    main()