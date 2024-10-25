
from typing import Any

import reflex as rx


class MachinesState(rx.State):
    clicked_data: str = "Cell clicked: "
    edited_data: str = "Cell edited: "

    machines_content: dict[str, dict[str, str|int]] = {
        "VMC08024":{
            "machine_id":"VMC08024", 
            #"status":"Working",
            "prod_op":"M77-OP15", 
            "target_qty":20, 
            "engineer_name":"阮黃英 F351", 
            },
        "VMC08026":{
            "machine_id":"VMC08026", 
            #"status":"Working",
            "prod_op":"M77-OP15", 
            "target_qty":20, 
            "engineer_name":"范文成 F279", 
            },
        "VMC08018":{
            "machine_id":"VMC08018", 
            #"status":"Working",
            "prod_op":"M77-OP30", 
            "target_qty":16, 
            "engineer_name":"范文成 F279", 
            },
        "VMC08029":{
            "machine_id":"VMC08029", 
            #"status":"Working",
            "prod_op":"M77-OP20", 
            "target_qty":16, 
            "engineer_name":"范文成 F279", 
            },
        "VMC08031":{
            "machine_id":"VMC08031", 
            #"status":"Working",
            "prod_op":"M77-OP45", 
            "target_qty":20, 
            "engineer_name":"范文成 F279", 
            },
        "VMC08014":{
            "machine_id":"VMC08014", 
            #"status":"Working",
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351", 
            },
        "VMC08015":{
            "machine_id":"VMC08015", 
            #"status":"Working",
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351", 
            },
        "VMC08030":{
            "machine_id":"VMC08030", 
            #"status":"Working",
            "prod_op":"M77-OP30", 
            "target_qty":20, 
            "engineer_name":"范文成 F279", 
            },
        "MAM01022":{
            "machine_id":"MAM01022", 
            #"status":"Working",
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297", 
            },
        "VMC08028":{
            "machine_id":"VMC08028", 
            #"status":"Working",
            "prod_op":"M77-OP45", 
            "target_qty":16, 
            "engineer_name":"范文成 F279", 
            },
        "VMC08027":{
            "machine_id":"VMC08028", 
            #"status":"Working",
            "prod_op":"M75-OP42", 
            "target_qty":16, 
            "engineer_name":"范文成 F279", 
            },
        "VMC08020":{
            "machine_id":"VMC08020", 
            #"status":"Working",
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279", 
            },
        "VMC08021":{
            "machine_id":"VMC08021", 
            #"status":"Working",
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279", 
            },
        "VMC08013":{
            "machine_id":"VMC08013", 
            #"status":"Working",
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243", 
            },
        "VMC08012":{
            "machine_id":"VMC08012", 
            #"status":"Working",
            "prod_op":"M76-OP40", 
            "target_qty":16, 
            "engineer_name":"范智南 F243", 
            },
        "VMC08019":{
            "machine_id":"VMC08019", 
            #"status":"Working",
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243", 
            },
        "MAM01021":{
            "machine_id":"MAM01021", 
            #"status":"Working",
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297", 
            },
        "MAM01010":{
            "machine_id":"MAM01010", 
            #"status":"Working",
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271", 
            },
        "MAM01013":{
            "machine_id":"MAM01013", 
            #"status":"Working",
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271", 
            },
        "MAM01014":{
            "machine_id":"MAM01014", 
            #"status":"Working",
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271", 
            },
        "MAM01017":{
            "machine_id":"MAM01017", 
            #"status":"Working",
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297", 
            },
        "MAM01019":{
            "machine_id":"MAM01017", 
            #"status":"Working",
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297", 
            },
        "MAM01020":{
            "machine_id":"MAM01020", 
            #"status":"Working",
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297", 
            },
            # kAI SIMULATION END
    }

    cols: list[dict[str, str]] = [
        {
            'title':'機台代號', #NOTE - MACHINE: machine_id
            'type':'str'
        },
        {
            'title':'件號', #NOTE - PRODUCT: prod_op
            'type':'str'
        },
        {
            'title':'數量', #NOTE - QUANTITY: target_qty
            'type':'int'
        },
        {
            'title':'操作者', #NOTE - ENGINEER: engineer_name
            'type':'str'
        }
    ]

    def convert_dict_to_list(self, data:dict[str, dict[str, str|int]]) -> list[list[Any]]:
        return [list(inner_dict.values()) for inner_dict in data.values()]
    
    @rx.var
    def machine_data(self) -> list[list[Any]]:
        return self.convert_dict_to_list(self.machines_content)
    
    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)

    def get_clicked_data(self, pos) -> None:
        self.clicked_data = f'Cell clicked: {pos}'

    def handle_cell_edit(self, pos, val) -> None:
        col, row = pos
        machine_id = list(self.machines_content.keys())[row]
        field = list(self.machines_content[machine_id].keys())[col]
        self.edited_data = f'Cell edited: {pos}, Cell value: {val["data"]}'
        self.machines_content[machine_id][field] = val['data']
