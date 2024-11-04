
import reflex as rx
import reflex_chakra as rc

from .states import MachinesState


#TODO - Change MachineSatate key's name
#TODO - To separate functin for different periods
def gen_machine_grid_cell(machine_id: str,
                          inner_period: str, # Add this argument 
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
                rx.text(f"{MachinesState.machines_content[machine_id].to(dict)[inner_period].to(dict)['prod_op']}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                #rx.text(f"{MachinesState.machines_content[machine_id].to(dict)['period_1'].to(dict)['prod_op']}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                #NOTE - inkeep is being funny, i would recommend structuring your data in a dataclass or rx.Base class
                # if that's not an option, you can do MachinesState.machines_content[machine_id].to(dict)['period_1'].to(dict)['prod_op'] 
                # essentially, doing .to(dict) tells reflex "this is a dict, and you can access fields in it using object item"
                # the issue in the code above is that there's a union between str and dict, 
                # so when you're doing a [] it doesn't understand which one you mean
                
                #NOTE - To reproduce error by using the following code
                #rx.text(f"{type(MachinesState.machines_content[machine_id]['period_1'])}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                
                #rx.text(f"{MachinesState.machines_content[machine_id]['period_1'].to_string()}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                #NOTE - Original code
                #rx.text(f"{MachinesState.machines_content[machine_id]['period_1']['prod_op']}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                
                rx.text(f" |=> ", white_space="pre", font_size=size_of_font),
                rx.text(f"數量：", weight='bold', font_size=size_of_font),
                rx.text(f"{MachinesState.machines_content[machine_id].to(dict)[inner_period].to(dict)['target_qty']}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
                direction='row',
            ), # rx.flex
            rx.flex(
                rx.text(f"操作者：", weight='bold', font_size=size_of_font),
                rx.text(f"{MachinesState.machines_content[machine_id].to(dict)[inner_period].to(dict)['engineer_name']}", weight='medium', font_size=size_of_font, high_contrast=True, color_scheme='bronze'),
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





def gen_area_1_block_cells(outer_period: str) -> list[rx.Component]:
    return [ # 13
        gen_machine_grid_cell('VMC08024', outer_period, 2, '3', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08026', outer_period, 3, '4', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08018', outer_period, 4, '5', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08029', outer_period, 5, '6', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08031', outer_period, 6, '7', 1, '2',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08014', outer_period, 2, '3', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08015', outer_period, 3, '4', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08030', outer_period, 4, '5', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('MAM01022', outer_period, 6, '7', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08028', outer_period, 7, '8', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"), #10
        gen_machine_grid_cell('VMC08027', outer_period, 8, '9', 2, '3',   ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08020', outer_period, 9, '10', 2, '3',  ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('VMC08021', outer_period, 10, '11', 2, '3', ['cell-border', 'cell-bgc-1'], "1.85vmin")
    ]

def gen_area_2_block_cells(outer_period: str) -> list[rx.Component]:
    return [ # 10
        gen_machine_grid_cell('VMC08013', outer_period, 2, '3', 3, '4', ['cell-border', 'cell-bgc-3'], "1.85vmin"),
        gen_machine_grid_cell('VMC08012', outer_period, 3, '4', 3, '4', ['cell-border', 'cell-bgc-3'], "1.85vmin"),
        gen_machine_grid_cell('VMC08019', outer_period, 4, '5', 3, '4', ['cell-border', 'cell-bgc-3'], "1.85vmin"),
        gen_machine_grid_cell('MAM01021', outer_period, 6, '7', 3, '4', ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('MAM01010', outer_period, 1, '2', 4, '5', ['cell-border', 'cell-bgc-2'], "1.85vmin"),
        gen_machine_grid_cell('MAM01013', outer_period, 2, '3', 4, '5', ['cell-border', 'cell-bgc-2'], "1.85vmin"),
        gen_machine_grid_cell('MAM01014', outer_period, 3, '4', 4, '5', ['cell-border', 'cell-bgc-2'], "1.85vmin"),
        gen_machine_grid_cell('MAM01017', outer_period, 4, '5', 4, '5', ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('MAM01019', outer_period, 5, '6', 4, '5', ['cell-border', 'cell-bgc-1'], "1.85vmin"),
        gen_machine_grid_cell('MAM01020', outer_period, 6, '7', 4, '5', ['cell-border', 'cell-bgc-1'], "1.85vmin")
    ]