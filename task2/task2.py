import sys

def read_ellipse(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f: #и да тут utf-8
        lines = [line.strip() for line in f if line.strip()]
    cen = list(map(float, lines[0].split()))
    rad = list(map(float, lines[1].split()))
    return cen[0], cen[1], rad[0], rad[1]

def point_position(cx, cy, rx, ry, x, y) -> int:
    if rx == 0 or ry == 0:
        if rx == 0 and ry == 0:
            return 0 if x == cx and y == cy else 2
    val = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 #Уравнение эллипса: ((x-cx)/rx)^2 + ((y-cy)/ry)^2 = 1
    if abs(val - 1) < 1e-12: #тут по идее должно быть val == 1(по крайней мере если числа целые), но в тз указано что числа рациональные(то бишь с плавающей точкой(float))
                             #поэтому танцы с бубном
        return 0 #на
    elif val < 1.0:
        return 1 #d
    else:
        return 2 #cнаружи

def main():
    if len(sys.argv) != 3:
        print("Примре: python task2.py ellipse.txt points.txt")
    else:
        cx, cy, rx, ry = read_ellipse(sys.argv[1])
        with open(sys.argv[2], 'r', encoding='utf-8') as f: #и да тут utf-8
            for line in f:
                line = line.strip()
                if not line:
                    continue
                x, y = map(float, line.split())
                print(point_position(cx, cy, rx, ry, x, y))

if __name__ == "__main__":
    main()
