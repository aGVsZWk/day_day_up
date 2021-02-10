"""
半价优惠
"""
from typing import List
from etc.config import Config


class HalfPrice:

    @staticmethod
    def count_price(food_list: List[dict]) -> int:
        """
        计算指定菜品半价后的价格
        """
        total_price = 0
        for food in food_list:
            price = food.get('price_discount', 0)

            # -1 表示没有优惠价格，使用原价
            if price == -1:
                price = food.get('price_original', 0)

            num = food['num']
            total_price += (price * num)
        return total_price

    @staticmethod
    def info_discount(food_list: List[dict]) -> str:
        """
        生成半价优惠信息

        例如：
        使用优惠:
        指定菜品半价(黄焖鸡，凉皮)，省13元
        """
        save_total = 0
        save_names = []
        for food in food_list:
            price_original = food.get('price_original', 0)
            price_half = food.get('price_discount', 0)

            if price_half != -1:
                save = (price_original - price_half)
                save_total += save

                name = food.get('name', '')
                save_names.append(name)

        food_names = '，'.join(save_names)
        info = Config().template_info_half_price.format(
            food_names=food_names,
            save_total=save_total,
        )
        return info
