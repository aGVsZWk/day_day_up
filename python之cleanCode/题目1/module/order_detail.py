"""
订单明细输出
"""
from typing import List

from etc.config import Config
from module.discount.EnumDiscount import EnumDiscount
from module.discount.half_price import HalfPrice
from module.discount.money_off import MoneyOff
from model.food import Food


class OrderDetail:

    @classmethod
    def parse_input(cls, input_: List[str]) -> List[dict]:
        """
        解析输入，添加购买数量，返回餐品对象列表

        直接返回对象，相当于使用缓存，后续接口不需要再查询数据库，提高效率
        """
        food_list = []
        for item in input_:
            parts = item.split('x')
            food_uid = parts[0].strip()

            food = Food.food_obj(food_uid)
            num = int(parts[1].strip())
            food['num'] = num

            food_list.append(food)

        return food_list

    @classmethod
    def info_summary(cls, input_: List[str]) -> str:
        """
        生成订单明细信息
        """
        food_list = cls.parse_input(input_)

        info_food_list = cls.info_food_list(food_list)
        info_discount = cls.info_discount(food_list)
        info_final_price = cls.info_final_price(food_list)

        if info_discount:
            info_list = [info_food_list, info_discount, info_final_price]
        else:
            info_list = [info_food_list, info_final_price]

        order_detail_info = Config().order_detail_separator.join(info_list)
        info = Config().template_order_detail.format(
            order_detail_info=order_detail_info,
        )

        return info

    @classmethod
    def discount_type(cls, food_list: List[dict]) -> EnumDiscount:
        """
        判断优惠类型
        """
        original = Food.price_original_total(food_list)
        p1 = MoneyOff.count_price(food_list)
        p2 = HalfPrice.count_price(food_list)

        if (p1 < original) and (p1 <= p2):
            return EnumDiscount.moneyOff
        elif (p2 < original) and (p2 < p1):
            return EnumDiscount.halfPrice
        else:
            return EnumDiscount.noDiscount

    @classmethod
    def price_final(cls, food_list: List[dict]):
        """
        根据多种优惠类型，返回最低的价格
        """
        p1 = MoneyOff.count_price(food_list)
        p2 = HalfPrice.count_price(food_list)
        p = min(p1, p2)
        return p

    @classmethod
    def info_food_list(cls, food_list: List[dict]) -> str:
        """
        餐品列表明细
        """
        li = []
        for food in food_list:
            price = food.get('price_original')
            num = food['num']
            total_price = (price * num)

            food_name = food.get('name', '')
            line = Config().template_food_info.format(
                food_name=food_name,
                num=num,
                total_price=total_price,
            )
            li.append(line)

        info = '\n'.join(li)
        return info

    @classmethod
    def info_discount(cls, food_list: List[dict]) -> str:
        """
        优惠明细信息
        """
        type_ = cls.discount_type(food_list)
        if type_ is EnumDiscount.moneyOff:
            info = MoneyOff.info_discount()
        elif type_ is EnumDiscount.halfPrice:
            info = HalfPrice.info_discount(food_list)
        else:
            info = ''

        return info

    @classmethod
    def info_final_price(cls, food_list: List[dict]) -> str:
        """
        最终价格信息
        """
        final_price = cls.price_final(food_list)
        info = Config().template_final_price.format(final_price=final_price)
        return info
