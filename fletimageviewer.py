"""
This program will show an example on how to control containers using button.
The container part will change its attibute when user click the buttons on the bottom.
"""

import flet as ft

def main(page: ft.Page):

    # PAGE CONFIGURATIONS
    page.title = "Flet Container Test"    
    page.window_maximized = True
    page.window_maximizable = False    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # BASIC CONTAINER FUNCTIONS
    # ---- CONTENT CONTAINER
    def contents():
        """Basic content container"""
        content_container = ft.Container(
            ft.Column([
                ft.Text(
                    value = "CONTAINER TEST",
                    style = 'displayLarge',
                    weight = 'bold'                    
                )],
                spacing = 50,                
                alignment = 'spaceBetween' 
                ),
            width = 1200,
            height = 650,
            border_radius = 30, 
            margin = ft.margin.all(10),
            bgcolor ='#F4DBD8',        
            alignment = ft.alignment.center,
            animate = True,
            animate_offset = ft.animation.Animation(2000, curve = 'easeOutCirc')
        ) 
        return content_container   

    # ---- BUTTON CONTAINER
    def buttons(button_width, container_width, button_list = None):
        """Basic buttons container"""
        button_container = ft.Container(
            ft.Row(
                button_list, 
                width = container_width, 
                spacing = int((container_width - (button_width * len(button_list)))/(len(button_list) + 1)) if button_list else 300,  
                alignment = 'spaceEvenly'
                ),
            width = 1200,
            height = 100,
            border_radius = 20,
            alignment = ft.alignment.center,
            margin = ft.margin.all(10),
            bgcolor = "#F4DBD8"
        )
        return button_container
    
    # BASIC VARIABLES TO BE ADDED TO THE PAGE
    all_contents = contents()
    all_buttons = buttons(200, 1200, button_list = [])

    # EVENTS FUNCTIONS
    def showone(e): 
        """Events for button one"""                    
        all_contents.gradient = ft.LinearGradient(
                begin = ft.alignment.top_right,
                end = ft.alignment.bottom_left,
                colors = ['#F4DBD8', '#BEA8A7'],
              )        
        all_contents.content = ft.Column([
                ft.Text(
                    value = "THE FIRST PART",
                    style = 'displayLarge',
                    weight = 'w900',
                    color = '#2A0800'                 
                ),
                ft.Card(
                    ft.Image(
                    src = f'/chuttersnap-mBR7z0TLDH4-unsplash.jpg',                    
                    border_radius = ft.border_radius.all(10),
                    width = 500,
                    height = 500,
                    tooltip = "Image from unsplash.com",
                    fit = 'fill'
                    ),
                    elevation = 20,
                    margin = ft.margin.all(10)
                ),
                ],
                spacing = 50,
                alignment = 'center',
                animate_offset = ft.animation.Animation(2000, curve = 'easeOutCirc')
        )                
        page.update()

    def showtwo(e): 
        """Events for button two"""               
        all_contents.gradient = ft.LinearGradient(
                begin = ft.alignment.top_right,
                end = ft.alignment.bottom_left,
                colors = ['#F4DBD8', '#C09891'],
              )    
        all_contents.content = ft.Column([
                ft.Text(
                    value = "THE SECOND PART",
                    style = 'displayLarge',
                    weight = 'w900',
                    color = 'black'                                    
                ),
                ft.Card(
                    ft.Image(
                    src = f'/greg-becker-UXRceJ89NNw-unsplash.jpg',                    
                    border_radius = ft.border_radius.all(10), 
                    width = 500,
                    height = 500,
                    tooltip = "Image from unsplash.com",
                    fit = 'fill'
                    ),
                    elevation = 20,
                    margin = ft.margin.all(10)
                )
                ],
                spacing = 50,
                alignment = 'center', 
                animate_offset = ft.animation.Animation(2000, curve = 'easeOutCirc')
        )    
        page.update()
    
    def showthree(e):
        """Events for button three"""
        all_contents.gradient = ft.LinearGradient(
                begin = ft.alignment.top_right,
                end = ft.alignment.bottom_left,
                colors = ['#F4DBD8', '#775144'],
              ) 
        all_contents.content = ft.Column([
                ft.Text(
                    value = "THE THIRD PART",
                    style = 'displayLarge',
                    weight = 'w900',
                    color = 'black'                                        
                ),
                ft.Card(
                    ft.Image(                    
                    src = f'/jackson-case-hYEI0kTmbdU-unsplash.jpg',
                    border_radius = ft.border_radius.all(10),
                    width = 500,
                    height = 500,
                    tooltip = "Image from unsplash.com",
                    fit = 'fill'
                    ),
                    elevation = 20,
                    margin = ft.margin.all(10)
                )
                ],
                spacing = 50,
                alignment = 'center',
                animate_offset = ft.animation.Animation(2000, curve = 'easeOutCirc')
        )
        page.update()

    def showfour(e):    
        """Events for button four"""    
        all_contents.gradient = ft.LinearGradient(
                begin = ft.alignment.top_right,
                end = ft.alignment.bottom_left,
                colors = ['#F4DBD8', '#2A0800'],
              ) 
        all_contents.content = ft.Column([
                ft.Text(
                    value = "THE FOURTH PART",
                    style = 'displayLarge',
                    weight = 'w900',
                    color = 'black'
                ),
                ft.Card(
                    ft.Image(
                        src = f'/drew-gilliam-Hq_K7X2NkGE-unsplash.jpg',
                        border_radius = ft.border_radius.all(10),
                        width = 500,
                        height = 500,
                        tooltip = "Image from unsplash.com",
                        fit = 'fill'
                    ),                    
                    elevation = 20,
                    margin = ft.margin.all(10)
                ),
                ],
                spacing = 50,
                alignment = 'center',
                animate_offset = ft.animation.Animation(2000, curve = 'easeOutCirc')
        )
        page.update()

    # SPECIFY WIDGETS INSIDE BUTTON CONTAINER
    one = ft.ElevatedButton(
        text = 'ONE', 
        width = 200,                 
        style = ft.ButtonStyle(
            bgcolor = {
                ft.MaterialState.HOVERED: ft.colors.BLUE_GREY_600,
                ft.MaterialState.DEFAULT: ft.colors.BLUE_GREY_900                
            },
            color = {
                ft.MaterialState.DEFAULT: ft.colors.WHITE
            }
        ),
        on_click=showone
        )

    two = ft.ElevatedButton(
        text = 'TWO', 
        width = 200, 
        style = ft.ButtonStyle(
            bgcolor = {
                ft.MaterialState.HOVERED: ft.colors.BLUE_GREY_600,
                ft.MaterialState.DEFAULT: ft.colors.BLUE_GREY_900
            },
            color = {
                ft.MaterialState.DEFAULT: ft.colors.WHITE
            }
        ),
        on_click=showtwo)

    three = ft.ElevatedButton(
        text = 'THREE', 
        width = 200, 
        style = ft.ButtonStyle(
            bgcolor = {
                ft.MaterialState.HOVERED: ft.colors.BLUE_GREY_600,
                ft.MaterialState.DEFAULT: ft.colors.BLUE_GREY_900
            },
            color = {
                ft.MaterialState.DEFAULT: ft.colors.WHITE
            }
        ),
        on_click=showthree)

    four = ft.ElevatedButton(
        text = 'FOUR', 
        width = 200,                 
        style = ft.ButtonStyle(
            bgcolor = {
                ft.MaterialState.HOVERED: ft.colors.BLUE_GREY_600,
                ft.MaterialState.DEFAULT: ft.colors.BLUE_GREY_900
            },
            color = {
                ft.MaterialState.DEFAULT: ft.colors.WHITE
            }
        ),
        on_click=showfour)

    all_buttons = buttons(200, 1200, button_list = [one, two, three, four])
    
    # ADDING ALL CONTAINERS TO THE PAGE
    page.add(
        ft.Column(
            [
                all_contents,
                all_buttons
            ],            
            spacing = 50,
            alignment = 'spaceBetween'
        )
    )

    page.update()


if __name__ == '__main__':
    # EXECUTE THE APP
    ft.app(target = main, assets_dir = 'images')