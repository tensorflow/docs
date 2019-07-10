page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.run_test_in_graph_and_eager_modes

Execute the decorated test with and without enabling eager execution.

``` python
tf.contrib.eager.run_test_in_graph_and_eager_modes(
    func=None,
    config=None,
    use_gpu=True,
    reset_test=True,
    assert_no_eager_garbage=False
)
```



Defined in [`python/framework/test_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/test_util.py).

<!-- Placeholder for "Used in" -->

This function returns a decorator intended to be applied to test methods in
a <a href="../../../tf/test/TestCase"><code>tf.test.TestCase</code></a> class. Doing so will cause the contents of the test
method to be executed twice - once normally, and once with eager execution
enabled. This allows unittests to confirm the equivalence between eager
and graph execution (see <a href="../../../tf/enable_eager_execution"><code>tf.compat.v1.enable_eager_execution</code></a>).

For example, consider the following unittest:

```python
class MyTests(tf.test.TestCase):

  @run_in_graph_and_eager_modes
  def test_foo(self):
    x = tf.constant([1, 2])
    y = tf.constant([3, 4])
    z = tf.add(x, y)
    self.assertAllEqual([4, 6], self.evaluate(z))

if __name__ == "__main__":
  tf.test.main()
```

This test validates that <a href="../../../tf/math/add"><code>tf.add()</code></a> has the same behavior when computed with
eager execution enabled as it does when constructing a TensorFlow graph and
executing the `z` tensor in a session.

`deprecated_graph_mode_only`, `run_v1_only`, `run_v2_only`, and
`run_in_graph_and_eager_modes` are available decorators for different
v1/v2/eager/graph combinations.


#### Args:


* <b>`func`</b>: function to be annotated. If `func` is None, this method returns a
  decorator the can be applied to a function. If `func` is not None this
  returns the decorator applied to `func`.
* <b>`config`</b>: An optional config_pb2.ConfigProto to use to configure the session
  when executing graphs.
* <b>`use_gpu`</b>: If True, attempt to run as many operations as possible on GPU.
* <b>`reset_test`</b>: If True, tearDown and SetUp the test case between the two
  executions of the test (once with and once without eager execution).
* <b>`assert_no_eager_garbage`</b>: If True, sets DEBUG_SAVEALL on the garbage
  collector and asserts that no extra garbage has been created when running
  the test with eager execution enabled. This will fail if there are
  reference cycles (e.g. a = []; a.append(a)). Off by default because some
  tests may create garbage for legitimate reasons (e.g. they define a class
  which inherits from `object`), and because DEBUG_SAVEALL is sticky in some
  Python interpreters (meaning that tests which rely on objects being
  collected elsewhere in the unit test file will not work). Additionally,
  checks that nothing still has a reference to Tensors that the test
  allocated.


#### Returns:

Returns a decorator that will run the decorated test method twice:
once by constructing and executing a graph in a session and once with
eager execution enabled.
