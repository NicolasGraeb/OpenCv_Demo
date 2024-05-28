import flet as ft
import base64
import numpy as np
from kamera import Kamera, Kamera1

class CAM_FLET(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.current_camera = None
        #self.img = None

        self.red_lower1 = np.array([0, 100, 100])
        self.red_upper1 = np.array([10, 255, 255])
        self.red_lower2 = np.array([160, 100, 100])
        self.red_upper2 = np.array([179, 255, 255])
        self.blue_lower = np.array([20, 100, 100])
        self.blue_upper = np.array([40, 255, 255])
        self.yellow_lower = np.array([90, 100, 100])
        self.yellow_upper = np.array([130, 255, 255])



        #self.update_frame()
    def update_frame(self):
        camera = Kamera1(
            np.array([0, 100, 100]), np.array([10, 255, 255]),  # Red
            np.array([160, 100, 100]), np.array([179, 255, 255]),  # Red2
            np.array([20, 100, 100]), np.array([40, 255, 255]),  # Blue
            np.array([90, 100, 100]), np.array([130, 255, 255])  # Yellow
        )
        while True:
            im_arr = camera.detect_obj()
            im_b64 = base64.b64encode(im_arr)
            self.img.src_base64 = im_b64.decode("utf-8")
            self.update()

    def build(self):
        self.img = ft.Image(
            border_radius=ft.border_radius.all(20)
        )
        return self.img
def main(page: ft.Page):
    camera = CAM_FLET()

    def start_cam(e):
        camera.update_frame()

    appbar = ft.AppBar(
        leading_width=50,
        title=ft.Text("Aplikacja Testowa"),
        center_title=True,
        bgcolor=ft.colors.GREY_800,
        actions=[
            ft.IconButton(ft.icons.CAMERA, on_click=start_cam)
        ]
    )

    section = ft.Container(
        bgcolor=ft.colors.WHITE24,
        padding=15,
        content=ft.Column([
            camera,
            ft.Text("your cam",
                    size=15, weight="bold",
                    color=ft.colors.WHITE),
        ]),
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50
    page.add(
        section,
        appbar
    )
    page.bgcolor = "#2E2E2E"

if __name__ == "__main__":
    ft.app(target=main)
