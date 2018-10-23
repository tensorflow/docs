

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.run_test_in_graph_and_eager_modes

``` python
run_test_in_graph_and_eager_modes(
    __unused__=None,
    graph=None,
    config=None,
    use_gpu=False,
    force_gpu=False,
    reset_test=True,
    assert_no_eager_garbage=False
)
```



Defined in [`tensorflow/python/framework/test_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/framework/test_util.py).

Runs the test in both graph and eager modes.

#### Args:

* <b>`__unused__`</b>: Prevents sliently skipping tests.
* <b>`graph`</b>: Optional graph to use during the returned session.
* <b>`config`</b>: An optional config_pb2.ConfigProto to use to configure the
    session.
* <b>`use_gpu`</b>: If True, attempt to run as many ops as possible on GPU.
* <b>`force_gpu`</b>: If True, pin all ops to `/device:GPU:0`.
* <b>`reset_test`</b>: If True, tearDown and SetUp the test case again.
* <b>`assert_no_eager_garbage`</b>: If True, sets DEBUG_SAVEALL on the garbage
    collector and asserts that no extra garbage has been created when running
    the test in eager mode. This will fail if there are reference cycles
    (e.g. a = []; a.append(a)). Off by default because some tests may create
    garbage for legitimate reasons (e.g. they define a class which inherits
    from `object`), and because DEBUG_SAVEALL is sticky in some Python
    interpreters (meaning that tests which rely on objects being collected
    elsewhere in the unit test file will not work). Additionally, checks that
    nothing still has a reference to Tensors that the test allocated.

#### Returns:

Returns a decorator that will run the decorated test function
    using both a graph and using eager execution.