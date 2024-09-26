import numpy as np

arr1d = np.array([
    1,2,3,4
])

arr2d = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

arr3d = np.array([
    [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6]
    ],

    [
        [4,5,6,7],
        [5,6,7,8],
        [6,7,8,9]
    ]
])
#
# # Total number of elements in array
# print(arr2d.size)
#
# # Dimensions of array :
# # 1D : (Items,)
# # 2D : (Rows, Items)
# # 3D : (Group, Rows, Items)
# print(arr1d.shape)
# print(arr2d.shape)
# print(arr3d.shape)

# print(type(arr1d))
# numpy.ndarray

# print(arr1d.dtype)
# int64 (data type)


# newarr = np.arange(5,21,3)
# print(newarr)

# arr = np.array(["Diljeet Dosanjh", "Karan Aujla"])
# print(arr.dtype)


# zeros = np.zeros(arr2d.shape,dtype=np.int64)
# print(zeros)
# ones = np.ones(shape, dtype=np.int32)
# shape = (2,4)
# full = np.full(shape, "item")
# print(full)
# ol = np.ones_like(arr2d)
# print(ol)

identity_matrix = np.eye(5)
print(identity_matrix)
print(identity_matrix[[1,2,identity_matrix.size-1 ]])