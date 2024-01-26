def triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return -1
    elif a + b < c or b + c < a or c + a < b:
         return -1
    elif a == b and b == c:
        return 3 # 정삼각형
    elif a == b or b == c or c == a:
        return 2  # 이등변
    else:
        return 1 # normal

