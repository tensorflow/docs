

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.test.TestCase

## Class `TestCase`





Defined in [`tensorflow/python/framework/test_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/framework/test_util.py).

See the guide: [Testing > Unit tests](../../../../api_guides/python/test#Unit_tests)

Base class for tests that need to test TensorFlow.
  

## Child Classes
[`class failureException`](../../tf/test/TestCase/failureException)

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(methodName='runTest')
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    *args,
    **kwds
)
```



<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```



<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```



<h3 id="addCleanup"><code>addCleanup</code></h3>

``` python
addCleanup(
    function,
    *args,
    **kwargs
)
```

Add a function, with arguments, to be called when the test is
completed. Functions added are called on a LIFO basis and are
called after tearDown on test failure or success.

Cleanup items are called even if setUp fails (unlike tearDown).

<h3 id="addTypeEqualityFunc"><code>addTypeEqualityFunc</code></h3>

``` python
addTypeEqualityFunc(
    typeobj,
    function
)
```

Add a type specific assertEqual style function to compare a type.

This method is for use by TestCase subclasses that need to register
their own type equality functions to provide nicer error messages.

#### Args:

* <b>`typeobj`</b>: The data type to call this function on when both values
            are of the same type in assertEqual().
* <b>`function`</b>: The callable taking two arguments and an optional
            msg= argument that raises self.failureException with a
            useful error message when the two arguments are not equal.

<h3 id="assertAllClose"><code>assertAllClose</code></h3>

``` python
assertAllClose(
    a,
    b,
    rtol=1e-06,
    atol=1e-06,
    msg=None
)
```

Asserts that two structures of numpy arrays, have near values.

`a` and `b` can be arbitrarily nested structures. A layer of a nested
structure can be a `dict`, `namedtuple`, `tuple` or `list`.

#### Args:

* <b>`a`</b>: The expected numpy `ndarray`, or anything that can be converted into a
      numpy `ndarray`, or any arbitrarily nested of structure of these.
* <b>`b`</b>: The actual numpy `ndarray`, or anything that can be converted into a
      numpy `ndarray`, or any arbitrarily nested of structure of these.
* <b>`rtol`</b>: relative tolerance.
* <b>`atol`</b>: absolute tolerance.
* <b>`msg`</b>: Optional message to report on failure.


#### Raises:

* <b>`ValueError`</b>: if only one of `a[p]` and `b[p]` is a dict or
      `a[p]` and `b[p]` have different length, where `[p]` denotes a path
      to the nested structure, e.g. given `a = [(1, 1), {'d': (6, 7)}]` and
      `[p] = [1]['d']`, then `a[p] = (6, 7)`.

<h3 id="assertAllCloseAccordingToType"><code>assertAllCloseAccordingToType</code></h3>

``` python
assertAllCloseAccordingToType(
    a,
    b,
    rtol=1e-06,
    atol=1e-06,
    float_rtol=1e-06,
    float_atol=1e-06,
    half_rtol=0.001,
    half_atol=0.001,
    bfloat16_rtol=0.01,
    bfloat16_atol=0.01,
    msg=None
)
```

Like assertAllClose, but also suitable for comparing fp16 arrays.

In particular, the tolerance is reduced to 1e-3 if at least
one of the arguments is of type float16.

#### Args:

* <b>`a`</b>: the expected numpy ndarray or anything can be converted to one.
* <b>`b`</b>: the actual numpy ndarray or anything can be converted to one.
* <b>`rtol`</b>: relative tolerance.
* <b>`atol`</b>: absolute tolerance.
* <b>`float_rtol`</b>: relative tolerance for float32.
* <b>`float_atol`</b>: absolute tolerance for float32.
* <b>`half_rtol`</b>: relative tolerance for float16.
* <b>`half_atol`</b>: absolute tolerance for float16.
* <b>`bfloat16_rtol`</b>: relative tolerance for bfloat16.
* <b>`bfloat16_atol`</b>: absolute tolerance for bfloat16.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertAllEqual"><code>assertAllEqual</code></h3>

``` python
assertAllEqual(
    a,
    b,
    msg=None
)
```

Asserts that two numpy arrays have the same values.

#### Args:

* <b>`a`</b>: the expected numpy ndarray or anything can be converted to one.
* <b>`b`</b>: the actual numpy ndarray or anything can be converted to one.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertAlmostEqual"><code>assertAlmostEqual</code></h3>

``` python
assertAlmostEqual(
    first,
    second,
    places=None,
    msg=None,
    delta=None
)
```

Fail if the two objects are unequal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
between the two objects is more than the given delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most significant digit).

If the two objects compare equal then they will automatically
compare almost equal.

<h3 id="assertAlmostEquals"><code>assertAlmostEquals</code></h3>

``` python
assertAlmostEquals(
    first,
    second,
    places=None,
    msg=None,
    delta=None
)
```

Fail if the two objects are unequal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
between the two objects is more than the given delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most significant digit).

If the two objects compare equal then they will automatically
compare almost equal.

<h3 id="assertArrayNear"><code>assertArrayNear</code></h3>

``` python
assertArrayNear(
    farray1,
    farray2,
    err,
    msg=None
)
```

Asserts that two float arrays are near each other.

Checks that for all elements of farray1 and farray2
|f1 - f2| < err.  Asserts a test failure if not.

#### Args:

* <b>`farray1`</b>: a list of float values.
* <b>`farray2`</b>: a list of float values.
* <b>`err`</b>: a float value.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertDeviceEqual"><code>assertDeviceEqual</code></h3>

``` python
assertDeviceEqual(
    device1,
    device2,
    msg=None
)
```

Asserts that the two given devices are the same.

#### Args:

* <b>`device1`</b>: A string device name or TensorFlow `DeviceSpec` object.
* <b>`device2`</b>: A string device name or TensorFlow `DeviceSpec` object.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertDictContainsSubset"><code>assertDictContainsSubset</code></h3>

``` python
assertDictContainsSubset(
    expected,
    actual,
    msg=None
)
```

Checks whether actual is a superset of expected.

<h3 id="assertDictEqual"><code>assertDictEqual</code></h3>

``` python
assertDictEqual(
    d1,
    d2,
    msg=None
)
```



<h3 id="assertEqual"><code>assertEqual</code></h3>

``` python
assertEqual(
    first,
    second,
    msg=None
)
```

Fail if the two objects are unequal as determined by the '=='
operator.

<h3 id="assertEquals"><code>assertEquals</code></h3>

``` python
assertEquals(
    first,
    second,
    msg=None
)
```

Fail if the two objects are unequal as determined by the '=='
operator.

<h3 id="assertFalse"><code>assertFalse</code></h3>

``` python
assertFalse(
    expr,
    msg=None
)
```

Check that the expression is false.

<h3 id="assertGreater"><code>assertGreater</code></h3>

``` python
assertGreater(
    a,
    b,
    msg=None
)
```

Just like self.assertTrue(a > b), but with a nicer default message.

<h3 id="assertGreaterEqual"><code>assertGreaterEqual</code></h3>

``` python
assertGreaterEqual(
    a,
    b,
    msg=None
)
```

Just like self.assertTrue(a >= b), but with a nicer default message.

<h3 id="assertIn"><code>assertIn</code></h3>

``` python
assertIn(
    member,
    container,
    msg=None
)
```

Just like self.assertTrue(a in b), but with a nicer default message.

<h3 id="assertIs"><code>assertIs</code></h3>

``` python
assertIs(
    expr1,
    expr2,
    msg=None
)
```

Just like self.assertTrue(a is b), but with a nicer default message.

<h3 id="assertIsInstance"><code>assertIsInstance</code></h3>

``` python
assertIsInstance(
    obj,
    cls,
    msg=None
)
```

Same as self.assertTrue(isinstance(obj, cls)), with a nicer
default message.

<h3 id="assertIsNone"><code>assertIsNone</code></h3>

``` python
assertIsNone(
    obj,
    msg=None
)
```

Same as self.assertTrue(obj is None), with a nicer default message.

<h3 id="assertIsNot"><code>assertIsNot</code></h3>

``` python
assertIsNot(
    expr1,
    expr2,
    msg=None
)
```

Just like self.assertTrue(a is not b), but with a nicer default message.

<h3 id="assertIsNotNone"><code>assertIsNotNone</code></h3>

``` python
assertIsNotNone(
    obj,
    msg=None
)
```

Included for symmetry with assertIsNone.

<h3 id="assertItemsEqual"><code>assertItemsEqual</code></h3>

``` python
assertItemsEqual(
    expected_seq,
    actual_seq,
    msg=None
)
```

An unordered sequence specific comparison. It asserts that
actual_seq and expected_seq have the same element counts.
Equivalent to::

    self.assertEqual(Counter(iter(actual_seq)),
                     Counter(iter(expected_seq)))

Asserts that each element has the same count in both sequences.
Example:
    - [0, 1, 1] and [1, 0, 1] compare equal.
    - [0, 0, 1] and [0, 1] compare unequal.

<h3 id="assertLess"><code>assertLess</code></h3>

``` python
assertLess(
    a,
    b,
    msg=None
)
```

Just like self.assertTrue(a < b), but with a nicer default message.

<h3 id="assertLessEqual"><code>assertLessEqual</code></h3>

``` python
assertLessEqual(
    a,
    b,
    msg=None
)
```

Just like self.assertTrue(a <= b), but with a nicer default message.

<h3 id="assertListEqual"><code>assertListEqual</code></h3>

``` python
assertListEqual(
    list1,
    list2,
    msg=None
)
```

A list-specific equality assertion.

#### Args:

* <b>`list1`</b>: The first list to compare.
* <b>`list2`</b>: The second list to compare.
* <b>`msg`</b>: Optional message to use on failure instead of a list of
            differences.

<h3 id="assertMultiLineEqual"><code>assertMultiLineEqual</code></h3>

``` python
assertMultiLineEqual(
    first,
    second,
    msg=None
)
```

Assert that two multi-line strings are equal.

<h3 id="assertNDArrayNear"><code>assertNDArrayNear</code></h3>

``` python
assertNDArrayNear(
    ndarray1,
    ndarray2,
    err,
    msg=None
)
```

Asserts that two numpy arrays have near values.

#### Args:

* <b>`ndarray1`</b>: a numpy ndarray.
* <b>`ndarray2`</b>: a numpy ndarray.
* <b>`err`</b>: a float. The maximum absolute difference allowed.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertNear"><code>assertNear</code></h3>

``` python
assertNear(
    f1,
    f2,
    err,
    msg=None
)
```

Asserts that two floats are near each other.

Checks that |f1 - f2| < err and asserts a test failure
if not.

#### Args:

* <b>`f1`</b>: A float value.
* <b>`f2`</b>: A float value.
* <b>`err`</b>: A float value.
* <b>`msg`</b>: An optional string message to append to the failure message.

<h3 id="assertNotAlmostEqual"><code>assertNotAlmostEqual</code></h3>

``` python
assertNotAlmostEqual(
    first,
    second,
    places=None,
    msg=None,
    delta=None
)
```

Fail if the two objects are equal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
between the two objects is less than the given delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most significant digit).

Objects that are equal automatically fail.

<h3 id="assertNotAlmostEquals"><code>assertNotAlmostEquals</code></h3>

``` python
assertNotAlmostEquals(
    first,
    second,
    places=None,
    msg=None,
    delta=None
)
```

Fail if the two objects are equal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
between the two objects is less than the given delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most significant digit).

Objects that are equal automatically fail.

<h3 id="assertNotEqual"><code>assertNotEqual</code></h3>

``` python
assertNotEqual(
    first,
    second,
    msg=None
)
```

Fail if the two objects are equal as determined by the '!='
operator.

<h3 id="assertNotEquals"><code>assertNotEquals</code></h3>

``` python
assertNotEquals(
    first,
    second,
    msg=None
)
```

Fail if the two objects are equal as determined by the '!='
operator.

<h3 id="assertNotIn"><code>assertNotIn</code></h3>

``` python
assertNotIn(
    member,
    container,
    msg=None
)
```

Just like self.assertTrue(a not in b), but with a nicer default message.

<h3 id="assertNotIsInstance"><code>assertNotIsInstance</code></h3>

``` python
assertNotIsInstance(
    obj,
    cls,
    msg=None
)
```

Included for symmetry with assertIsInstance.

<h3 id="assertNotRegexpMatches"><code>assertNotRegexpMatches</code></h3>

``` python
assertNotRegexpMatches(
    text,
    unexpected_regexp,
    msg=None
)
```

Fail the test if the text matches the regular expression.

<h3 id="assertProtoEquals"><code>assertProtoEquals</code></h3>

``` python
assertProtoEquals(
    expected_message_maybe_ascii,
    message,
    msg=None
)
```

Asserts that message is same as parsed expected_message_ascii.

Creates another prototype of message, reads the ascii message into it and
then compares them using self._AssertProtoEqual().

#### Args:

* <b>`expected_message_maybe_ascii`</b>: proto message in original or ascii form.
* <b>`message`</b>: the message to validate.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertProtoEqualsVersion"><code>assertProtoEqualsVersion</code></h3>

``` python
assertProtoEqualsVersion(
    expected,
    actual,
    producer=versions.GRAPH_DEF_VERSION,
    min_consumer=versions.GRAPH_DEF_VERSION_MIN_CONSUMER,
    msg=None
)
```



<h3 id="assertRaises"><code>assertRaises</code></h3>

``` python
assertRaises(
    excClass,
    callableObj=None,
    *args,
    **kwargs
)
```

Fail unless an exception of class excClass is raised
by callableObj when invoked with arguments args and keyword
arguments kwargs. If a different type of exception is
raised, it will not be caught, and the test case will be
deemed to have suffered an error, exactly as for an
unexpected exception.

If called with callableObj omitted or None, will return a
context object used like this::

     with self.assertRaises(SomeException):
         do_something()

The context manager keeps a reference to the exception as
the 'exception' attribute. This allows you to inspect the
exception after the assertion::

    with self.assertRaises(SomeException) as cm:
        do_something()
    the_exception = cm.exception
    self.assertEqual(the_exception.error_code, 3)

<h3 id="assertRaisesOpError"><code>assertRaisesOpError</code></h3>

``` python
assertRaisesOpError(expected_err_re_or_predicate)
```



<h3 id="assertRaisesRegexp"><code>assertRaisesRegexp</code></h3>

``` python
assertRaisesRegexp(
    expected_exception,
    expected_regexp,
    callable_obj=None,
    *args,
    **kwargs
)
```

Asserts that the message in a raised exception matches a regexp.

#### Args:

* <b>`expected_exception`</b>: Exception class expected to be raised.
* <b>`expected_regexp`</b>: Regexp (re pattern object or string) expected
            to be found in error message.
* <b>`callable_obj`</b>: Function to be called.
* <b>`args`</b>: Extra args.
* <b>`kwargs`</b>: Extra kwargs.

<h3 id="assertRaisesWithPredicateMatch"><code>assertRaisesWithPredicateMatch</code></h3>

``` python
assertRaisesWithPredicateMatch(
    *args,
    **kwds
)
```

Returns a context manager to enclose code expected to raise an exception.

If the exception is an OpError, the op stack is also included in the message
predicate search.

#### Args:

* <b>`exception_type`</b>: The expected type of exception that should be raised.
* <b>`expected_err_re_or_predicate`</b>: If this is callable, it should be a function
    of one argument that inspects the passed-in exception and
    returns True (success) or False (please fail the test). Otherwise, the
    error message is expected to match this regular expression partially.


#### Returns:

A context manager to surround code that is expected to raise an
exception.

<h3 id="assertRegexpMatches"><code>assertRegexpMatches</code></h3>

``` python
assertRegexpMatches(
    text,
    expected_regexp,
    msg=None
)
```

Fail the test unless the text matches the regular expression.

<h3 id="assertSequenceEqual"><code>assertSequenceEqual</code></h3>

``` python
assertSequenceEqual(
    seq1,
    seq2,
    msg=None,
    seq_type=None
)
```

An equality assertion for ordered sequences (like lists and tuples).

For the purposes of this function, a valid ordered sequence type is one
which can be indexed, has a length, and has an equality operator.

#### Args:

* <b>`seq1`</b>: The first sequence to compare.
* <b>`seq2`</b>: The second sequence to compare.
* <b>`seq_type`</b>: The expected datatype of the sequences, or None if no
            datatype should be enforced.
* <b>`msg`</b>: Optional message to use on failure instead of a list of
            differences.

<h3 id="assertSetEqual"><code>assertSetEqual</code></h3>

``` python
assertSetEqual(
    set1,
    set2,
    msg=None
)
```

A set-specific equality assertion.

#### Args:

* <b>`set1`</b>: The first set to compare.
* <b>`set2`</b>: The second set to compare.
* <b>`msg`</b>: Optional message to use on failure instead of a list of
            differences.

assertSetEqual uses ducktyping to support different types of sets, and
is optimized for sets specifically (parameters must support a
difference method).

<h3 id="assertShapeEqual"><code>assertShapeEqual</code></h3>

``` python
assertShapeEqual(
    np_array,
    tf_tensor,
    msg=None
)
```

Asserts that a Numpy ndarray and a TensorFlow tensor have the same shape.

#### Args:

* <b>`np_array`</b>: A Numpy ndarray or Numpy scalar.
* <b>`tf_tensor`</b>: A Tensor.
* <b>`msg`</b>: Optional message to report on failure.


#### Raises:

* <b>`TypeError`</b>: If the arguments have the wrong type.

<h3 id="assertStartsWith"><code>assertStartsWith</code></h3>

``` python
assertStartsWith(
    actual,
    expected_start,
    msg=None
)
```

Assert that actual.startswith(expected_start) is True.

#### Args:

* <b>`actual`</b>: str
* <b>`expected_start`</b>: str
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertTrue"><code>assertTrue</code></h3>

``` python
assertTrue(
    expr,
    msg=None
)
```

Check that the expression is true.

<h3 id="assertTupleEqual"><code>assertTupleEqual</code></h3>

``` python
assertTupleEqual(
    tuple1,
    tuple2,
    msg=None
)
```

A tuple-specific equality assertion.

#### Args:

* <b>`tuple1`</b>: The first tuple to compare.
* <b>`tuple2`</b>: The second tuple to compare.
* <b>`msg`</b>: Optional message to use on failure instead of a list of
            differences.

<h3 id="assert_"><code>assert_</code></h3>

``` python
assert_(
    expr,
    msg=None
)
```

Check that the expression is true.

<h3 id="checkedThread"><code>checkedThread</code></h3>

``` python
checkedThread(
    target,
    args=None,
    kwargs=None
)
```

Returns a Thread wrapper that asserts 'target' completes successfully.

This method should be used to create all threads in test cases, as
otherwise there is a risk that a thread will silently fail, and/or
assertions made in the thread will not be respected.

#### Args:

* <b>`target`</b>: A callable object to be executed in the thread.
* <b>`args`</b>: The argument tuple for the target invocation. Defaults to ().
* <b>`kwargs`</b>: A dictionary of keyword arguments for the target invocation.
    Defaults to {}.


#### Returns:

A wrapper for threading.Thread that supports start() and join() methods.

<h3 id="countTestCases"><code>countTestCases</code></h3>

``` python
countTestCases()
```



<h3 id="debug"><code>debug</code></h3>

``` python
debug()
```

Run the test without collecting errors in a TestResult

<h3 id="defaultTestResult"><code>defaultTestResult</code></h3>

``` python
defaultTestResult()
```



<h3 id="doCleanups"><code>doCleanups</code></h3>

``` python
doCleanups()
```

Execute all cleanup functions. Normally called for you after
tearDown.

<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate(tensors)
```

Evaluates tensors and returns numpy values.

#### Args:

* <b>`tensors`</b>: A Tensor or a nested list/tuple of Tensors.


#### Returns:

tensors numpy values.

<h3 id="fail"><code>fail</code></h3>

``` python
fail(msg=None)
```

Fail immediately, with the given message.

<h3 id="failIf"><code>failIf</code></h3>

``` python
failIf(
    *args,
    **kwargs
)
```



<h3 id="failIfAlmostEqual"><code>failIfAlmostEqual</code></h3>

``` python
failIfAlmostEqual(
    *args,
    **kwargs
)
```



<h3 id="failIfEqual"><code>failIfEqual</code></h3>

``` python
failIfEqual(
    *args,
    **kwargs
)
```



<h3 id="failUnless"><code>failUnless</code></h3>

``` python
failUnless(
    *args,
    **kwargs
)
```



<h3 id="failUnlessAlmostEqual"><code>failUnlessAlmostEqual</code></h3>

``` python
failUnlessAlmostEqual(
    *args,
    **kwargs
)
```



<h3 id="failUnlessEqual"><code>failUnlessEqual</code></h3>

``` python
failUnlessEqual(
    *args,
    **kwargs
)
```



<h3 id="failUnlessRaises"><code>failUnlessRaises</code></h3>

``` python
failUnlessRaises(
    *args,
    **kwargs
)
```



<h3 id="get_temp_dir"><code>get_temp_dir</code></h3>

``` python
get_temp_dir()
```

Returns a unique temporary directory for the test to use.

If you call this method multiple times during in a test, it will return the
same folder. However, across different runs the directories will be
different. This will ensure that across different runs tests will not be
able to pollute each others environment.
If you need multiple unique directories within a single test, you should
use tempfile.mkdtemp as follows:
  tempfile.mkdtemp(dir=self.get_temp_dir()):

#### Returns:

string, the path to the unique temporary directory created for this test.

<h3 id="id"><code>id</code></h3>

``` python
id()
```



<h3 id="run"><code>run</code></h3>

``` python
run(result=None)
```



<h3 id="setUp"><code>setUp</code></h3>

``` python
setUp()
```



<h3 id="setUpClass"><code>setUpClass</code></h3>

``` python
setUpClass(cls)
```

Hook method for setting up class fixture before running tests in the class.

<h3 id="shortDescription"><code>shortDescription</code></h3>

``` python
shortDescription()
```

Returns a one-line description of the test, or None if no
description has been provided.

The default implementation of this method returns the first line of
the specified test method's docstring.

<h3 id="skipTest"><code>skipTest</code></h3>

``` python
skipTest(reason)
```

Skip this test.

<h3 id="tearDown"><code>tearDown</code></h3>

``` python
tearDown()
```



<h3 id="tearDownClass"><code>tearDownClass</code></h3>

``` python
tearDownClass(cls)
```

Hook method for deconstructing the class fixture after running all tests in the class.

<h3 id="test_session"><code>test_session</code></h3>

``` python
test_session(
    *args,
    **kwds
)
```

Returns a TensorFlow Session for use in executing tests.

This method should be used for all functional tests.

This method behaves different than session.Session: for performance reasons
`test_session` will by default (if `graph` is None) reuse the same session
across tests. This means you may want to either call the function
`reset_default_graph()` before tests, or if creating an explicit new graph,
pass it here (simply setting it with `as_default()` won't do it), which will
trigger the creation of a new session.

Use the `use_gpu` and `force_gpu` options to control where ops are run. If
`force_gpu` is True, all ops are pinned to `/device:GPU:0`. Otherwise, if
`use_gpu`
is True, TensorFlow tries to run as many ops on the GPU as possible. If both
`force_gpu and `use_gpu` are False, all ops are pinned to the CPU.

Example:

```python
class MyOperatorTest(test_util.TensorFlowTestCase):
  def testMyOperator(self):
    with self.test_session(use_gpu=True):
      valid_input = [1.0, 2.0, 3.0, 4.0, 5.0]
      result = MyOperator(valid_input).eval()
      self.assertEqual(result, [1.0, 2.0, 3.0, 5.0, 8.0]
      invalid_input = [-1.0, 2.0, 7.0]
      with self.assertRaisesOpError("negative input not supported"):
        MyOperator(invalid_input).eval()
```

#### Args:

* <b>`graph`</b>: Optional graph to use during the returned session.
* <b>`config`</b>: An optional config_pb2.ConfigProto to use to configure the
    session.
* <b>`use_gpu`</b>: If True, attempt to run as many ops as possible on GPU.
* <b>`force_gpu`</b>: If True, pin all ops to `/device:GPU:0`.


#### Returns:

A Session object that should be used as a context manager to surround
the graph building and execution code in a test case.



## Class Members

<h3 id="longMessage"><code>longMessage</code></h3>

<h3 id="maxDiff"><code>maxDiff</code></h3>

