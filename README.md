## Linear Algebra

搭建个人线性代数库  
数据结构练习及线性代数复习  
Python实现  
为了简化代码，底层使用list  

liuyubobobo 课程

----
## 目录
<!-- TOC -->

- [Linear Algebra](#linear-algebra)
- [目录](#目录)
- [项目结构](#项目结构)
- [向量类实现](#向量类实现)
  - [实现向量基本内建方法](#实现向量基本内建方法)
  - [实现向量基本运算](#实现向量基本运算)
- [矩阵类实现](#矩阵类实现)
  - [矩阵基本方法实现](#矩阵基本方法实现)
  - [矩阵应用](#矩阵应用)
- [线性系统](#线性系统)

<!-- /TOC -->
----
## 项目结构
- LA
  - __init\__.py
  - _global.py
  - Vector.py
  - Matrix.py
  - LinearSystem.py
- main_vector.py
- main_matrix.py
- main_matrix_transformation.py
- main_linearsystem.py

----
## 向量类实现
### 实现向量基本内建方法
- #### 实现 __repr__输出：
    
    > \>>> vec   
    > \>>> Vector([5,2])
- #### 实现 __str__输出：
    ```Python
    print(vec)
    (5,2)
    ```
- #### 实现 __len__方法：
    ```Python
    len(vec)
    ```
- #### 实现 __getitem__方法：
    ```Python
    vec[0]
    ```
----
### 实现向量基本运算
- #### 向量加法
> ```Python
> print("{} + {} = {}".format(vec, vec2, vec + vec2))  
> ```
> (5, 2) + (3, 1) = (8, 3)
- #### 向量减法
> ```Python
> print("{} - {} = {}".format(vec, vec2, vec - vec2))  
> ```
> (5, 2) - (3, 1) = (2, 1)
- #### 向量数乘(左乘，右乘)
> ```Python
> print("{} * {} = {}".format(vec, 2, vec * 2))  
> print("{} * {} = {}".format(2, vec, 2 * vec))  
> ```
> (5, 2) * 3 = (15, 6)   
> 3 * (5, 2) = (15, 6)
- #### 向量取正、负
> ```Python
> print("+{} = {}".format(vec, +vec))  
> print("-{} = {}".format(vec, -vec))  
> ```
> +(5, 2) = (5, 2)   
> -(5, 2) = (-5, -2)
- #### 实现零向量
> ```Python
> zero2 = Vector.zero(2)  
> print(zero2)  
> ```
> (0, 0)
- #### 向量规范化
> ```Python
> vec = Vector([30, 40])
> print("norm({}) = {}".format(vec, vec.norm()))  
> print("normalize {} is {}".format(vec, vec.normalize()))  
> print(vec.normalize().norm())  
> ```
> norm((30, 40)) = 50.0  
> normalize (30, 40) is (0.6, 0.8)  
> 1.0
- #### 向量数量除法
> ```Python
> print("{} / {} = {}".format(vec, 2, vec / 2))   
> ```
> (30, 40) / 2 = (15.0, 20.0)
- #### 向量点乘
> ```Python
> print("{} · {} = {}".format(vec, vec2, vec.dot(vec2)))  
> print("{} * {} = {}".format(vec, vec2, vec * vec2))  
> print("{} * {} = {}".format(vec, [2.5], vec * [2.5]))
> ```
> (3, 4) · (3, 7) = 37  
> (3, 4) · (3, 7) = 37  
> (3, 4) * [2.5] = (7.5, 10.0)

----
## 矩阵类实现
### 矩阵基本方法实现
- #### 初始化
```Python
matrix = Matrix([[1, 2], [3, 4]])
```
- #### 初始化
```Python
print(matrix)
```
- #### 矩阵形状
```Python
print(matrix.shape())
```
- #### 矩阵长度
```Python
print(matrix.shape())
```
- #### 选取矩阵行、列向量
```Python
print(matrix.row_vector(0))
print(matrix.col_vector(0))
```
- #### 矩阵加法
```Python
print(print(matrix + matrix2))
```
- #### 矩阵减法
```Python
print(print(matrix - matrix2))
```
- #### 矩阵左右数量乘法
```Python
print(matrix * 2)
print(2 * matrix)
```
- #### 矩阵数量除法
```Python
print(matrix / 2)
```
- #### 零矩阵
```Python
print(Matrix.zero(3, 7))
```
- #### 矩阵乘法
```Python
T = Matrix([[1.5, 0], [0, 2]])
p = Vector([5, 3])
P = Matrix([[0, 4, 5], [0, 0, 3]])
print(T.dot(p))
print(T.dot(P))
```
- #### 矩阵转置
```Python
print(P.T())
```
----
### 矩阵应用
- #### 矩阵缩放
- #### 矩阵剪切
- #### 矩阵旋转
- #### 单位矩阵
> ```Python
> print(Matrix.identity(2))
> ```
## 线性系统
- #### 高斯消元法
```Python
ls = LinearSystem(A, b)
if not ls.gauss_jordan_elimination():
    print("No Solution!")
ls.fancy_print()
```
- #### 矩阵逆
```Python
invA = inv(A)
```
- #### 矩阵LU分解
```Python
L, U = LU(A)
```
- #### 矩阵秩
```Python
rank(A)
```
