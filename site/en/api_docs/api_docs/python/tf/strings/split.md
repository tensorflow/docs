

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.split

``` python
tf.strings.split(
    source,
    sep=None,
    maxsplit=-1
)
```



Defined in [`tensorflow/python/ops/string_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/string_ops.py).

Split elements of `source` based on `sep` into a `SparseTensor`.

Let N be the size of source (typically N will be the batch size). Split each
element of `source` based on `sep` and return a `SparseTensor`
containing the split tokens. Empty tokens are ignored.

For example, N = 2, source[0] is 'hello world' and source[1] is 'a b c',
then the output will be

st.indices = [0, 0;
              0, 1;
              1, 0;
              1, 1;
              1, 2]
st.shape = [2, 3]
st.values = ['hello', 'world', 'a', 'b', 'c']

If `sep` is given, consecutive delimiters are not grouped together and are
deemed to delimit empty strings. For example, source of `"1<>2<><>3"` and
sep of `"<>"` returns `["1", "2", "", "3"]`. If `sep` is None or an empty
string, consecutive whitespace are regarded as a single separator, and the
result will contain no empty strings at the startor end if the string has
leading or trailing whitespace.

Note that the above mentioned behavior matches python's str.split.

#### Args:

* <b>`source`</b>: `1-D` string `Tensor`, the strings to split.
* <b>`sep`</b>: `0-D` string `Tensor`, the delimiter character.
* <b>`maxsplit`</b>: An `int`. If `maxsplit > 0`, limit of the split of the result.


#### Raises:

* <b>`ValueError`</b>: If sep is not a string.


#### Returns:

A `SparseTensor` of rank `2`, the strings split according to the delimiter.
The first column of the indices corresponds to the row in `source` and the
second column corresponds to the index of the split component in this row.