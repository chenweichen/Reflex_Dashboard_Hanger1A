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


from typing import Callable

import reflex as rx
import reflex_chakra as rc
from reflex.components.datadisplay.dataeditor import DataEditorTheme

from rxconfig import config

from .components import gen_area_1_block_cells, gen_area_2_block_cells
from .states import MachinesState
from .styles import style

data_editor_theme_case = {
    "header_font_style": "bold 2.5vmin",
    "base_font_style": "2.5vmin", #20241024_01:1.3em, #20241025_01: test dvw, dvh or dvmin=min(dvh, dvw)
}

def data_edit_tab() -> rx.Component:
    return rx.box( # rx.container
        rx.heading(f'Data Edit Tab'),
        rx.text(f'{MachinesState.clicked_data}'),
        rx.text(f'{MachinesState.edited_data}'),
        rx.data_editor(
            columns=MachinesState.cols,
            data=MachinesState.machine_data, # @rx.var
            on_cell_clicked=MachinesState.click_cell,
            on_cell_edited=MachinesState.handle_cell_edit,
            theme=DataEditorTheme(**data_editor_theme_case),
            header_height=70,
            row_height=65,
            max_column_width=120,
            freeze_columns=1, # The number of columns which should remain in place when scrolling horizontally.
            smooth_scroll_x=True,
            smooth_scroll_y=True,
            column_select='multi',
            overscroll_y=2,
        ),
        width='43vw', #TODO - Does it fit into the big screen?
        height='55vh', #TODO - Does it fit into the big screen?
    )


def data_presentation_tab(block_cells_1: list,  
                          block_cells_2: list
                          ) -> rx.Component:
    return rx.box(
        rc.grid(
            *block_cells_1,
            *block_cells_2,
            template_rows='repeat(10, 1fr)',
            template_columns='repeat(4, 1fr)',
            height='100%',
            width='100%',
            gap=2,
        ), # rc.grid
        height='100vh', # height for rx.box 
    ) # rx.box

def index() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Data edit tab", value="tab1"),
            rx.tabs.trigger("第 1 班", value="tab2"),  #NOTE - 1st period
            rx.tabs.trigger("第 2 班", value="tab3"),  #NOTE - 2nd period
            rx.tabs.trigger("第 3 班", value="tab4"),  #NOTE - 3rd period
            rx.tabs.trigger("第 4 班", value="tab5"),  #NOTE - 4th period
        ), # rx.tabs.list
        rx.tabs.content(
            data_edit_tab(),
            value="tab1",
        ),
        rx.tabs.content( #TODO - 1st period               
            data_presentation_tab(gen_area_1_block_cells('period_1'), gen_area_2_block_cells('period_1')),
            value="tab2",
        ),
        rx.tabs.content( #TODO - 2nd period
            data_presentation_tab(gen_area_1_block_cells('period_2'), gen_area_2_block_cells('period_2')),
            value="tab3",
        ),
        rx.tabs.content( #TODO - 3rd period
            data_presentation_tab(gen_area_1_block_cells('period_3'), gen_area_2_block_cells('period_3')),
            value="tab4",
        ),
        rx.tabs.content( #TODO - 4th period
            data_presentation_tab(gen_area_1_block_cells('period_4'), gen_area_2_block_cells('period_4')),
            value="tab5",
        ),
        defalut_value="tab1",
        orientation="horizontal"
    ) # rx.tab.root

app = rx.App(style=style)
app.add_page(index)