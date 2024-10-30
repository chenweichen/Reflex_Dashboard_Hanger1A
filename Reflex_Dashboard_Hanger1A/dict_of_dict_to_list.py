
mcahines_content:dict[str, dict[str, str|dict[str, str|int]]] = {
    "vmc001":{
        "machine_id":"vmc001",
        "period_1":{
            "prod_op":"m77op15",
            "target_qty":10,
            "engineer_name":"Alex",
        },
        "period_2":{
            "prod_op":"m77op20",
            "target_qty":20,
            "engineer_name":"Bill",
        },
        "period_3":{
            "prod_op":"m77op30",
            "target_qty":30,
            "engineer_name":"Cox",
        },
        "period_4":{
            "prod_op":"m77op40",
            "target_qty":40,
            "engineer_name":"David",
        },
    },
    "vmc101":{
        "machine_id":"vmc101",
        "period_1":{
            "prod_op":"m65op15",
            "target_qty":10,
            "engineer_name":"Allen",
        },
        "period_2":{
            "prod_op":"m65op20",
            "target_qty":20,
            "engineer_name":"Banson",
        },
        "period_3":{
            "prod_op":"m65op30",
            "target_qty":30,
            "engineer_name":"Carol",
        },
        "period_4":{
            "prod_op":"m65op40",
            "target_qty":40,
            "engineer_name":"Denzel",
        },
    },
    "vmc202":{
        "machine_id":"vmc202",
        "period_1":{
            "prod_op":"m93op15",
            "target_qty":10,
            "engineer_name":"Apollo",
        },
        "period_2":{
            "prod_op":"m93op20",
            "target_qty":20,
            "engineer_name":"Brain",
        },
        "period_3":{
            "prod_op":"m93op30",
            "target_qty":30,
            "engineer_name":"Card",
        },
        "period_4":{
            "prod_op":"m93op40",
            "target_qty":40,
            "engineer_name":"Daniel",
        },
    },
}

print(f"{mcahines_content['vmc001']['period_1']['prod_op']=}\n")

#print(f"{mcahines_content.keys()=} \n")
#print(f"{mcahines_content.values()=} \n")

#print(f"{mcahines_content['vmc202']} \n")
print(f"{mcahines_content['vmc202'].keys()=} \n")

def get_machine_id(content, row):
    return list(content.keys())[row]

ret_machine_id = get_machine_id(mcahines_content, 2) #vmc202
print(f"{ret_machine_id=} \n")

def field_helper_col_period(col):
    if col in (0,):
        return 'machine_id'
    elif col in (1,2,3):
        return 'period_1'
    elif col in (4,5,6):
        return 'period_2'
    elif col in (7,8,9):
        return 'period_3'
    else:
        return 'period_4'
    
def field_helper_col_name(col):
    reminder = col % 3
    if reminder == 1:
        return 'prod_op'
    elif reminder == 2:
        return 'target_qty'
    else:
        return 'engineer_name'

def get_field(content, machine_id, col):
    ret_period = field_helper_col_period(col)
    print(f"{ret_period=}")
    ret_col_name = field_helper_col_name(col)
    print(f"{ret_col_name=}")
    if ret_period == 'machine_id':
        return content[machine_id]['machine_id']
    else :
        return content[machine_id][ret_period][ret_col_name]


ret_field = get_field(mcahines_content, ret_machine_id, 10)
print(f"{ret_field=} \n")



simple = {
    "vmc991":{
        "machine_id":"vmc991",
        "prod_op":"m99-op10",
        "target_qty":153,
        "engineer":"Abel",
        }
    }

#print(f"{simple["vmc991"]}\n")
#print(f"{simple["vmc991"].keys()}\n")
#print(f"{list(simple["vmc991"].keys())}\n")
#print(f"{list(simple["vmc991"].keys())[2]}\n")


def prototype(content):
    val_1 = content.values()
    #print(f"{val_1=} \n")
    #print(f"{list(val_1)[0]=} \n")
    val_2 = [list(inner_dict_element.values()) for inner_dict_element in  content.values()]
    #print(f"{val_2=}\n")
    #temp_21 = val_2[0]
    #print(f"{temp_21=}\n")
    #temp_list = []
    #for i in temp_21: # temp_21
    #    if isinstance(i, dict):
    #        temp_list.extend(i.values())
    #    else :
    #        temp_list.append(i)
    #print(f"{temp_list=}\n")

    ret_list = []
    for i in val_2:
        temp_list = []
        for d in i:
            if isinstance(d, dict):
                temp_list.extend(d.values())
            else:
                temp_list.append(d)
        ret_list.append(temp_list)
    print(f"{ret_list=}\n")


#prototype(mcahines_content)

