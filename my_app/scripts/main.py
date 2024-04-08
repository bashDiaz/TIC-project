import flet as ft
import Generate_cards as gc
import upper_menu as um
import os 

def card_rows(page, dir, data_path):
    # Create a list of cards
    cards = [os.path.splitext(element)[0] for element in dir]
    imgs = [element for element in dir]
    
    # Create a list of Card objects
    card_objects = [gc.Card(card, img, data_path, page) for card, img in zip(cards, imgs)]
    
    # Create a list of card containers
    card_containers = [card.create_card() for card in card_objects]

    card_rows = ft.Column(
        controls = [ft.ResponsiveRow(card_containers)],
        scroll=True
    )
    return card_rows


def main(page: ft.Page):
    # Set window properties
    page.bgcolor = '#EFEBE8'
    page.scroll = True

   # Ruta del directorio actual
    current_path = os.getcwd()
    # Ruta de la carpeta "assets" fuera del directorio actual
    data_path = os.path.join(current_path, 'my_app\\assets\\pictogramas')
    dir = os.listdir(data_path)


    #Create headder, upper menu
    upper_menu = um.UpperMenu(page, data_path)
    page.appbar = upper_menu.create_menu()


    #Create a categorry container
    main_column = ft.Column( 
        controls=[],                    
        scroll=True,
        spacing=0,
        expand=True)

    for foler in dir:
        main_column.controls.append(ft.Text(foler, size=20, weight='bold', color='black'))
        data_path_col = os.path.join(current_path, 'my_app\\assets\\pictogramas\\'+foler)
        dir = os.listdir(data_path_col)
        main_column.controls.append(card_rows(page, dir, data_path_col))
        main_column.controls.append(ft.Divider(thickness=3))

        

    page.add(main_column)

ft.app(main)
