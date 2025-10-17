

---

### 1. Definition

**Python List**

* Built-in data structure.
* Can store different data types.
* Flexible but slower for numeric tasks.

**NumPy Array**

* Comes from the NumPy library.
* Stores only one data type (homogeneous).
* Built for fast mathematical and vector operations.

---

### 2. Syntax

Python List:

```python
py_list = [1, 2, 3, 4, 5]
```

NumPy Array:

```python
import numpy as np
np_array = np.array([1, 2, 3, 4, 5])
```

---

### 3. Key Differences

| Feature         | Python List                   | NumPy Array                      |
| --------------- | ----------------------------- | -------------------------------- |
| Data Type       | Mixed types allowed           | Single data type only            |
| Speed           | Slower                        | Much faster                      |
| Memory Usage    | Uses more memory              | Uses less memory                 |
| Math Operations | Requires loops                | Vectorized (no loops needed)     |
| Dimensions      | 1D only                       | Supports multi-dimensional       |
| Performance     | Not optimized for computation | Optimized with C/Fortran backend |

---

### 4. Why Prefer NumPy?

1. **Speed**

```python
# List
result = [x + 5 for x in py_list]

# NumPy
result = np_array + 5
```

2. **Memory Efficiency**

```python
import sys
print(sys.getsizeof(py_list))   # More memory
print(np_array.nbytes)          # Less memory
```

3. **Math without loops**
4. **Supports multi-dimensional arrays**

Example:

```python
matrix = np.array([[1, 2], [3, 4]])
```

---

### 5. Example Comparison

Using List:

```python
py_list = [1, 2, 3, 4]
new_list = [x * 2 for x in py_list]
print(new_list)  # [2, 4, 6, 8]
```

Using NumPy:

```python
np_array = np.array([1, 2, 3, 4])
new_array = np_array * 2
print(new_array)  # [2 4 6 8]
```

---

### 6. When to Use?

**Use Python List when:**

* Data types are mixed
* No heavy calculations
* Small/general tasks

**Use NumPy when:**

* Numerical/data science tasks
* Matrix or multidimensional data
* Fast performance needed
* ML or data analysis work

---

### 7. Interview Summary

A **Python list** is a general-purpose container that can store mixed data but is slower and uses more memory.
A **NumPy array** is homogeneous, much faster, memory-efficient, and optimized for mathematical and multi-dimensional operations using vectorization.

Let me know if you want this in PDF, Word, or text file format!
