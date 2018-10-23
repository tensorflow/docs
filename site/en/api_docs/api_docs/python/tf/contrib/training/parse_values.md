

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.training.parse_values

``` python
parse_values(
    values,
    type_map
)
```



Defined in [`tensorflow/contrib/training/python/training/hparam.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/training/python/training/hparam.py).

Parses hyperparameter values from a string into a python map..

`values` is a string containing comma-separated `name=value` pairs.
For each pair, the value of the hyperparameter named `name` is set to
`value`.

If a hyperparameter name appears multiple times in `values`, the last
value is used.

The `value` in `name=value` must follows the syntax according to the
type of the parameter:

*  Scalar integer: A Python-parsable integer point value.  E.g.: 1,
   100, -12.
*  Scalar float: A Python-parsable floating point value.  E.g.: 1.0,
   -.54e89.
*  Boolean: Either true or false.
*  Scalar string: A non-empty sequence of characters, excluding comma,
   spaces, and square brackets.  E.g.: foo, bar_1.
*  List: A comma separated list of scalar values of the parameter type
   enclosed in square backets.  E.g.: [1,2,3], [1.0,1e-12], [high,low].

#### Args:

* <b>`values`</b>: String.  Comma separated list of `name=value` pairs where
    'value' must follow the syntax described above.
* <b>`type_map`</b>: A dictionary mapping hyperparameter names to types.  Note every
    parameter name in values must be a key in type_map.  The values must
    conform to the types indicated, where a value V is said to conform to a
    type T if either V has type T, or V is a list of elements of type T.
    Hence, for a multidimensional parameter 'x' taking float values,
    'x=[0.1,0.2]' will parse successfully if type_map['x'] = float.


#### Returns:

  A python map containing the name, value pairs.


#### Raises:

* <b>`ValueError`</b>: If `values` cannot be parsed.