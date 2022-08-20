# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import numpy.numpy as np



array1 = np.array([[1,2,3],[2,2,3]])
print(type(array1))
print(array1.shape)

print(array1.ndim)

print(array1, array1.dtype)

array2 = np.array([1,2,'test'])
array3 = np.array([1,2,3.0])
print(array2.dtype, array3.dtype)

array_float = np.array([1.1,2.1,3.1])
array_float2 = array_float.astype('int64')
print(array_float2, array_float2.dtype)

one_array = np.ones((3,2), dtype='int32')
print(one_array, one_array.dtype)

array1 = np.arange(8)
print(array1)
array2 = array1.reshape(2,2,2)
print(array2)
array3 = array2.reshape(-1,1)
print(array3)
array4 = array3.reshape(-1,1)
print(array4)

array1 = np.arange(1,10)
a2 = array1.reshape(3,3)
print(a2[2,2])

print(a2[0])

print(array1[array1>5])

a1 = np.array([[8,12], [7,1]])
print(a1)
print(np.sort(a1, axis=0))
print(np.sort(a1, axis=1))

a1 = np.array([3,1,9,4])
si = np.argsort(a1)[::-1]
print(si)


a = np.array([[1,2,3],[1,4,9]])
b = np.array([[6,3],[4,5],[6,9]])
print(np.dot(a,b))

print(a)
print(np.transpose(a))
