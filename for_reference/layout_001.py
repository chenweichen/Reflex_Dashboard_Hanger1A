"""Welcome to Reflex! This file outlines the steps to create a basic app."""

# Environment: Reflex_0_5_5
# Python version: 3.11.9
# Reflex version: 0.5.5

import reflex as rx

from rxconfig import config

from .component_machines import (gen_h1_1_block_cells, gen_h1_2_block_cells,
                                 gen_h2_1_block_cells, gen_h2_2_block_cells,
                                 gen_kai_area1_block_cells, gen_kai_area2_block_cells)
from .states import MachineState

from .styles import style


def data_edit_tab() -> rx.Component:
    return rx.container(
        rx.heading(f'Data Edit Tab'),
        rx.text(f'{MachineState.clicked_data}'),
        rx.text(f'{MachineState.edited_data}'),
        rx.data_editor(
            columns=MachineState.cols,
            data=MachineState.machine_data,
            on_cell_clicked=MachineState.click_cell,
            on_cell_edited=MachineState.handle_cell_edit, 
            )
    )


def data_presentation_tab() -> rx.Component:
    return rx.chakra.grid(
        #*gen_h2_1_block_cells(),
        #*gen_h2_2_block_cells(),
        #*gen_h1_1_block_cells(),
        #*gen_h1_2_block_cells(),
        *gen_kai_area1_block_cells(),
        *gen_kai_area2_block_cells(),
        #template_rows="repeat(11, 1fr)",
        template_rows="repeat(10, 1fr)",
        #template_columns="repeat(9, 1fr)",
        template_columns="repeat(4, 1fr)",
        height="10em",
        width="100%",
        gap=2,
    )


def index() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Data edit tab", value="tab1"),
            rx.tabs.trigger("Presentation tab", value="tab2"),
        ), # rx.tabs.list
        rx.tabs.content(
            data_edit_tab(),
            value="tab1",
        ), #rx.tabs.content
        rx.tabs.content(
            data_presentation_tab(),
            value="tab2",
        ), #rx.tabs.content
        default_value="tab1",
        orientation="horizontal"
    ) # rx.tab.root


app = rx.App(style=style)
app.add_page(index)