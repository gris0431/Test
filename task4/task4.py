import sys

def min_moves(nums: list) -> int:
    nums.sort()
    n = len(nums)
    median = nums[n // 2] #находим центральный элемент осортированного(а как иначе) массива
    return sum(abs(x - median) for x in nums) #расчёт суммы растояний(по модулю) к медиане для каждого элемента(на медиане не вижу смысла писать пропуск числа т.к. растояние 0)

def main():
    if len(sys.argv) != 2:
        print("Пример: python task4.py nums.txt")
    else:
        with open(sys.argv[1], 'r', encoding='utf-8') as f: #и да тут utf-8
            nums = [int(line.strip()) for line in f if line.strip()]
        if not nums:
            return
        moves = min_moves(nums)
        if moves > 20:
            print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
        else:
            print(moves)

if __name__ == "__main__":
    main()
