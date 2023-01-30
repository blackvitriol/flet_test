import flet as ft


def main(page: ft.Page):
    page.title = "A7 Flet Sample App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_username = ft.TextField(label="Please enter your name")

    def get_username():
        if page.client_storage.contains_key("user_name"):
            return page.client_storage.get("user_name")
        else:
            return "Unknown User"

    def save_name(e):
        open_dlg(e)
        page.client_storage.set("user_name", txt_username.value)

    txt_number = ft.TextField(
        value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 2)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    c = ft.Container(
        width=150,
        height=150,
        bgcolor="blue",
        border_radius=10,
        animate_opacity=300,
    )

    def animate_opacity(e):
        c.opacity = 0 if c.opacity == 1 else 1
        c.update()

    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)

    dlg = ft.AlertDialog(
        title=ft.Text("You name has been saved !"), on_dismiss=lambda e: print("Dialog dismissed!"))

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        ft.Text(value="Hello, {}! Welcome to the app.".format(
            get_username()), color="white"),
        txt_username,
        ft.Row(
            [
                ft.ElevatedButton("Save", on_click=save_name),
                ft.ElevatedButton("Continue", on_click=animate_opacity),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        c,
        ft.Divider(),
        ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                        txt_number,
                        ft.IconButton(ft.icons.ADD, on_click=plus_click),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.ElevatedButton("Choose files...",
                                  on_click=lambda _: file_picker.pick_files(allow_multiple=True))
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )


ft.app(target=main)
# Run as web app
# ft.app(target=main, view=ft.WEB_BROWSER)
