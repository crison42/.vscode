import re


def validate_license_plate(license_plate):
    # 正则表达式模式
    pattern_fuel = r"^[京沪津渝鲁冀晋蒙辽吉黑苏浙皖闽赣豫湘鄂粤桂琼川贵云藏陕甘青宁新港澳台][A-HJ-NP-Z][A-HJ-NP-Za-hj-np-z0-9][A-HJ-NP-Za-hj-np-z0-9][A-HJ-NP-Za-hj-np-z0-9][A-HJ-NP-Za-hj-np-z0-9][A-HJ-NP-Za-hj-np-z0-9]$"
    pattern_nev_small = (
        r"^[京沪津渝鲁冀晋蒙辽吉黑苏浙皖闽赣豫湘鄂粤桂琼川贵云藏陕甘青宁新港澳台][A-HJ-NP-Z]([DF]\d{5}|\d{4}[DF])$"
    )
    pattern_nev_large = r"^[京沪津渝鲁冀晋蒙辽吉黑苏浙皖闽赣豫湘鄂粤桂琼川贵云藏陕甘青宁新港澳台][A-HJ-NP-Z]\d{5}[DF]$"

    # 匹配燃油汽车号牌
    if re.match(pattern_fuel, license_plate):
        return str(license_plate + "是燃油车")

    # 匹配新能源小型车号牌
    if re.match(pattern_nev_small, license_plate):
        return str(license_plate + "是小型新能源车")

    # 匹配新能源大型车号牌
    if re.match(pattern_nev_large, license_plate):
        return str(license_plate + "是大型新能源车")

    # 未匹配任何类型
    return str("输入的车牌" + license_plate + "格式是错误的")


license_plate = str(input("请输入车牌号:"))
print(validate_license_plate(license_plate))
