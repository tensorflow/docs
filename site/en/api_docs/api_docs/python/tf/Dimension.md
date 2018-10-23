

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.Dimension

## Class `Dimension`





Defined in [`tensorflow/python/framework/tensor_shape.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/framework/tensor_shape.py).

See the guide: [Building Graphs > Defining new operations](../../../api_guides/python/framework#Defining_new_operations)

Represents the value of one dimension in a TensorShape.

## Properties

<h3 id="value"><code>value</code></h3>

The value of this dimension, or None if it is unknown.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(value)
```

Creates a new Dimension with the given value.

<h3 id="__add__"><code>__add__</code></h3>

``` python
__add__(other)
```

Returns the sum of `self` and `other`.

Dimensions are summed as follows:

```python
tf.Dimension(m)    + tf.Dimension(n)    == tf.Dimension(m + n)
tf.Dimension(m)    + tf.Dimension(None) == tf.Dimension(None)
tf.Dimension(None) + tf.Dimension(n)    == tf.Dimension(None)
tf.Dimension(None) + tf.Dimension(None) == tf.Dimension(None)
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

A Dimension whose value is the sum of `self` and `other`.

<h3 id="__div__"><code>__div__</code></h3>

``` python
__div__(other)
```

DEPRECATED: Use `__floordiv__` via `x // y` instead.

This function exists only for backwards compatibility purposes; new code
should use `__floordiv__` via the syntax `x // y`.  Using `x // y`
communicates clearly that the result rounds down, and is forward compatible
to Python 3.

#### Args:

* <b>`other`</b>: Another `Dimension`.


#### Returns:

A `Dimension` whose value is the integer quotient of `self` and `other`.

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```

Returns true if `other` has the same known value as this Dimension.

<h3 id="__floordiv__"><code>__floordiv__</code></h3>

``` python
__floordiv__(other)
```

Returns the quotient of `self` and `other` rounded down.

Dimensions are divided as follows:

```python
tf.Dimension(m)    // tf.Dimension(n)    == tf.Dimension(m // n)
tf.Dimension(m)    // tf.Dimension(None) == tf.Dimension(None)
tf.Dimension(None) // tf.Dimension(n)    == tf.Dimension(None)
tf.Dimension(None) // tf.Dimension(None) == tf.Dimension(None)
```

#### Args:

* <b>`other`</b>: Another `Dimension`.


#### Returns:

A `Dimension` whose value is the integer quotient of `self` and `other`.

<h3 id="__ge__"><code>__ge__</code></h3>

``` python
__ge__(other)
```

Returns True if `self` is known to be greater than or equal to `other`.

Dimensions are compared as follows:

```python
(tf.Dimension(m)    >= tf.Dimension(n))    == (m >= n)
(tf.Dimension(m)    >= tf.Dimension(None)) == None
(tf.Dimension(None) >= tf.Dimension(n))    == None
(tf.Dimension(None) >= tf.Dimension(None)) == None
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

The value of `self.value >= other.value` if both are known, otherwise
None.

<h3 id="__gt__"><code>__gt__</code></h3>

``` python
__gt__(other)
```

Returns True if `self` is known to be greater than `other`.

Dimensions are compared as follows:

```python
(tf.Dimension(m)    > tf.Dimension(n))    == (m > n)
(tf.Dimension(m)    > tf.Dimension(None)) == None
(tf.Dimension(None) > tf.Dimension(n))    == None
(tf.Dimension(None) > tf.Dimension(None)) == None
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

The value of `self.value > other.value` if both are known, otherwise
None.

<h3 id="__index__"><code>__index__</code></h3>

``` python
__index__()
```



<h3 id="__int__"><code>__int__</code></h3>

``` python
__int__()
```



<h3 id="__le__"><code>__le__</code></h3>

``` python
__le__(other)
```

Returns True if `self` is known to be less than or equal to `other`.

Dimensions are compared as follows:

```python
(tf.Dimension(m)    <= tf.Dimension(n))    == (m <= n)
(tf.Dimension(m)    <= tf.Dimension(None)) == None
(tf.Dimension(None) <= tf.Dimension(n))    == None
(tf.Dimension(None) <= tf.Dimension(None)) == None
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

The value of `self.value <= other.value` if both are known, otherwise
None.

<h3 id="__long__"><code>__long__</code></h3>

``` python
__long__()
```



<h3 id="__lt__"><code>__lt__</code></h3>

``` python
__lt__(other)
```

Returns True if `self` is known to be less than `other`.

Dimensions are compared as follows:

```python
(tf.Dimension(m)    < tf.Dimension(n))    == (m < n)
(tf.Dimension(m)    < tf.Dimension(None)) == None
(tf.Dimension(None) < tf.Dimension(n))    == None
(tf.Dimension(None) < tf.Dimension(None)) == None
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

The value of `self.value < other.value` if both are known, otherwise
None.

<h3 id="__mod__"><code>__mod__</code></h3>

``` python
__mod__(other)
```

Returns `self` modulo `other.

Dimension moduli are computed as follows:

```python
tf.Dimension(m)    % tf.Dimension(n)    == tf.Dimension(m % n)
tf.Dimension(m)    % tf.Dimension(None) == tf.Dimension(None)
tf.Dimension(None) % tf.Dimension(n)    == tf.Dimension(None)
tf.Dimension(None) % tf.Dimension(None) == tf.Dimension(None)
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

A Dimension whose value is `self` modulo `other`.

<h3 id="__mul__"><code>__mul__</code></h3>

``` python
__mul__(other)
```

Returns the product of `self` and `other`.

Dimensions are summed as follows:

```python
tf.Dimension(m)    * tf.Dimension(n)    == tf.Dimension(m * n)
tf.Dimension(m)    * tf.Dimension(None) == tf.Dimension(None)
tf.Dimension(None) * tf.Dimension(n)    == tf.Dimension(None)
tf.Dimension(None) * tf.Dimension(None) == tf.Dimension(None)
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

A Dimension whose value is the product of `self` and `other`.

<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```

Returns true if `other` has a different known value from `self`.

<h3 id="__sub__"><code>__sub__</code></h3>

``` python
__sub__(other)
```

Returns the subtraction of `other` from `self`.

Dimensions are subtracted as follows:

```python
tf.Dimension(m)    - tf.Dimension(n)    == tf.Dimension(m - n)
tf.Dimension(m)    - tf.Dimension(None) == tf.Dimension(None)
tf.Dimension(None) - tf.Dimension(n)    == tf.Dimension(None)
tf.Dimension(None) - tf.Dimension(None) == tf.Dimension(None)
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

A Dimension whose value is the subtraction of sum of `other` from `self`.

<h3 id="assert_is_compatible_with"><code>assert_is_compatible_with</code></h3>

``` python
assert_is_compatible_with(other)
```

Raises an exception if `other` is not compatible with this Dimension.

#### Args:

* <b>`other`</b>: Another Dimension.


#### Raises:

* <b>`ValueError`</b>: If `self` and `other` are not compatible (see
    is_compatible_with).

<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

``` python
is_compatible_with(other)
```

Returns true if `other` is compatible with this Dimension.

Two known Dimensions are compatible if they have the same value.
An unknown Dimension is compatible with all other Dimensions.

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

True if this Dimension and `other` are compatible.

<h3 id="merge_with"><code>merge_with</code></h3>

``` python
merge_with(other)
```

Returns a Dimension that combines the information in `self` and `other`.

Dimensions are combined as follows:

```python
tf.Dimension(n)   .merge_with(tf.Dimension(n))    == tf.Dimension(n)
tf.Dimension(n)   .merge_with(tf.Dimension(None)) == tf.Dimension(n)
tf.Dimension(None).merge_with(tf.Dimension(n))    == tf.Dimension(n)
tf.Dimension(None).merge_with(tf.Dimension(None)) == tf.Dimension(None)
tf.Dimension(n)   .merge_with(tf.Dimension(m))  # raises ValueError for n != m
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

A Dimension containing the combined information of `self` and
`other`.


#### Raises:

* <b>`ValueError`</b>: If `self` and `other` are not compatible (see
    is_compatible_with).



