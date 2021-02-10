"""
枚举定义
"""

import enum


class EnumDiscount(enum.Enum):
    """
    优惠类型枚举类
    """
    # 无优惠
    noDiscount = 'noDiscount'

    # 满减优惠
    moneyOff = 'moneyOff'

    # 半价优惠
    halfPrice = 'halfPrice'
