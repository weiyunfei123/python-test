# 作者：Wei
# 时间 2022/3/19 17:37

# 程序准备
import math

# 1.数据输入I
X, Y, Z = eval(input("请输入一点空间直角坐标(X,Y,Z)，格式为X,Y,Z:"))
TQXZ = input("请选择参考椭球，克拉索夫斯基椭球请按1，1975年国际椭球请按2，WGS-84椭球请按3，CGCS2000椭球请按4\n")
if TQXZ == "1" or TQXZ == "2" or TQXZ == "3" or TQXZ == "4":
    if TQXZ == "1":
        print("您选择的是克拉索夫斯基椭球")
        a = 6378245.0000000000  # 克拉索夫斯基椭球下的长半轴
        b = 6356863.0187730473  # 克拉索夫斯基椭球下的短半轴
    elif TQXZ == "2":
        print("您选择的是1975年国际椭球")
        a = 6378140.0000000000  # 1975年国际椭球下的长半轴
        b = 6356755.2881575287  # 1975年国际椭球下的短半轴
    elif TQXZ == "3":
        print("您选择的是WGS-84椭球")
        a = 6378137.0000000000  # WGS - 84椭球下的长半轴
        b = 6356752.3142451795  # WGS - 84椭球下的短半轴
    elif TQXZ == "4":
        print("您选择的是CGCS2000椭球")
        a = 6378137.0000000000  # CGCS2000椭球下的长半轴
        b = 6356752.3141403558  # CGCS2000椭球下的短半轴

    e = math.sqrt((a * a - b * b) / (a * a))  # 椭球偏心率
    # 计算经度L
    L = math.atan2(Y, X)  # 经度，以弧度为单位
    # 利用循环迭代计算纬度B
    tanBn = Z / math.sqrt(X * X + Y * Y)
    tanBn1 = (Z + a * e * e * tanBn / (math.sqrt(1 + (1 - e * e) * tanBn * tanBn))) / math.sqrt(X * X + Y * Y)
    while abs(tanBn1 - tanBn) >= 0.00000000001:
        tanBn = tanBn1
        tanBn1 = (Z + a * e * e * tanBn / (math.sqrt(1 + (1 - e * e) * tanBn * tanBn))) / math.sqrt(X * X + Y * Y)
    B = math.atan(tanBn1)  # 纬度，以弧度为单位
    # 计算大地高H
    N = a / math.sqrt(1 - e * e * math.sin(B) * math.sin(B))  # 卯酉圈曲率半径
    H = math.sqrt(X * X + Y * Y) / math.cos(B) - N
    # 经度L单位由弧度化角度
    L_du = int(L * 180 / math.pi)  # 角度中的°
    L_fen = int((L * 180 / math.pi - L_du) * 60)  # 角度中的′
    L_miao = ((L * 180 / math.pi - L_du) * 60 - L_fen) * 60  # 角度中的″
    # 纬度B单位由弧度化角度
    B_du = int(B * 180 / math.pi)  # 角度中的°
    B_fen = int((B * 180 / math.pi - B_du) * 60)  # 角度中的′
    B_miao = ((B * 180 / math.pi - B_du) * 60 - B_fen) * 60  # 角度中的″
    # 3.数据输出O
    print("转换后的大地坐标B为：{:d}度{:d}分{:.1f}秒".format(B_du, B_fen, B_miao))
    print("转换后的大地坐标L为：{:d}度{:d}分{:.1f}秒".format(L_du, L_fen, L_miao))
    print("转换后的大地坐标H为：{:.3f}m".format(H))
else:
    print("您选择了错误的数字，请重新选择！")