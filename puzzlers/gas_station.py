from collections import namedtuple


def find_path(in_list):
    """
    interview question
    :param in_list: list
    :return: first passed route in with N complexity
    """

    cum_miles = 0
    segment_miles = 0
    pop_rtn_id_flag = True
    rtn_id = 0

    for item in in_list:
        if pop_rtn_id_flag:
            pop_rtn_id_flag = False
            rtn_id = item.id

        segment_miles = segment_miles + item.gas_quantity - item.distance_to_next_station
        cum_miles = cum_miles + segment_miles
        if segment_miles < 0:
            pop_rtn_id_flag = True
            segment_miles = 0

    if cum_miles < 0:
        rtn_id = -1

    return rtn_id


if __name__ == "__main__":
    gas_station = namedtuple("gas_station", ["id", "gas_quantity", "distance_to_next_station"])
    gs1 = gas_station(1, 200, 200)
    gs2 = gas_station(2, 200, 200)
    gs3 = gas_station(3, 200, 200)
    gs4 = gas_station(4, 200, 201)
    gs5 = gas_station(5, 200, 200)
    gs6 = gas_station(6, 200, 200)
    gs7 = gas_station(7, 200, 201)
    gs8 = gas_station(8, 200, 201)
    gs9 = gas_station(9, 200, 200)
    gs10 = gas_station(10, 201, 200)
    gs11 = gas_station(11, 200, 200)
    gs12 = gas_station(12, 202, 200)

    gas_station_list = [gs1, gs2, gs3, gs4, gs5, gs6, gs7, gs8, gs9, gs10, gs11, gs12]
    rtn = find_path(gas_station_list)
    print(rtn)
