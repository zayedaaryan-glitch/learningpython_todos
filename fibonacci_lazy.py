# ==================================================
# Fibonacci Sequence Generator
# ==================================================

def fibonacci_generator():
    """A lazy Fibonacci generator that yields numbers one at a time."""
    a, b = 0, 1
    while True:
        yield a  # Produce current Fibonacci number
        a, b = b, a + b


def main():
    import sys

    print("\nFibonacci Sequence Generator")
    print("=================================\n")

    # Ask user for how many numbers to generate
    try:
        count = int(input("How many Fibonacci numbers do you want? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nGenerating Fibonacci sequence...\n")

    # Create generator instance
    fib_gen = fibonacci_generator()

    # Generate and print numbers one by one
    for i in range(1, count + 1):
        value = next(fib_gen)
        print(f"Fibonacci #{i}: {value}")

    print("\nGeneration complete!\n")

    # -------------------------
    # Memory usage comparison
    # -------------------------
    import tracemalloc
    tracemalloc.start()

    # Generator memory usage
    gen_obj = fibonacci_generator()
    gen_snapshot = tracemalloc.get_traced_memory()[0]

    # List memory usage
    fib_list = []
    a, b = 0, 1
    for _ in range(count):
        fib_list.append(a)
        a, b = b, a + b
    list_snapshot = tracemalloc.get_traced_memory()[0]

    print("Memory Usage Comparison:")
    print("----------------------------")
    print(f"Generator object size: {gen_snapshot} bytes")
    print(f"List storing {count} Fibonacci numbers: {list_snapshot} bytes")

    tracemalloc.stop()


if __name__ == "__main__":
    main()
