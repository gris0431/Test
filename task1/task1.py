import sys #для работы с консолью

def circular_path(n: int, m: int) -> str:
    path = []
    start = 1
    while True:
        path.append(start)
        end = (start + m - 2) % n + 1 #тут вычисление конца интервала
        if end == 1:
            break
        start = end
    return ''.join(map(str, path)) #склеивание цифр одного массива

def main():
    if len(sys.argv) != 5:
        print("Пример: python task1.py n1 m1 n2 m2")
    else:
        n1, m1, n2, m2 = map(int, sys.argv[1:5])
        result = circular_path(n1, m1) + circular_path(n2, m2) #я так понял просто склеивание двух строк
        print(result)

if __name__ == "__main__":
    main()
