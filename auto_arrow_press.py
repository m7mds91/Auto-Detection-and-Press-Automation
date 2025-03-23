import cv2
import numpy as np
import mss
import pydirectinput
import time

def select_roi():
    with mss.mss() as sct:
        screenshot = np.array(sct.grab(sct.monitors[1]))
        img = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
        roi = cv2.selectROI("Select ROI and press ENTER", img, False)
        cv2.destroyAllWindows()
        return {'top': int(roi[1]), 'left': int(roi[0]), 'width': int(roi[2]), 'height': int(roi[3])}

def detect_highlight(img_segment, threshold=100):  # Adjust threshold after calibration
    gray = cv2.cvtColor(img_segment, cv2.COLOR_BGR2GRAY)
    mean_brightness = np.mean(gray)
    return mean_brightness > threshold

def press_key(key):
    pydirectinput.keyDown(key)
    time.sleep(0.51)  # Increased reliability for games
    pydirectinput.keyUp(key)
    print(f"Pressed: {key}")

def main():
    region = select_roi()
    print(f"Monitoring region: {region}")

    arrow_keys = ['up', 'down', 'left', 'right']

    with mss.mss() as sct:
        while True:
            screen = np.array(sct.grab(region))
            img = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)
            h, w, _ = img.shape

            segment_height = h // 4
            for i, key in enumerate(arrow_keys):
                segment = img[i*segment_height:(i+1)*segment_height, :]
                if detect_highlight(segment):
                    press_key(key)
                    time.sleep(0.2)  # Prevent repeated rapid presses

            cv2.imshow("Monitoring (press 'q' to quit)", img)
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
