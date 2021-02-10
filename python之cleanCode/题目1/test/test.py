import sys
sys.path.insert(0, '../')

from module.discount.half_price import HalfPrice
from module.discount.money_off import MoneyOff
from module.order_detail import OrderDetail
from lib.utils import log
import textwrap

from main import (
    bestCharge
)


def test_parse_input():
    """
    输出解析测试
    """
    test_items = [
        [['ITEM0001 x 1'], [{'name': '黄焖鸡', 'price_original': 18, 'price_discount': 9, 'num': 1}], ],
        [["ITEM0013 x 4", "ITEM0022 x 1"], [
            {'name': '肉夹馍', 'price_original': 6, 'price_discount': -1, 'num': 4},
            {'name': '凉皮', 'price_original': 8, 'price_discount': 4, 'num': 1},
        ]],
        [["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"], [
            {'name': '黄焖鸡', 'price_original': 18, 'price_discount': 9, 'num': 1},
            {'name': '肉夹馍', 'price_original': 6, 'price_discount': -1, 'num': 2},
            {'name': '凉皮', 'price_original': 8, 'price_discount': 4, 'num': 1},
        ]],
    ]

    for input_, expect in test_items:
        r = OrderDetail.parse_input(input_)
        error = '\nExpect: {}\nResult: {}'.format(expect, r)
        assert r == expect, error

    log('Test pass: parse input')


def test_half_price_count():
    """
    半价测试
    """
    test_items = [
        [['ITEM0001 x 1'], 9],
        [['ITEM0001 x 2'], 18],
        [['ITEM0001 x 1', 'ITEM0013 x 1'], 15],
        [['ITEM0001 x 1', 'ITEM0022 x 1'], 13],
    ]

    for input_, expect in test_items:
        food_list = OrderDetail.parse_input(input_)
        r = HalfPrice.count_price(food_list)
        error = '\nExpect: {}\nResult: {}'.format(expect, r)
        assert r == expect, error

    log('Test pass: half price')


def test_money_off():
    """
    满减价格测试
    """
    test_items = [
        [['ITEM0001 x 1'], 18],
        [['ITEM0001 x 2'], 30],
        [['ITEM0001 x 1', 'ITEM0013 x 1'], 24],
        [['ITEM0001 x 1', 'ITEM0022 x 1'], 26],
        [['ITEM0001 x 1', 'ITEM0022 x 1', 'ITEM0013 x 2'], 32],
    ]

    for input_, expect in test_items:
        food_list = OrderDetail.parse_input(input_)
        r = MoneyOff.count_price(food_list)
        error = '\nExpect: {}\nResult: {}'.format(expect, r)
        assert r == expect, error

    log('Test pass: money off')


def test_best_charge():
    test_items = [
        [["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"], textwrap.dedent("""\
        ============= 订餐明细 =============
        黄焖鸡 x 1 = 18元
        肉夹馍 x 2 = 12元
        凉皮 x 1 = 8元
        -----------------------------------
        使用优惠:
        指定菜品半价(黄焖鸡，凉皮)，省13元
        -----------------------------------
        总计：25元
        ===================================
        """)],

        [["ITEM0013 x 4", "ITEM0022 x 1"], textwrap.dedent("""\
        ============= 订餐明细 =============
        肉夹馍 x 4 = 24元
        凉皮 x 1 = 8元
        -----------------------------------
        使用优惠:
        满30减6元，省6元
        -----------------------------------
        总计：26元
        ===================================
        """)],

        [["ITEM0013 x 4"], textwrap.dedent("""\
        ============= 订餐明细 =============
        肉夹馍 x 4 = 24元
        -----------------------------------
        总计：24元
        ===================================
        """)],
    ]

    for input_, expect in test_items:
        r = bestCharge(input_)
        error = '\nExpect: \n{}\nResult: \n{}'.format(expect, r)
        assert r == expect, error

    log('Test pass: best charge')


if __name__ == '__main__':
    test_parse_input()
    test_half_price_count()
    test_money_off()
    test_best_charge()
