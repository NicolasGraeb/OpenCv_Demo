import cv2
cap = cv2.VideoCapture(0)

class Kamera:
    def __init__(self, color_lower1, color_upper1, color_lower2=None, color_upper2=None):
        self.color_lower1 = color_lower1
        self.color_upper1 = color_upper1
        self.color_lower2 = color_lower2
        self.color_upper2 = color_upper2

        self.is_camera_running = False
    def detect_obj(self):

        _, frame = cap.read()  # odczytywanie klatki obrazu

        img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(img_hsv, self.color_lower1, self.color_upper1)
        if self.color_lower2 is not None and self.color_upper2 is not None:
            mask2 = cv2.inRange(img_hsv, self.color_lower2, self.color_upper2)
            mask = mask1 + mask2
        else:
            mask = mask1

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            center_x = x + w // 2
            center_y = y + h // 2

            cv2.circle(frame, (center_x, center_y), 5, (240, 100, 0), -1)
            x_pos = str(center_x)
            y_pos = str(center_y)
            x_pos_text = f"x: {x_pos}"
            y_pos_text = f"y: {y_pos}"
            cv2.putText(frame, x_pos_text,(550, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            cv2.putText(frame, y_pos_text, (550, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
        _, im_arr = cv2.imencode('.png', frame)

        return im_arr

    def stop_camera(self):
        self.is_camera_running = False
class Kamera1:
    def __init__(self, red_lower1, red_upper1, red_lower2, red_upper2,
                 yellow_lower, yellow_upper, blue_lower, blue_upper):
        self.red_lower1 = red_lower1
        self.red_upper1 = red_upper1
        self.red_lower2 = red_lower2
        self.red_upper2 = red_upper2
        self.yellow_lower = yellow_lower
        self.yellow_upper = yellow_upper
        self.blue_lower = blue_lower
        self.blue_upper = blue_upper

        self.is_camera_running = False

    def detect_obj(self):
        _, frame = cap.read()

        img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask_red1 = cv2.inRange(img_hsv, self.red_lower1, self.red_upper1)
        mask_red2 = cv2.inRange(img_hsv, self.red_lower2, self.red_upper2)
        mask_red = mask_red1 + mask_red2

        mask_blue = cv2.inRange(img_hsv, self.blue_lower, self.blue_upper)

        mask_yellow = cv2.inRange(img_hsv, self.yellow_lower, self.yellow_upper)

        contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        largest_contour_red = None
        largest_contour_blue = None
        largest_contour_yellow = None

        if contours_red:
            largest_contour_red = max(contours_red, key=cv2.contourArea)
            x_red, y_red, w_red, h_red = cv2.boundingRect(largest_contour_red)
            cv2.rectangle(frame, (x_red, y_red), (x_red + w_red, y_red + h_red), (0, 0, 255), 2)
            center_red = (x_red + w_red // 2, y_red + h_red // 2)
            cv2.circle(frame, center_red, 5, (0, 0, 255), -1)
            cv2.putText(frame, f"x: {center_red[0]}", (x_red + w_red + 10, y_red + h_red // 2), cv2.FONT_HERSHEY_PLAIN,
                        1, (0, 0, 255), 2)
            cv2.putText(frame, f"y: {center_red[1]}", (x_red + w_red + 10, y_red + h_red // 2 + 20),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

        if contours_blue:
            largest_contour_blue = max(contours_blue, key=cv2.contourArea)
            x_blue, y_blue, w_blue, h_blue = cv2.boundingRect(largest_contour_blue)
            cv2.rectangle(frame, (x_blue, y_blue), (x_blue + w_blue, y_blue + h_blue), (255, 0, 0), 2)
            center_blue = (x_blue + w_blue // 2, y_blue + h_blue // 2)
            cv2.circle(frame, center_blue, 5, (255, 0, 0), -1)
            cv2.putText(frame, f"x: {center_blue[0]}", (x_blue + w_blue + 10, y_blue + h_blue // 2),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            cv2.putText(frame, f"y: {center_blue[1]}", (x_blue + w_blue + 10, y_blue + h_blue // 2 + 20),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

        if contours_yellow:
            largest_contour_yellow = max(contours_yellow, key=cv2.contourArea)
            x_yellow, y_yellow, w_yellow, h_yellow = cv2.boundingRect(largest_contour_yellow)
            cv2.rectangle(frame, (x_yellow, y_yellow), (x_yellow + w_yellow, y_yellow + h_yellow), (0, 255, 255), 2)
            center_yellow = (x_yellow + w_yellow // 2, y_yellow + h_yellow // 2)
            cv2.circle(frame, center_yellow, 5, (0, 255, 255), -1)
            cv2.putText(frame, f"x: {center_yellow[0]}", (x_yellow + w_yellow + 10, y_yellow + h_yellow // 2),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
            cv2.putText(frame, f"y: {center_yellow[1]}", (x_yellow + w_yellow + 10, y_yellow + h_yellow // 2 + 20),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)

        _, im_arr = cv2.imencode('.png', frame)

        return im_arr

    def stop_camera(self):
        self.is_camera_running = False
