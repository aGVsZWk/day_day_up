import textwrap
from lib.utils import singleton


@singleton
class Config:
    # 满减优惠的订单价格下限
    money_off_floor = 30

    # 满减优惠的价格
    money_off_price = 6

    # 订单明细模板
    template_order_detail = textwrap.dedent("""\
        ============= 订餐明细 =============
        {order_detail_info}
        ===================================
        """)

    # 订单明细中的模块分隔符
    order_detail_separator = '\n-----------------------------------\n'

    # 餐品信息模板
    template_food_info = '{food_name} x {num} = {total_price}元'

    # 最终价格信息模板
    template_final_price = '总计：{final_price}元'

    # 满减优惠信息模板
    template_info_money_off = textwrap.dedent("""\
        使用优惠:
        满{money_off_floor}减{money_off_price}元，省{money_off_price}元""")

    # 半价优惠信息模板
    template_info_half_price = textwrap.dedent("""\
        使用优惠:
        指定菜品半价({food_names})，省{save_total}元""")
