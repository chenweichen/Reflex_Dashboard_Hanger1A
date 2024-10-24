
import reflex as rx
import reflex_chakra as rc

from .states import MachinesState


def gen_machine_grid_cell(machine_id: str, 
                          row_start: int, row_end: str, 
                          col_start: int, col_end: str, 
                          css_classes: list[str],
                          size_of_font: str) -> rx.Component:
    return rc.grid_item(
        rx.box(
            rx.flex(
                rx.text(f"機台：", weight='bold', font_size=size_of_font),
                rx.text(f"{MachinesState.machines_content[machine_id]['machine_id']}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                direction='row',
            ), # rx.flex
            rx.flex(
                rx.text(f"件號：", weight='bold', font_size=size_of_font),
                rx.text(f"{MachinesState.machines_content[machine_id]['prod_op']}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                rx.text(f" |=> ", white_space="pre", font_size=size_of_font),
                rx.text(f"數量：", weight='bold', font_size=size_of_font),
                rx.text(f"{MachinesState.machines_content[machine_id]['target_qty']}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                direction='row',
            ), # rx.flex
            rx.flex(
                rx.text(f"操作者：", weight='bold', font_size=size_of_font),
                rx.text(f"{MachinesState.machines_content[machine_id]['engineer_name']}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                direction='row',
            ), # rx.flex
        ), # rx.box
        col_start=col_start,
        col_end=col_end,
        row_start=row_start,
        row_end=row_end,
        id="", 
        class_name=[*css_classes],
    )

def gen_area_1_block_cells() -> list[rx.Component]:
    return [ # 13
        gen_machine_grid_cell('VMC08024', 2, '3', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08026', 3, '4', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08018', 4, '5', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08029', 5, '6', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08031', 6, '7', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08014', 2, '3', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08015', 3, '4', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08030', 4, '5', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('MAM01022', 6, '7', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08028', 7, '8', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"), #10
        gen_machine_grid_cell('VMC08027', 8, '9', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08020', 9, '10', 2, '3',  ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08021', 10, '11', 2, '3', ['cell-border', 'cell-bgc-1'], "1.85vmin")
    ]

def gen_area_2_block_cells() -> list[rx.Component]:
    return [ # 10
        gen_machine_grid_cell('VMC08013', 2, '3', 3, '4', ['cell-border', 'cell-bgc-3'], "1.85vmin"),
        gen_machine_grid_cell('VMC08012', 3, '4', 3, '4', ['cell-border', 'cell-bgc-3'], "1.85vmin"),
        gen_machine_grid_cell('VMC08019', 4, '5', 3, '4', ['cell-border', 'cell-bgc-3'], "1.85vmin"),
        gen_machine_grid_cell('MAM01021', 6, '7', 3, '4', ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('MAM01010', 1, '2', 4, '5', ['cell-border', 'cell-bgc-2'], "1.85vmin"),
        gen_machine_grid_cell('MAM01013', 2, '3', 4, '5', ['cell-border', 'cell-bgc-2'], "1.85vmin"),
        gen_machine_grid_cell('MAM01014', 3, '4', 4, '5', ['cell-border', 'cell-bgc-2'], "1.85vmin"),
        gen_machine_grid_cell('MAM01017', 4, '5', 4, '5', ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('MAM01019', 5, '6', 4, '5', ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('MAM01020', 6, '7', 4, '5', ['cell-border', 'cell-bgc-1'], "1.85vmin")
    ]