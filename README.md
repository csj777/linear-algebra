## Vector for Linear Algebra
实现线性代数中的向量（Vector）  
数据结构练习及线性代数复习  
Python实现  
为了简化代码，底层使用list

----
### 项目结构：
- LA包
   - __init\__.py：包初始化  
   - Vector.py：包实现
- main_vector.py：测试代码
----
## 目录
- [实现基本内建方法](#实现基本内建方法)  
- [实现向量基本运算](#实现向量基本运算)
----
### 实现基本内建方法
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
> ```
> (3, 4) · (3, 7) = 37  
> (3, 4) · (3, 7) = 37

