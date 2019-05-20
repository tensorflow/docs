# TensorFlow code style guide

## Python style

Follow the [PEP 8 Python style
guide](https://www.python.org/dev/peps/pep-0008/), except TensorFlow uses 2
spaces instead of 4. Please conform to the
[Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md),
and use [pylint](https://www.pylint.org/) to check your Python changes.


### pylint

To install `pylint` and retrieve TensorFlow's custom style definition:

```bash

$ pip install pylint
$ wget -O /tmp/pylintrc https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/tools/ci_build/pylintrc

```

To check a file with `pylint`:

```bash
$ pylint --rcfile=/tmp/pylintrc myfile.py
```

### Supported Python versions

TensorFlow supports Python 2.7 and Python >= 3.4. See the
[installation guide](https://www.tensorflow.org/install) for details.

See the TensorFlow
[continuous build status](https://github.com/tensorflow/tensorflow/blob/master/README.md#continuous-build-status)
for official and community supported builds.

#### Legacy Python compatibility

TensorFlow will support Legacy Python (Python 2.7) until
[January 1, 2020](https://groups.google.com/a/tensorflow.org/forum/#!searchin/announce/python$202.7%7Csort:date/announce/gVwS5RC8mds/dCt1ka2XAAAJ).
Until that time, all code will need to be compatible with the Python versions
listed above.

These lines should be present in every Python file:


```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
```

Use `six` to write compatible code (for example, `six.moves.range`).


## C++ coding style

Changes to TensorFlow C++ code should conform to the [Google C++ Style
Guide](https://google.github.io/styleguide/cppguide.html). Use `clang-tidy` to
check your C/C++ changes.

To install `clang-tidy` on Ubuntu 16+, do:


```bash
$ apt-get install -y clang-tidy
```

You can check a C/C++ file by using the following:

```bash
$ clang-format <my_cc_file> --style=google > /tmp/my_cc_file.cc
$ diff <my_cc_file> /tmp/my_cc_file.cc
```

## Other languages

*   [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
*   [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
*   [Google Shell Style Guide](https://google.github.io/styleguide/shell.xml)
*   [Google Objective-C Style Guide](https://google.github.io/styleguide/objcguide.html)




## TensorFlow conventions and special uses

### Tensors

*   Operations that deal with batches may assume that the **first dimension** of
    a Tensor is the batch dimension.
*   In most models, the **last dimension** is the number of _channels_.
*   Dimensions excluding the first and last usually make up the _space_
    dimensions: sequence-length, or image-size.
*   When possible, use a Tensor's overloaded operators rather than TensorFlow
    functions. For example, we prefer `**`, `+`, `/`, `*`, `-`, `and/or` over
    `tf.pow`, `tf.add`, `tf.divide`, `tf.multiply`, `tf.subtract`, and `tf.logical_*` —
    unless a specific name for the operation is desired.


### Python operations

A _Python operation_ is a function that, given input tensors and parameters,
creates a part of the graph and returns output tensors.

*   The first argument should be tensors, followed by basic Python parameters.
    The last argument is `name` with a default value of `None`.
*   Tensor arguments should be either a single tensor or an iterable of tensors. That is, a "Tensor or list of Tensors" is too broad. See `assert_proper_iterable`.
*   Operations that take tensors as arguments should call `convert_to_tensor` to
    convert non-tensor inputs into tensors if they are using C++ operations.
    Note that the arguments are still described as a `Tensor` object of a
    specific dtype in the documentation.
*   Each Python operation should have a `name_scope`. As seen below, pass the name
    of the op as a string.
*   Operations should contain an extensive Python comment with Args and Returns
    declarations that explain both the type and meaning of each value. Possible
    shapes, dtypes, or ranks should be specified in the description. See
    documentation details.
*   For increased usability, include an example of usage with inputs / outputs
    of the op in Example section.
*   Avoid making explicit use of `tf.Tensor.eval` or `tf.Session.run`. For
    example, to write logic that depends on the Tensor value, use the TensorFlow
    control flow. Alternatively, restrict the operation to only run when eager
    execution is enabled (`tf.executing_eagerly()`).

Example:


```python
def my_op(tensor_in, other_tensor_in, my_param, other_param=0.5,
          output_collections=(), name=None):
  """My operation that adds two tensors with given coefficients.

  Args:
    tensor_in: `Tensor`, input tensor.
    other_tensor_in: `Tensor`, same shape as `tensor_in`, other input tensor.
    my_param: `float`, coefficient for `tensor_in`.
    other_param: `float`, coefficient for `other_tensor_in`.
    output_collections: `tuple` of `string`s, name of the collection to
                        collect result of this op.
    name: `string`, name of the operation.

  Returns:
    `Tensor` of same shape as `tensor_in`, sum of input values with coefficients.

  Example:
    >>> my_op([1., 2.], [3., 4.], my_param=0.5, other_param=0.6,
              output_collections=['MY_OPS'], name='add_t1t2')
    [2.3, 3.4]
  """
  with tf.name_scope(name or "my_op"):
    tensor_in = tf.convert_to_tensor(tensor_in)
    other_tensor_in = tf.convert_to_tensor(other_tensor_in)
    result = my_param * tensor_in + other_param * other_tensor_in
    tf.add_to_collection(output_collections, result)
    return result
```

Usage:

```python
output = my_op(t1, t2, my_param=0.5, other_param=0.6,
               output_collections=['MY_OPS'], name='add_t1t2')
```
