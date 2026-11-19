# 팀 계산기


def add(a, b):
    return a + b


def main():
    print("=== 팀 계산기 ===")
    print("1. 더하기")
    choice = input("번호 선택: ")
    a = float(input("첫 번째 수: "))
    b = float(input("두 번째 수: "))

    if choice == "1":
        print("결과:", add(a, b))
    else:
        print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
