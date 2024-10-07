
import reflex as rx
import reflex_chakra as rc

from .states import MachinesState


def gen_machine_grid_cell(machine_id: str, 
                          row_start: int, row_end: str, 
                          col_start: int, col_end: str, 
                          css_classes: list[str]) -> rx.Component:
    return rc.grid_item(
        rx.text(f"機台：{MachinesState.machines_content[machine_id]['machine_id']}"),
        rx.text(f"件號：{MachinesState.machines_content[machine_id]['prod_op']}"),
        rx.text(f"數量：{MachinesState.machines_content[machine_id]['target_qty']}"),
        rx.text(f"操作者：{MachinesState.machines_content[machine_id]['engineer_name']}"),
        col_start=col_start,
        col_end=col_end,
        row_start=row_start,
        row_end=row_end,
        id="", 
        class_name=[*css_classes],
    )

def gen_area_1_block_cells() -> list[rx.Component]:
    return [ # 13
        gen_machine_grid_cell('VMC08024', 2, '3', 1, '2',   ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('VMC08026', 3, '4', 1, '2',   ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('VMC08018', 4, '5', 1, '2',   ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('VMC08029', 5, '6', 1, '2',   ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('VMC08031', 6, '7', 1, '2',   ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('VMC08014', 2, '3', 2, '3',   ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('VMC08015', 3, '4', 2, '3',   ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('VMC08030', 4, '5', 2, '3',   ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('MAM01022', 6, '7', 2, '3',   ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('VMC08028', 7, '8', 2, '3',   ['machine-border-class', 'kai-1-bgc-class']), #10
        gen_machine_grid_cell('VMC08027', 8, '9', 2, '3',   ['machine-border-class', 'kai-2-bgc-class']),
        gen_machine_grid_cell('VMC08020', 9, '10', 2, '3',  ['machine-border-class', 'kai-2-bgc-class']),
        gen_machine_grid_cell('VMC08021', 10, '11', 2, '3', ['machine-border-class', 'kai-3-bgc-class'])
    ]

def gen_area_2_block_cells() -> list[rx.Component]:
    return [ # 10
        gen_machine_grid_cell('VMC08013', 2, '3', 3, '4', ['machine-border-class', 'kai-3-bgc-class']),
        gen_machine_grid_cell('VMC08012', 3, '4', 3, '4', ['machine-border-class', 'kai-3-bgc-class']),
        gen_machine_grid_cell('VMC08019', 4, '5', 3, '4', ['machine-border-class', 'kai-3-bgc-class']),
        gen_machine_grid_cell('MAM01021', 6, '7', 3, '4', ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('MAM01010', 1, '2', 4, '5', ['machine-border-class', 'kai-2-bgc-class']),
        gen_machine_grid_cell('MAM01013', 2, '3', 4, '5', ['machine-border-class', 'kai-2-bgc-class']),
        gen_machine_grid_cell('MAM01014', 3, '4', 4, '5', ['machine-border-class', 'kai-2-bgc-class']),
        gen_machine_grid_cell('MAM01017', 4, '5', 4, '5', ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('MAM01019', 5, '6', 4, '5', ['machine-border-class', 'kai-1-bgc-class']),
        gen_machine_grid_cell('MAM01020', 6, '7', 4, '5', ['machine-border-class', 'kai-1-bgc-class'])
    ]