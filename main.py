import flet as ft
import base64
import numpy as np
from kamera import Kamera

class CAM_FLET(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.current_camera = None
    def update_frame(self, lower_color1, upper_color1, lower_color2=None, upper_color2=None):
        if self.current_camera:
            self.current_camera.stop_camera()
        self.current_camera = Kamera(lower_color1, upper_color1, lower_color2, upper_color2)
        while True:
            im_arr = self.current_camera.detect_obj()
            im_b64 = base64.b64encode(im_arr)
            self.img.src_base64 = im_b64.decode("utf-8")
            self.update()
    def stop_camera(self):
        if self.current_camera:
            self.current_camera.stop_camera()
            self.current_camera = None
    def build(self):
        if not self.current_camera:
            self.img = ft.Image(
                border_radius=ft.border_radius.all(20)
            )
            return self.img
def main(page: ft.Page):
    camera = CAM_FLET()
    def clicked_red(e):
        camera.stop_camera()
        camera.update_frame(np.array([0, 100, 100]), np.array([10, 255, 255]), np.array([160, 100, 100]), np.array([179, 255, 255]))
    def clicked_yellow(e):
        camera.stop_camera()
        camera.update_frame(np.array([20, 100, 100]), np.array([40, 255, 255]))
    def clicked_blue(e):
        camera.stop_camera()
        camera.update_frame(np.array([90, 100, 100]), np.array([130, 255, 255]))
    def clicked_green(e):
        camera.stop_camera()
        camera.update_frame(np.array([40, 100, 100]), np.array([80, 255, 255]))

    appbar = ft.AppBar(
        leading_width=50,
        title=ft.Text("Aplikacja Testowa"),
        bgcolor=ft.colors.BLUE_300,
        actions=[
            ft.IconButton(ft.icons.CAMERA),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="RED", on_click=clicked_red),
                    ft.PopupMenuItem(text="YELLOW", on_click=clicked_yellow),
                    ft.PopupMenuItem(text="BLUE", on_click=clicked_blue),
                    ft.PopupMenuItem(text="GREEN", on_click=clicked_green),
                ]
            ),
        ],
    )

    section = ft.Container(
        border_radius=ft.border_radius.all(20),
        bgcolor=ft.colors.BLUE_300,
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
    #page.theme = ft.theme.Theme(color_scheme_seed="light")
    page.theme_mode = "light"
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
