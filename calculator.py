def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main() -> None:
    x = add(5, 10)
    y = divide(10.0, 2.0)

    # ❌ Intentional type error (passing str instead of int)
    z = add("5", "7")  

    print(x, y, z)

if __name__ == "__main__":
    main()
