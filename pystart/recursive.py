import os


def recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n > 0")
    elif n == 0:
        return 1
    else:
        return n * recursive(n - 1)


def disk_usage(path: str) -> float:
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            child_path = os.path.join(path, file_name)
            total += disk_usage(child_path)

    print(f"{total}: {path}")
    return total


if __name__ == "__main__":
    # print(recursive(2))

    disk_usage("/Users/linzhenhao/Documents")
