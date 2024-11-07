
from typing import Any

import reflex as rx


class MachinesState(rx.State):
    clicked_data: str = "Cell clicked: "
    edited_data: str = "Cell edited: "

    machines_content: dict[str, 
                           dict[str, 
                                str|dict[str, str|int]]] = {
        "VMC08024":{
            "machine_id":"VMC08024",
            #"status":"Working",

            "period_1":{
            "prod_op":"M77-OP15", 
            "target_qty":20, 
            "engineer_name":"阮黃英 F351"},
            ###
            "period_2":{
            "prod_op":"M77-OP15",
            "target_qty":100, 
            "engineer_name":"阮黃英 F351"},
            ###
            "period_3":{
            "prod_op":"M77-OP15", 
            "target_qty":200, 
            "engineer_name":"阮黃英 F351"},
            ###
            "period_4":{
            "prod_op":"M77-OP15", 
            "target_qty":200, 
            "engineer_name":"阮黃英 F351"},
            ###
            },

        "VMC08026":{
            "machine_id":"VMC08026", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP15", 
            "target_qty":20, 
            "engineer_name":"范文成 F279"},
            "period_2":{
            "prod_op":"M77-OP15", 
            "target_qty":300, 
            "engineer_name":"范文成 F279"},
            "period_3":{
            "prod_op":"M77-OP15", 
            "target_qty":200, 
            "engineer_name":"范文成 F279"},
            "period_4":{
            "prod_op":"M77-OP15", 
            "target_qty":200, 
            "engineer_name":"范文成 F279"},
            },

        "VMC08018":{
            "machine_id":"VMC08018", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP30", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            "period_2":{
            "prod_op":"M77-OP30", 
            "target_qty":0, 
            "engineer_name":"范文成 F279"},
            "period_3":{
            "prod_op":"M77-OP30", 
            "target_qty":0, 
            "engineer_name":"范文成 F279"},
            "period_4":{
            "prod_op":"M77-OP30", 
            "target_qty":0, 
            "engineer_name":"范文成 F279"},
            },

        "VMC08029":{
            "machine_id":"VMC08029", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP20", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            "period_2":{
            "prod_op":"M77-OP20", 
            "target_qty":0, 
            "engineer_name":"范文成 F279"},
            "period_3":{
            "prod_op":"M77-OP20", 
            "target_qty":0, 
            "engineer_name":"范文成 F279"},
            "period_4":{
            "prod_op":"M77-OP20", 
            "target_qty":0, 
            "engineer_name":"范文成 F279"},
            },

        "VMC08031":{
            "machine_id":"VMC08031", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP45", 
            "target_qty":20, 
            "engineer_name":"范文成 F279"},
            "period_2":{
            "prod_op":"M77-OP45", 
            "target_qty":20, 
            "engineer_name":"范文成 F279"},
            "period_3":{
            "prod_op":"M77-OP45", 
            "target_qty":20, 
            "engineer_name":"范文成 F279"},
            "period_4":{
            "prod_op":"M77-OP45", 
            "target_qty":20, 
            "engineer_name":"范文成 F279"},
            },

        "VMC08014":{
            "machine_id":"VMC08014", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351"},
            "period_2":{
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351"},
            "period_3":{
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351"},
            "period_4":{
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351"},
            },

        "VMC08015":{
            "machine_id":"VMC08015", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351"},
            "period_2":{
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351"},
            "period_3":{
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351"},
            "period_4":{
            "prod_op":"M77-OP60", 
            "target_qty":15, 
            "engineer_name":"阮黃英 F351"},
            },

        "VMC08030":{
            "machine_id":"VMC08030", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP30", 
            "target_qty":20, 
            "engineer_name":"范文成 F279"},
            "period_2":{
            "prod_op":"M77-OP30", 
            "target_qty":20, 
            "engineer_name":"范文成 F279"},
            "period_3":{
            "prod_op":"M77-OP30", 
            "target_qty":20, 
            "engineer_name":"范文成 F279"},
            "period_4":{
            "prod_op":"M77-OP30", 
            "target_qty":20, 
            "engineer_name":"范文成 F279"},
            },

        "MAM01022":{
            "machine_id":"MAM01022", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_2":{
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_3":{
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_4":{
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            },

        "VMC08028":{
            "machine_id":"VMC08028", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP45", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            "period_2":{
            "prod_op":"M77-OP45", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            "period_3":{
            "prod_op":"M77-OP45", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            "period_4":{
            "prod_op":"M77-OP45", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            },

        "VMC08027":{
            "machine_id":"VMC08028", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M75-OP42", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            "period_2":{
            "prod_op":"M75-OP42", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            "period_3":{
            "prod_op":"M75-OP42", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            "period_4":{
            "prod_op":"M75-OP42", 
            "target_qty":16, 
            "engineer_name":"范文成 F279"},
            },

        "VMC08020":{
            "machine_id":"VMC08020", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279"},
            "period_2":{
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279"},
            "period_3":{
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279"},
            "period_4":{
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279"},
            },

        "VMC08021":{
            "machine_id":"VMC08021", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279"},
            "period_2":{
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279"},
            "period_3":{
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279"},
            "period_4":{
            "prod_op":"M76-OP30", 
            "target_qty":24, 
            "engineer_name":"范文成 F279"},
            },
        "VMC08013":{
            "machine_id":"VMC08013", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243"},
            "period_2":{
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243"},
            "period_3":{
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243"},
            "period_4":{
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243"},
            },

        "VMC08012":{
            "machine_id":"VMC08012", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M76-OP40", 
            "target_qty":16, 
            "engineer_name":"范智南 F243"},
            "period_2":{
            "prod_op":"M76-OP40", 
            "target_qty":16, 
            "engineer_name":"范智南 F243"},
            "period_3":{
            "prod_op":"M76-OP40", 
            "target_qty":16, 
            "engineer_name":"范智南 F243"},
            "period_4":{
            "prod_op":"M76-OP40", 
            "target_qty":16, 
            "engineer_name":"范智南 F243"},
            },

        "VMC08019":{
            "machine_id":"VMC08019", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243"},
            "period_2":{
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243"},
            "period_3":{
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243"},
            "period_4":{
            "prod_op":"M76-OP40", 
            "target_qty":8, 
            "engineer_name":"范智南 F243"},
            },

        "MAM01021":{
            "machine_id":"MAM01021", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_2":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_3":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_4":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            },

        "MAM01010":{
            "machine_id":"MAM01010", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            "period_2":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            "period_3":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            "period_4":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            },
        "MAM01013":{
            "machine_id":"MAM01013", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            "period_2":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            "period_3":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            "period_4":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            },

        "MAM01014":{
            "machine_id":"MAM01014", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            "period_2":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            "period_3":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            "period_4":{
            "prod_op":"M75-OP40", 
            "target_qty":12, 
            "engineer_name":"阮文陽 F271"},
            },
        "MAM01017":{
            "machine_id":"MAM01017", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_2":{
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_3":{
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_4":{
            "prod_op":"M77-OP50", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            },

        "MAM01019":{
            "machine_id":"MAM01017", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_2":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_3":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_4":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            },

        "MAM01020":{
            "machine_id":"MAM01020", 
            #"status":"Working",
            "period_1":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_2":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_3":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            "period_4":{
            "prod_op":"M77-OP70", 
            "target_qty":8, 
            "engineer_name":"阮文黃 F297"},
            },
            # kAI SIMULATION END
    }
    
    width_machine_id: int = 200
    width_prod_op: int = 190
    width_target_qty: int = 120
    width_engineer_name: int = 190

    cols: list[dict[str, str]] = [
        # ret_list=[
        # ['vmc001', 'm77op15', 10, 'Alex', 'm77op20', 20, 'Bill', 'm77op30', 30, 'Cox', 'm77op40', 40, 'David'], 
        # ['vmc101', 'm65op15', 10, 'Allen', 'm65op20', 20, 'Banson', 'm65op30', 30, 'Carol', 'm65op40', 40, 'Denzel'], 
        # ['vmc202', 'm93op15', 10, 'Apollo', 'm93op20', 20, 'Brain', 'm93op30', 30, 'Card', 'm93op40', 40, 'Daniel']
        # ]
        {
            'title':'機台代號', #NOTE - MACHINE: machine_id
            'type':'str',
            'width':width_machine_id,
        },
        ###
        {
            'group':'早班',
            'title':'件號', #NOTE - PRODUCT: prod_op
            'type':'str',
            'width':width_prod_op,
        },
        {
            'group':'早班',
            'title':'數量', #NOTE - QUANTITY: target_qty
            'type':'int',
            'width':width_target_qty,
        },
        {
            'group':'早班',
            'title':'操作者', #NOTE - ENGINEER: engineer_name
            'type':'str',
            'width':width_engineer_name,
        },
        ###
        {
            'group':'午班-1',
            'title':'件號', #NOTE - PRODUCT: prod_op
            'type':'str',
            'width':width_prod_op,
        },
        {
            'group':'午班-1',
            'title':'數量', #NOTE - QUANTITY: target_qty
            'type':'int',
            'width':width_target_qty,
        },
        {
            'group':'午班-1',
            'title':'操作者', #NOTE - ENGINEER: engineer_name
            'type':'str',
            'width':width_engineer_name,
        },
        ###
        {
            'group':'午班-2',
            'title':'件號', #NOTE - PRODUCT: prod_op
            'type':'str',
            'width':width_prod_op,
        },
        {
            'group':'午班-2',
            'title':'數量', #NOTE - QUANTITY: target_qty
            'type':'int',
            'width':width_target_qty,
        },
        {
            'group':'午班-2',
            'title':'操作者', #NOTE - ENGINEER: engineer_name
            'type':'str',
            'width':width_engineer_name,
        },
        ###
        {
            'group':'晚班',
            'title':'件號', #NOTE - PRODUCT: prod_op
            'type':'str',
            'width':width_prod_op,
        },
        {
            'group':'晚班',
            'title':'數量', #NOTE - QUANTITY: target_qty
            'type':'int',
            'width':width_target_qty,
        },
        {
            'group':'晚班',
            'title':'操作者', #NOTE - ENGINEER: engineer_name
            'type':'str',
            'width':width_engineer_name,
        },
        ###

    ]

    def convert_dict_to_list(self, data:dict[str, dict[str, str|int]]) -> list[list[Any]]:
        return [list(inner_dict.values()) for inner_dict in data.values()]
    
    def convert_dict_to_list(self, data:dict[str, dict[str, str|dict[str, str|int]]]):
        unpack_1 = [list(inner_dict_element.values()) for inner_dict_element in data.values()]
        unpack_2 = []
        for i in unpack_1:
            temp_list = []
            for d in i:
                if isinstance(d, dict):
                    temp_list.extend(d.values())
                else:
                    temp_list.append(d)
            unpack_2.append(temp_list)
        return unpack_2
    
    @rx.var
    def machine_data(self) -> list[list[Any]]:
        return self.convert_dict_to_list(self.machines_content)
    
    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)

    def get_clicked_data(self, pos) -> None:
        self.clicked_data = f'Cell clicked: {pos}'

    def field_helper_col_period(self, col_num):
        if col_num in (0, ):
            return 'mahcine_id'
        elif col_num in (1,2,3):
            return 'period_1'
        elif col_num in (4,5,6):
            return 'period_2'
        elif col_num in (7,8,9):
            return 'period_3'
        else:
            return 'period_4'
        
    def field_helper_col_name(self, col_num):
        reminder = col_num % 3
        if reminder == 1:
            return 'prod_op'
        elif reminder == 2:
            return 'target_qty'
        else:
            return 'engineer_name'
        
    def change_field_val(self, machine_id, col, value):
        ret_period = self.field_helper_col_period(col)
        ret_col_name = self.field_helper_col_name(col)
        if ret_period == 'machine_id':
            self.machines_content[machine_id][ret_period] = value['data'] #NOTE - Here ret_period = 'machine_id
        else:
            self.machines_content[machine_id][ret_period][ret_col_name] = value['data']

    def handle_cell_edit(self, pos, val) -> None:
        col, row = pos
        machine_id = list(self.machines_content.keys())[row] # eg: [MAM01017, MAM01019, MAM01020]
        self.edited_data = f'Cell edited: {pos}, Cell value: {val["data"]}' # To be confirm
        self.change_field_val(machine_id, col, val)

