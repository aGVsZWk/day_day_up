"""
满减优惠
"""
from typing import List
from etc.config import Config
from model.food import Food


class MoneyOff:

    @staticmethod
    def count_price(food_list: List[dict]) -> int:
        """
        计算满减后的价格
        """
        total_price = Food.price_original_total(food_list)
        if total_price >= Config().money_off_floor:
            total_price -= Config().money_off_price

        return total_price

    @staticmethod
    def info_discount() -> str:
        """
        生成满减优惠信息

        例如：
        使用优惠:
        满30减6元，省6元
        """
        info = Config().template_info_money_off.format(
            money_off_floor=Config().money_off_floor,
            money_off_price=Config().money_off_price,
        )
        return info
