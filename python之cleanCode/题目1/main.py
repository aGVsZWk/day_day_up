from typing import List
from module.order_detail import OrderDetail


def bestCharge(input_: List[str]):
    info = OrderDetail.info_summary(input_)
    return info

