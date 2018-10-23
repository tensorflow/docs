

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.IsolateTest

## Class `IsolateTest`





Defined in [`tensorflow/python/framework/test_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/framework/test_util.py).

A context manager which isolates resources in its block.

Provides an Eager-agnostic abstraction for preventing the sharing of
variables and other resources.

In graph mode, resource handle ops are only executed in a particular Session,
isolating them from resources with the same name in other Graphs. In Eager,
separate Sessions do not exist, so resources (particularly ResourceVariables)
would be shared implicitly if a resource of the same name were created
anywhere in a Python process. Multiple handles to the same resource would
cause several issues, and so this type of sharing will raise an exception.

Using resources with the same name in a single Python process may be useful
(especially for unit tests), so this context manager provides an abstraction
for isolating resources. Using a resource created in one Isolation environment
in another is an error.

Example usage in Eager mode:

```python
import tensorflow as tf
# Import subject to change
from tensorflow.contrib.eager.python import tfe

tfe.enable_eager_execution()

for hyperparameter in [1, 2, 3]:
  with tfe.IsolateTest():
    v = tfe.Variable(name="v", initial_value=hyperparameter)
    # train model, test results ...
```

IsolateTest is currently exposed through contrib.eager, but it creates a new
default Graph and provides equivalent safety in graph mode.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__()
```



<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```



<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    type_arg,
    value_arg,
    traceback_arg
)
```





