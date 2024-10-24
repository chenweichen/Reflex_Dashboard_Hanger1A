"""Welcome to Reflex! This file outlines the steps to create a basic app."""

# Environment: Reflex0_6_py3_12_5
# Python version: 3.12.5
# Reflex version: 0.6.1


#import reflex as rx
#from rxconfig import config
#class State(rx.State):
#    """The app state."""
#
#    ...
#def index() -> rx.Component:
#    # Welcome Page (Index)
#    return rx.container(
#        rx.color_mode.button(position="top-right"),
#        rx.vstack(
#            rx.heading("Welcome to Reflex!", size="9"),
#            rx.text(
#                "Get started by editing ",
#                rx.code(f"{config.app_name}/{config.app_name}.py"),
#                size="5",
#            ),
#            rx.link(
#                rx.button("Check out our docs!"),
#                href="https://reflex.dev/docs/getting-started/introduction/",
#                is_external=True,
#            ),
#            spacing="5",
#            justify="center",
#            min_height="85vh",
#        ),
#        rx.logo(),
#    )
#app = rx.App()
#app.add_page(index)


import reflex as rx
import reflex_chakra as rc
from reflex.components.datadisplay.dataeditor import DataEditorTheme

from rxconfig import config

from .components import gen_area_1_block_cells, gen_area_2_block_cells
from .states import MachinesState
from .styles import style

data_editor_theme_case = {
    "header_font_style": "bold 2.5vmin",
    "base_font_style": "2.5vmin", #20241024_01:1.3em, 
}



def data_edit_tab() -> rx.Component:
    return rx.container(
        rx.heading(f'Data Edit Tab'),
        rx.text(f'{MachinesState.clicked_data}'),
        rx.text(f'{MachinesState.edited_data}'),
        rx.data_editor(
            columns=MachinesState.cols,
            data=MachinesState.machine_data,
            on_cell_clicked=MachinesState.click_cell,
            on_cell_edited=MachinesState.handle_cell_edit,
            theme=DataEditorTheme(**data_editor_theme_case),
            header_height=70,
            row_height=65,
            max_column_width=120,
        )
    )

def data_presentation_tab() -> rx.Component:
    return rx.box(
        rc.grid(
            *gen_area_1_block_cells(),
            *gen_area_2_block_cells(),
            template_rows='repeat(10, 1fr)',
            template_columns='repeat(4, 1fr)',
            height='100%',
            width='100%',
            gap=2,
        ), # rc.grid
        height='100vh', # height for rx.box
        width='100vw', # width for rx.box
    ) # rx.box

def index() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Data edit tab", value="tab1"),
            rx.tabs.trigger("Presentation tab", value="tab2"),
        ), # rx.tabs.list
        rx.tabs.content(
            data_edit_tab(),
            value="tab1",
        ),
        rx.tabs.content(
            data_presentation_tab(),
            value="tab2",
        ),
        defalut_value="tab1",
        orientation="horizontal"
    ) # rx.tab.root

app = rx.App(style=style)
app.add_page(index)