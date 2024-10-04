
from typing import Any

import reflex as rx


class MachineState(rx.State):
    clicked_data: str = "Cell clicked: "
    edited_data: str = "Cell edited: "

    machine_contents: dict[str, dict[str, str|int]] = {
        # Kai Simulation
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
        
        ## H2-1 Start
        #"MAG03001":{
        #    "machine_id":"MAG03001", 
        #    #"status":"Working",
        #    "prod_op":"M7X-OP01", 
        #    "target_qty":11, 
        #    "engineer_name":"劉嘉瑜", 
        #    }, #1-1
        #"MAG03003":{
        #    "machine_id":"MAG03003", 
        #    #"status":"待料",
        #    "prod_op":"M7X-OP02", 
        #    "target_qty":12, 
        #    "engineer_name":"阮文留", 
        #    }, #1-2
        #"MAG03002":{
        #    "machine_id":"MAG03002", 
        #    #"status":"故障",
        #    "prod_op":"M7X-OP03", 
        #    "target_qty":13, 
        #    "engineer_name":"潘莊黃娟", 
        #    }, #1-3
        ##H2-1 End
        ##H2-1 Start
        #"VMC02001":{
        #    "machine_id":"VMC02001", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #2-1
        #"VMC02004":{
        #    "machine_id":"VMC02004", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #2-3
        #"VMC08001":{
        #    "machine_id":"VMC08001", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #3-1
        #"VMC08006":{
        #    "machine_id":"VMC08006", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #3-2
        #"VMC08016":{
        #    "machine_id":"VMC08016", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #3-3
        ##H2-1 End
        ##H2-1 Start
        #"VMC08017":{
        #    "machine_id":"VMC08017", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #3-4
        #"MAM01006":{
        #    "machine_id":"MAM01006", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #3-5
        #"MAM01003":{
        #    "machine_id":"MAM01003", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #3-6
        ##H2-1 End
        ##H2-1 Start
        #"MAG02003":{
        #    "machine_id":"MAG02003", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #4-1
        #"MAG02004":{
        #    "machine_id":"MAG02004", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #4-3
        #"MAG02007":{
        #    "machine_id":"MAG02007", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #4-5
        ##H2-1 End
#
#
#
        ##H1-1 Start
        #"MAG04001":{
        #    "machine_id":"MAG04001", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #1-4 
        #"MAG04002":{
        #    "machine_id":"MAG04002", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #1-5
        #"MAG04003":{
        #    "machine_id":"MAG04003", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #1-6
        ##H1-1 End
        ##H1-1 Start
        #"VMC08004":{
        #    "machine_id":"VMC08004", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #3-7
        #"VMC08003":{
        #    "machine_id":"VMC08003", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #3-8
        #"VMC08005":{
        #    "machine_id":"VMC08005", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #3-9
        ##H1-1 End
        ##H1-1 Start
        #"MAG02002":{
        #    "machine_id":"MAG02002", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #4-7
        #"MAG02005":{
        #    "machine_id":"MAG02005", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #4-9
        #"MAG02006":{
        #    "machine_id":"MAG02006", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #4-10
        #"MAG02001":{
        #    "machine_id":"MAG02001", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #4-11
        ##H1-1 End
#
#
        ##H2-2 Start
        #"VMC01002":{
        #    "machine_id":"VMC01002", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-1
        #"VMC01001":{
        #    "machine_id":"VMC01001", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-2
        #"VMC01004":{
        #    "machine_id":"VMC01004", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-3
        #"VMC01003":{
        #    "machine_id":"VMC01003", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-4
        #"VMC03004":{
        #    "machine_id":"VMC03004", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-5
        ##H2-2 End
        ##H2-2 Start
        #"NCG01005":{
        #    "machine_id":"NCG01005", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #6-1
        #"NCG01001":{
        #    "machine_id":"NCG01001", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #6-2
        #"NCG01002":{
        #    "machine_id":"NCG01002", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #6-3
        #"NCG01003":{
        #    "machine_id":"NCG01003", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #6-4
        ##H2-2 End



        ##H1-2 Start
        #"VMC02008":{
        #    "machine_id":"VMC02008", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-6
        #"VMC06006":{
        #    "machine_id":"VMC06006", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-7
        #"VMC06001":{
        #    "machine_id":"VMC06001", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-8
        #"VMC06004":{
        #    "machine_id":"VMC06004", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-9
        #"VMC06003":{
        #    "machine_id":"VMC06003", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-10
        #"VMC06002":{
        #    "machine_id":"VMC06002", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #5-11
        ##H1-2 End
        ##H1-2 Start
        #"NCG01008":{
        #    "machine_id":"NCG01008", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #6-6
        #"NCG01009":{
        #    "machine_id":"NCG01009", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #6-7
        #"NCG01010":{
        #    "machine_id":"NCG01010", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #6-8
        #"NCG01012":{
        #    "machine_id":"NCG01012", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #6-9
        #"NCG01013":{
        #    "machine_id":"NCG01013", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #6-11
        ##H1-2 End


        
        #Not In The List
        #"EDM05001":{
        #    "machine_id":"EDM05001", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #1-8
        #"EDM03005":{
        #    "machine_id":"EDM03005", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #1-10
        #"EDM03006":{
        #    "machine_id":"EDM03006", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #1-11        
        #"VMC08012":{
        #    "machine_id":"VMC08012", 
        #    #"status":"",
        #    "prod_op":"M7X-OP0", 
        #    "target_qty":1, 
        #    "engineer_name":"Mr. Smith", 
        #    }, #
        ##Not In The List  
#

##################
        }
    cols: list[dict[str, str|int]] = [
        {
            'title':'MACHINE',
            'type':'str'
        },
        #{
        #    'title':'STATUS',
        #    'type':'str',
        #},
        {
            'title':'PRODUCT',
            'type':'str',
        },
        {
            'title':'QUANTITY',
            'type':'int',
        },
        {
            'title':'ENGINEER',
            'type':'str',
        },
    ]

    def convert_dict_to_list(self, data:dict[str, dict[str, str|int]]) -> list[list[Any]]:
        return [list(inner_dict.values()) for inner_dict in data.values()]
    
    @rx.var
    def machine_data(self) -> list[list[Any]]:
        return self.convert_dict_to_list(self.machine_contents)


    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)

    def get_clicked_data(self, pos) -> None:
        self.clicked_data = f'Cell clicked: {pos}'

    def handle_cell_edit(self, pos, val):
        col, row = pos
        machine_id = list(self.machine_contents.keys())[row]
        field = list(self.machine_contents[machine_id].keys())[col]
        self.edited_data = f'Cell edited: {pos}, Cell value: {val["data"]}'
        self.machine_contents[machine_id][field] = val['data']



class AreaState(rx.State):
    area_contents: dict[str, dict[str, str|int]] = {
        'h2-1': {
            'area_leader':"Area 2-1",
            'team_leader':"Team 2-1",
            'expected_attendance':17,
            'actual_attendance':13,
            'five_s':'Five 2-1',
            'kind_of_product':'水蜘蛛',
        },
        'h1-1': {
            'area_leader':"Area 1-1",
            'team_leader':"Team 1-1",
            'expected_attendance':12,
            'actual_attendance':8,
            'five_s':'Five 1-1',
            'kind_of_product':'水蜘蛛',
        },
        'h2-2': {
            'area_leader':"Area 2-2",
            'team_leader':"Team 2-2",
            'expected_attendance':19,
            'actual_attendance':11,
            'five_s':'Five 2-2',
            'kind_of_product':'水蜘蛛',
        },
        'h1-2': {
            'area_leader':"Area 1-2",
            'team_leader':"Team 1-2",
            'expected_attendance':10,
            'actual_attendance':6,
            'five_s':'Five 1-2',
            'kind_of_product':'水蜘蛛',
        },
    }





