

import reflex as rx

from .states import AreaState, MachineState

# Left to Right

# Reference
# id and class name
# Components support many standard HTML properties as props. For example: the HTML id property is exposed directly as the prop id. The HTML className property is exposed as the prop class_name (note the Pythonic snake_casing!).
# https://reflex.dev/docs/components/props/#html-props
# 
# Component Styles
# In your style dictionary, you can also specify default styles for specific component types or arbitrary CSS classes and IDs.
# https://reflex.dev/docs/styling/overview/#component-styles


###############################################################################################
# Library/Chakra/Layout/Grid                                                                                           #
# https://reflex.dev/docs/library/chakra/layout/grid/                                                                                           #
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################
# Version: 20240806


def gen_machine_grid_cell(machine_id: str, row_start: int, row_end: str, col_start: int, col_end: str, css_classes: list[str]) -> rx.Component:
    return rx.chakra.grid_item(
        rx.text(f"機台：{MachineState.machine_contents[machine_id]['machine_id']}"),
        rx.text(f"件號：{MachineState.machine_contents[machine_id]['prod_op']}"),
        rx.text(f"數量：{MachineState.machine_contents[machine_id]['target_qty']}"),
        rx.text(f"操作者：{MachineState.machine_contents[machine_id]['engineer_name']}"),
        col_start=col_start,
        col_end=col_end,
        row_start=row_start,
        row_end=row_end,
        id="", 
        class_name=[*css_classes],
    )

def gen_area_grid_cell(area_id: str, row_start: int, row_end: str, col_start: int, col_end: str, css_classes: list[str]) -> rx.Component:
    return rx.chakra.grid_item(
        rx.text(f"區長：{AreaState.area_contents[area_id]['area_leader']}"),
        rx.text(f"小組長：{AreaState.area_contents[area_id]['team_leader']}"),
        rx.text(f"應到人數：{AreaState.area_contents[area_id]['expected_attendance']}"),
        rx.text(f"實到人數：{AreaState.area_contents[area_id]['actual_attendance']}"),
        rx.text(f"5S：{AreaState.area_contents[area_id]['five_s']}"),
        rx.text(f"：{AreaState.area_contents[area_id]['kind_of_product']}"),
        col_start=col_start,
        col_end=col_end,
        row_start=row_start,
        row_end=row_end,
        id="", 
        class_name=[*css_classes],
    )


def gen_h2_1_block_cells() -> rx.Component:
    return [
        gen_area_grid_cell('h2-1', 1, '7', 1, '2', ['h2-1-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('MAG03001', 1, '2', 2, '3',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('MAG03003', 2, '3', 2, '3',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('MAG03002', 3, '4', 2, '3',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('VMC02001', 1, '2', 4, '5',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('VMC02004', 3, '4', 4, '5',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('VMC08006', 1, '2', 5, '6',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('VMC08001', 2, '3', 5, '6',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('VMC08016', 3, '4', 5, '6',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('VMC08017', 4, '5', 5, '6',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('MAM01006', 5, '6', 5, '6',['machine-border-class', 'h2-1-bgc-class']),
        gen_machine_grid_cell('MAM01003', 6, '7', 5, '6',['machine-border-class', 'h2-1-bgc-class']),
    ]


def gen_kai_area1_block_cells() -> rx.Component:
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


def gen_kai_area2_block_cells() -> rx.Component:
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


def gen_h2_2_block_cells() -> rx.Component:
    return [
        gen_area_grid_cell('h2-2', 1, '6', 10, '11', ['h2-2-border-class', 'h2-2-bgc-class']),
        gen_machine_grid_cell('VMC01002', 1, '2', 8,  '9',  ['machine-border-class', 'h2-2-bgc-class']),
        gen_machine_grid_cell('VMC01001', 2, '3', 8,  '9',  ['machine-border-class', 'h2-2-bgc-class']),
        gen_machine_grid_cell('VMC01004', 3, '4', 8,  '9',  ['machine-border-class', 'h2-2-bgc-class']),
        gen_machine_grid_cell('VMC01003', 4, '5', 8,  '9',  ['machine-border-class', 'h2-2-bgc-class']),
        gen_machine_grid_cell('VMC03004', 5, '6', 8,  '9',  ['machine-border-class', 'h2-2-bgc-class']),
        gen_machine_grid_cell('NCG01005', 1, '2', 9, '10',  ['machine-border-class', 'h2-2-bgc-class']),
        gen_machine_grid_cell('NCG01001', 2, '3', 9, '10',  ['machine-border-class', 'h2-2-bgc-class']),
        gen_machine_grid_cell('NCG01002', 3, '4', 9, '10',  ['machine-border-class', 'h2-2-bgc-class']),
        gen_machine_grid_cell('NCG01003', 4, '6', 9, '10',  ['machine-border-class', 'h2-2-bgc-class']),
    ]


def gen_h1_1_block_cells() -> rx.Component:
    return [
        gen_area_grid_cell('h1-1', 7, '12', 1, '2', ['h1-1-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('MAG04001',  8,  '9', 2, '3', ['machine-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('MAG04002',  9, '10', 2, '3', ['machine-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('MAG04003', 10, '11', 2, '3', ['machine-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('VMC08004',  8,  '9', 5, '6', ['machine-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('VMC08003',  9, '10', 5, '6', ['machine-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('VMC08005', 10, '11', 5, '6', ['machine-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('MAG02002',  8,  '9', 6, '7', ['machine-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('MAG02005',  9, '10', 6, '7', ['machine-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('MAG02006', 10, '11', 6, '7', ['machine-border-class', 'h1-1-bgc-class']),
        gen_machine_grid_cell('MAG02001', 11, '12', 6, '7', ['machine-border-class', 'h1-1-bgc-class']),
    ]


def gen_h1_2_block_cells() -> rx.Component:
    return [
        gen_area_grid_cell('h1-2', 6, '12', 10, '11', ['h1-2-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('VMC02008',  6,  '7', 8,  '9', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('VMC06006',  7,  '8', 8,  '9', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('VMC06001',  8,  '9', 8,  '9', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('VMC06004',  9, '10', 8,  '9', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('VMC06003', 10, '11', 8,  '9', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('VMC06002', 11, '12', 8,  '9', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('NCG01008',  6,  '7', 9, '10', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('NCG01009',  7,  '8', 9, '10', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('NCG01010',  8,  '9', 9, '10', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('NCG01012',  9, '10', 9, '10', ['machine-border-class', 'h1-2-bgc-class']),
        gen_machine_grid_cell('NCG01013', 10, '11', 9, '10', ['machine-border-class', 'h1-2-bgc-class']),
    ]

