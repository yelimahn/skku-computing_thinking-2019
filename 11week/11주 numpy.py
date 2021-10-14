
>>> import numpy as np
>>> a=np.array([1,2,3,4])
>>> a+2
array([3, 4, 5, 6])
>>> b=np.array([1,0,1,0])
>>> a+b
array([2, 2, 4, 4])
>>> np.cos(a)
array([ 0.54030231, -0.41614684, -0.9899925 , -0.65364362])
>>> stats=np.array([[1,2,3],[4,5,6]])
>>> print(stats)
[[1 2 3]
 [4 5 6]]
>>> np.min(stats)
1
>>> np.max(stats,axis=1)#행
array([3, 6])
>>> np.sum(stats,axis=0)#열
array([5, 7, 9])
