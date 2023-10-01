import flet as ft
import qrcode
import os

temporal_text = ""
name_image = ""


def main(page: ft.Page):

    # Funciones
    def activateButton():
        if temporal_text != "" and name_image != "":
            button.disabled = False
            page.update()

        else:
            button.disabled = True
            page.update()

    # Funciones para guardar textos entrados
    def textbox_qr(e):
        global temporal_text
        temporal_text = e.control.value
        activateButton()

    def name_imageFun(e):
        global name_image
        name_image = e.control.value
        activateButton()

    # Funcion para generar codigoQR e imagen
    def qrgenerate(self):
        img = qrcode.make(temporal_text)
        type(img)  # qrcode.image.pil.PilImage

        try:
            # Guardar imagen
            img.save(os.environ['USERPROFILE'] +
                     "/Downloads/" + name_image + ".png")

            # Elementos de Pagina

            container1 = ft.Container(
                content=ft.Text(
                    "Escanee o Busque su archivo imagen en la carpeta Descargas de su PC",  size=20, text_align=ft.TextAlign.CENTER, color="blue")

            )
            container1.alignment = ft.alignment.center

            container2 = ft.Container(
                content=ft.Card(ft.Image(
                    src=os.environ['USERPROFILE'] +
                    "/Downloads/" + name_image + ".png",
                    width=300,
                    height=300,
                    fit=ft.ImageFit.CONTAIN,
                ))

            )
            container2.alignment = ft.alignment.center

            page.add(container1,  container2)

            page.update()
        except:

            error_text = ft.Text(
                "Error al guardar imagen, cierre y abra la aplicación nuevamente e intente de nuevo... O puede que el directorio Descargas o Downloads que crea Windows para el usuario no exista en su equipo para guardar la imagen",  size=20, text_align=ft.TextAlign.CENTER, color="red")
            page.add(error_text)

            page.update()

    # Propiedades de Pagina o Ventana
    page.padding = 20
    page.window_width = 900
    page.window_height = 600
    # page.window_resizable = False
    page.scroll = 'auto'

    page.title = "Genera tu QR"

    # Elementos
    button = ft.OutlinedButton(
        text="Generar QR", on_click=qrgenerate, disabled=True)

    responsive = ft.ResponsiveRow([
        ft.TextField(label="Entre el texto", width=300,
                     multiline=True, on_change=textbox_qr),
        ft.TextField(
            label="Entre el nombre del archivo imagen", width=300, on_change=name_imageFun),
        button

    ])

    page.add(
        responsive
    )

    firma = ft.Text(
        "Desarrollado por: Jore Ernesto Duvalón Hernández")
    page.add(ft.Divider(
        height=5, color="white"), firma, ft.Divider(
        height=5, color="white"))

    # Actualizar Pagina
    page.update()


ft.app(target=main)
