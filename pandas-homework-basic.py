import numpy as np


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


first_ar = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])
pretty_print("First numpy array", first_ar)
pretty_print("Dimensions", first_ar.ndim)
pretty_print("Shape", first_ar.shape)
pretty_print("Size", first_ar.size)
pretty_print("Data Types", first_ar.dtype)

first_mat = np.array([['a', 'b'], ['c', 'd'], [3, 3]])
pretty_print("First numpy matrix", first_mat)
pretty_print("Dimensions", first_mat.ndim)
pretty_print("Shape", first_mat.shape)
pretty_print("Size", first_mat.size)
pretty_print("Data Types", first_mat.dtype)

pretty_print("Array with arange(1, 11)", np.arange(1, 11))
pretty_print("Array with rand(1, 10)", np.random.rand(1, 10))

pretty_print("2-dimension Array with zeros(3, 10)", np.zeros((3, 10)))
pretty_print("Array with rand(2, 10)", np.random.rand(2, 10))

mat_1 = np.ones(20) * 7
pretty_print("Array of 20 sevens", mat_1)
pretty_print("Reshape to 4x5", mat_1.reshape((4, 5)))

mat_2 = np.arange(1, 37).reshape(6, 6)
pretty_print("6x6 matrix", mat_2)
pretty_print("First element in 6x6 matrix", mat_2[0, 0])
pretty_print("Last two rows", mat_2[-2:])
pretty_print("two mid columns and 2 mid rows", mat_2[2:4, 2:4])
for col in range(mat_2.shape[1]):
    pretty_print(f'Sum of column #{col + 1}', mat_2[:, col].sum())
