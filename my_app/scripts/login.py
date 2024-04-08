import flet as ft


def main(page: ft.Page):

    # Set window properties
    page.title = 'Login'
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.LIGHT_BLUE_500,
    )
    page.bgcolor = ft.colors.LIGHT_BLUE_200  # Set the background color of the page 
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.update()

    # Create a container
    container = ft.Container(
        ft.Column(   # Create a column
            [ft.Container(
                ft.Text(
                    'Iniciar sesion',
                    width=280,
                    size=24,
                    text_align='center',
                    weight='w600',
                    color=ft.colors.BLACK87
                ),
                padding=ft.padding.only(20,20),
            ),
            ft.Container(
                ft.TextField(
                    width=280,
                    height=40,
                    hint_text='Correo',
                    border='underline',
                    color=ft.colors.BLACK87,
                    prefix_icon=ft.icons.EMAIL
                ),
                padding=ft.padding.only(20,20),
            ),
            ft.Container(
                ft.TextField(
                    width=280,
                    height=40,
                    hint_text='Password',
                    border='underline',
                    color=ft.colors.BLACK87,
                    prefix_icon=ft.icons.PASSWORD,
                    password=True
                ),
                padding=ft.padding.only(20,20),
            ),
            ft.Container(
                ft.Checkbox(
                    label='Recordar contraseña',
                    check_color=ft.colors.LIGHT_BLUE_300,
                ), 
                theme=ft.Theme(color_scheme=ft.ColorScheme(
                    primary=ft.colors.BLACK87)),
            ),
            ft.Container(
                ft.ElevatedButton(
                    'Iniciar session',
                    width=280,
                    height=40,
                    color=ft.colors.LIGHT_BLUE_500,
                    on_click=lambda x: print('Iniciar session')
                ),
                padding=ft.padding.only(20,20),
            ),
            ft.Text(
                'o',
                width=320, 
                color=ft.colors.LIGHT_BLUE_500,
                size=14,
                text_align='center',
            ),
            ft.Text(
                'Iniciar sesion con',
                width=320, 
                color=ft.colors.LIGHT_BLUE_500,
                size=14,
                text_align='center',
            ),
            ft.Container(
                ft.Row(
                    [ft.IconButton(
                        ft.icons.EMAIL,
                        on_click=lambda x: print('Iniciar session con Google'),
                        icon_size=50,
                    ),
                    ft.IconButton(
                        ft.icons.FACEBOOK,
                        on_click=lambda x: print('Iniciar session con Facebook'),
                        icon_size=50,
                    ),
                ], alignment='center')
            )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        
        border_radius=20,
        width=320,
        height=page.height*0.85,
        bgcolor=ft.colors.LIGHT_BLUE_100,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.LIGHT_BLUE_300,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
    )
    
    page.add(container)


ft.app(main)