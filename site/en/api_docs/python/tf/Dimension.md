page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.Dimension


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L181-L699">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Dimension`

Represents the value of one dimension in a TensorShape.



### Aliases:

* Class <a href="/api_docs/python/tf/Dimension"><code>tf.compat.v1.Dimension</code></a>


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L184-L198">View source</a>

``` python
__init__(value)
```

Creates a new Dimension with the given value.




## Properties

<h3 id="value"><code>value</code></h3>

The value of this dimension, or None if it is unknown.




## Methods

<h3 id="__add__"><code>__add__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L317-L346">View source</a>

``` python
__add__(other)
```

Returns the sum of `self` and `other`.

Dimensions are summed as follows:

```python
tf.compat.v1.Dimension(m)    + tf.compat.v1.Dimension(n)     ==
tf.compat.v1.Dimension(m + n)
tf.compat.v1.Dimension(m)    + tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) + tf.compat.v1.Dimension(n)     # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) + tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
```

#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A Dimension whose value is the sum of `self` and `other`.


<h3 id="__div__"><code>__div__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L494-L508">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L207-L215">View source</a>

``` python
__eq__(other)
```

Returns true if `other` has the same known value as this Dimension.


<h3 id="__floordiv__"><code>__floordiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L448-L477">View source</a>

``` python
__floordiv__(other)
```

Returns the quotient of `self` and `other` rounded down.

Dimensions are divided as follows:

```python
tf.compat.v1.Dimension(m)    // tf.compat.v1.Dimension(n)     ==
tf.compat.v1.Dimension(m // n)
tf.compat.v1.Dimension(m)    // tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) // tf.compat.v1.Dimension(n)     # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) // tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
```

#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A `Dimension` whose value is the integer quotient of `self` and `other`.


<h3 id="__ge__"><code>__ge__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L673-L696">View source</a>

``` python
__ge__(other)
```

Returns True if `self` is known to be greater than or equal to `other`.

Dimensions are compared as follows:

```python
(tf.compat.v1.Dimension(m)    >= tf.compat.v1.Dimension(n))    == (m >= n)
(tf.compat.v1.Dimension(m)    >= tf.compat.v1.Dimension(None)) == None
(tf.compat.v1.Dimension(None) >= tf.compat.v1.Dimension(n))    == None
(tf.compat.v1.Dimension(None) >= tf.compat.v1.Dimension(None)) == None
```

#### Args:


* <b>`other`</b>: Another Dimension.


#### Returns:

The value of `self.value >= other.value` if both are known, otherwise
None.


<h3 id="__gt__"><code>__gt__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L648-L671">View source</a>

``` python
__gt__(other)
```

Returns True if `self` is known to be greater than `other`.

Dimensions are compared as follows:

```python
(tf.compat.v1.Dimension(m)    > tf.compat.v1.Dimension(n))    == (m > n)
(tf.compat.v1.Dimension(m)    > tf.compat.v1.Dimension(None)) == None
(tf.compat.v1.Dimension(None) > tf.compat.v1.Dimension(n))    == None
(tf.compat.v1.Dimension(None) > tf.compat.v1.Dimension(None)) == None
```

#### Args:


* <b>`other`</b>: Another Dimension.


#### Returns:

The value of `self.value > other.value` if both are known, otherwise
None.


<h3 id="__le__"><code>__le__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L623-L646">View source</a>

``` python
__le__(other)
```

Returns True if `self` is known to be less than or equal to `other`.

Dimensions are compared as follows:

```python
(tf.compat.v1.Dimension(m)    <= tf.compat.v1.Dimension(n))    == (m <= n)
(tf.compat.v1.Dimension(m)    <= tf.compat.v1.Dimension(None)) == None
(tf.compat.v1.Dimension(None) <= tf.compat.v1.Dimension(n))    == None
(tf.compat.v1.Dimension(None) <= tf.compat.v1.Dimension(None)) == None
```

#### Args:


* <b>`other`</b>: Another Dimension.


#### Returns:

The value of `self.value <= other.value` if both are known, otherwise
None.


<h3 id="__lt__"><code>__lt__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L598-L621">View source</a>

``` python
__lt__(other)
```

Returns True if `self` is known to be less than `other`.

Dimensions are compared as follows:

```python
(tf.compat.v1.Dimension(m)    < tf.compat.v1.Dimension(n))    == (m < n)
(tf.compat.v1.Dimension(m)    < tf.compat.v1.Dimension(None)) == None
(tf.compat.v1.Dimension(None) < tf.compat.v1.Dimension(n))    == None
(tf.compat.v1.Dimension(None) < tf.compat.v1.Dimension(None)) == None
```

#### Args:


* <b>`other`</b>: Another Dimension.


#### Returns:

The value of `self.value < other.value` if both are known, otherwise
None.


<h3 id="__mod__"><code>__mod__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L558-L584">View source</a>

``` python
__mod__(other)
```

Returns `self` modulo `other`.

Dimension moduli are computed as follows:

```python
tf.compat.v1.Dimension(m)    % tf.compat.v1.Dimension(n)     ==
tf.compat.v1.Dimension(m % n)
tf.compat.v1.Dimension(m)    % tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) % tf.compat.v1.Dimension(n)     # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) % tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
```

#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A Dimension whose value is `self` modulo `other`.


<h3 id="__mul__"><code>__mul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L405-L435">View source</a>

``` python
__mul__(other)
```

Returns the product of `self` and `other`.

Dimensions are summed as follows:

```python
tf.compat.v1.Dimension(m)    * tf.compat.v1.Dimension(n)     ==
tf.compat.v1.Dimension(m * n)
tf.compat.v1.Dimension(m)    * tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) * tf.compat.v1.Dimension(n)     # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) * tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
```

#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A Dimension whose value is the product of `self` and `other`.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L217-L225">View source</a>

``` python
__ne__(other)
```

Returns true if `other` has a different known value from `self`.


<h3 id="__radd__"><code>__radd__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L348-L357">View source</a>

``` python
__radd__(other)
```

Returns the sum of `other` and `self`.


#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A Dimension whose value is the sum of `self` and `other`.


<h3 id="__rdiv__"><code>__rdiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L510-L524">View source</a>

``` python
__rdiv__(other)
```

Use `__floordiv__` via `x // y` instead.

This function exists only to have a better error message. Instead of:
`TypeError: unsupported operand type(s) for /: 'int' and 'Dimension'`,
this function will explicitly call for usage of `//` instead.

#### Args:


* <b>`other`</b>: Another `Dimension`.


#### Raises:

TypeError.


<h3 id="__rfloordiv__"><code>__rfloordiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L479-L492">View source</a>

``` python
__rfloordiv__(other)
```

Returns the quotient of `other` and `self` rounded down.


#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A `Dimension` whose value is the integer quotient of `self` and `other`.


<h3 id="__rmod__"><code>__rmod__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L586-L596">View source</a>

``` python
__rmod__(other)
```

Returns `other` modulo `self`.


#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A Dimension whose value is `other` modulo `self`.


<h3 id="__rmul__"><code>__rmul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L437-L446">View source</a>

``` python
__rmul__(other)
```

Returns the product of `self` and `other`.


#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A Dimension whose value is the product of `self` and `other`.


<h3 id="__rsub__"><code>__rsub__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L390-L403">View source</a>

``` python
__rsub__(other)
```

Returns the subtraction of `self` from `other`.


#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A Dimension whose value is the subtraction of `self` from `other`.


<h3 id="__rtruediv__"><code>__rtruediv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L542-L556">View source</a>

``` python
__rtruediv__(other)
```

Use `__floordiv__` via `x // y` instead.

This function exists only to have a better error message. Instead of:
`TypeError: unsupported operand type(s) for /: 'int' and 'Dimension'`,
this function will explicitly call for usage of `//` instead.

#### Args:


* <b>`other`</b>: Another `Dimension`.


#### Raises:

TypeError.


<h3 id="__sub__"><code>__sub__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L359-L388">View source</a>

``` python
__sub__(other)
```

Returns the subtraction of `other` from `self`.

Dimensions are subtracted as follows:

```python
tf.compat.v1.Dimension(m)    - tf.compat.v1.Dimension(n)     ==
tf.compat.v1.Dimension(m - n)
tf.compat.v1.Dimension(m)    - tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) - tf.compat.v1.Dimension(n)     # equiv. to
tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None) - tf.compat.v1.Dimension(None)  # equiv. to
tf.compat.v1.Dimension(None)
```

#### Args:


* <b>`other`</b>: Another Dimension, or a value accepted by `as_dimension`.


#### Returns:

A Dimension whose value is the subtraction of `other` from `self`.


<h3 id="__truediv__"><code>__truediv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L526-L540">View source</a>

``` python
__truediv__(other)
```

Use `__floordiv__` via `x // y` instead.

This function exists only to have a better error message. Instead of:
`TypeError: unsupported operand type(s) for /: 'Dimension' and 'int'`,
this function will explicitly call for usage of `//` instead.

#### Args:


* <b>`other`</b>: Another `Dimension`.


#### Raises:

TypeError.


<h3 id="assert_is_compatible_with"><code>assert_is_compatible_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L263-L275">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L244-L261">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L277-L315">View source</a>

``` python
merge_with(other)
```

Returns a Dimension that combines the information in `self` and `other`.

Dimensions are combined as follows:

```python
tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(n))     ==
tf.compat.v1.Dimension(n)
tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(None))  ==
tf.compat.v1.Dimension(n)
tf.compat.v1.Dimension(None).merge_with(tf.compat.v1.Dimension(n))     ==
tf.compat.v1.Dimension(n)
# equivalent to tf.compat.v1.Dimension(None)
tf.compat.v1.Dimension(None).merge_with(tf.compat.v1.Dimension(None))

# raises ValueError for n != m
tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(m))
```

#### Args:


* <b>`other`</b>: Another Dimension.


#### Returns:

A Dimension containing the combined information of `self` and
`other`.



#### Raises:


* <b>`ValueError`</b>: If `self` and `other` are not compatible (see
  is_compatible_with).
