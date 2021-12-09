import numpy as np

if __name__ == "__main__":
    # print(np.__version__)
    # np.show_config()

    # z = np.zeros(10)
    # print(z)

    z = np.zeros((10, 10))  # type: ignore
    print(f"{z.size*z.itemsize}")
