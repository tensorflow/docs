


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.test.TestCase

### `class tf.test.TestCase`

See the guide: [Testing > Unit tests](../../../../api_guides/python/test#Unit_tests)

Base class for tests that need to test TensorFlow.
  

## Child Classes
[`class failureException`](../../tf/test/TestCase/failureException)

## Methods

<h3 id="__init__"><code>__init__(methodName='runTest')</code></h3>



<h3 id="addCleanup"><code>addCleanup(function, *args, **kwargs)</code></h3>

Add a function, with arguments, to be called when the test is
completed. Functions added are called on a LIFO basis and are
called after tearDown on test failure or success.

Cleanup items are called even if setUp fails (unlike tearDown).

<h3 id="addTypeEqualityFunc"><code>addTypeEqualityFunc(typeobj, function)</code></h3>

Add a type specific assertEqual style function to compare a type.

This method is for use by TestCase subclasses that need to register
their own type equality functions to provide nicer error messages.

#### Args:

    typeobj: The data type to call this function on when both values
            are of the same type in assertEqual().
    function: The callable taking two arguments and an optional
            msg= argument that raises self.failureException with a
            useful error message when the two arguments are not equal.

<h3 id="assertAllClose"><code>assertAllClose(a, b, rtol=1e-06, atol=1e-06)</code></h3>

Asserts that two numpy arrays have near values.

#### Args:

* <b>`a`</b>: a numpy ndarray or anything can be converted to one.
* <b>`b`</b>: a numpy ndarray or anything can be converted to one.
* <b>`rtol`</b>: relative tolerance
* <b>`atol`</b>: absolute tolerance

<h3 id="assertAllCloseAccordingToType"><code>assertAllCloseAccordingToType(a, b, rtol=1e-06, atol=1e-06)</code></h3>

Like assertAllClose, but also suitable for comparing fp16 arrays.

In particular, the tolerance is reduced to 1e-3 if at least
one of the arguments is of type float16.

#### Args:

* <b>`a`</b>: a numpy ndarray or anything can be converted to one.
* <b>`b`</b>: a numpy ndarray or anything can be converted to one.
* <b>`rtol`</b>: relative tolerance
* <b>`atol`</b>: absolute tolerance

<h3 id="assertAllEqual"><code>assertAllEqual(a, b)</code></h3>

Asserts that two numpy arrays have the same values.

#### Args:

* <b>`a`</b>: a numpy ndarray or anything can be converted to one.
* <b>`b`</b>: a numpy ndarray or anything can be converted to one.

<h3 id="assertAlmostEqual"><code>assertAlmostEqual(first, second, places=None, msg=None, delta=None)</code></h3>

Fail if the two objects are unequal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
between the two objects is more than the given delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most signficant digit).

If the two objects compare equal then they will automatically
compare almost equal.

<h3 id="assertAlmostEquals"><code>assertAlmostEquals(first, second, places=None, msg=None, delta=None)</code></h3>

Fail if the two objects are unequal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
between the two objects is more than the given delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most signficant digit).

If the two objects compare equal then they will automatically
compare almost equal.

<h3 id="assertArrayNear"><code>assertArrayNear(farray1, farray2, err)</code></h3>

Asserts that two float arrays are near each other.

Checks that for all elements of farray1 and farray2
|f1 - f2| < err.  Asserts a test failure if not.

#### Args:

* <b>`farray1`</b>: a list of float values.
* <b>`farray2`</b>: a list of float values.
* <b>`err`</b>: a float value.

<h3 id="assertDeviceEqual"><code>assertDeviceEqual(device1, device2)</code></h3>

Asserts that the two given devices are the same.

#### Args:

* <b>`device1`</b>: A string device name or TensorFlow `DeviceSpec` object.
* <b>`device2`</b>: A string device name or TensorFlow `DeviceSpec` object.

<h3 id="assertDictContainsSubset"><code>assertDictContainsSubset(expected, actual, msg=None)</code></h3>

Checks whether actual is a superset of expected.

<h3 id="assertDictEqual"><code>assertDictEqual(d1, d2, msg=None)</code></h3>



<h3 id="assertEqual"><code>assertEqual(first, second, msg=None)</code></h3>

Fail if the two objects are unequal as determined by the '=='
operator.

<h3 id="assertEquals"><code>assertEquals(first, second, msg=None)</code></h3>

Fail if the two objects are unequal as determined by the '=='
operator.

<h3 id="assertFalse"><code>assertFalse(expr, msg=None)</code></h3>

Check that the expression is false.

<h3 id="assertGreater"><code>assertGreater(a, b, msg=None)</code></h3>

Just like self.assertTrue(a > b), but with a nicer default message.

<h3 id="assertGreaterEqual"><code>assertGreaterEqual(a, b, msg=None)</code></h3>

Just like self.assertTrue(a >= b), but with a nicer default message.

<h3 id="assertIn"><code>assertIn(member, container, msg=None)</code></h3>

Just like self.assertTrue(a in b), but with a nicer default message.

<h3 id="assertIs"><code>assertIs(expr1, expr2, msg=None)</code></h3>

Just like self.assertTrue(a is b), but with a nicer default message.

<h3 id="assertIsInstance"><code>assertIsInstance(obj, cls, msg=None)</code></h3>

Same as self.assertTrue(isinstance(obj, cls)), with a nicer
default message.

<h3 id="assertIsNone"><code>assertIsNone(obj, msg=None)</code></h3>

Same as self.assertTrue(obj is None), with a nicer default message.

<h3 id="assertIsNot"><code>assertIsNot(expr1, expr2, msg=None)</code></h3>

Just like self.assertTrue(a is not b), but with a nicer default message.

<h3 id="assertIsNotNone"><code>assertIsNotNone(obj, msg=None)</code></h3>

Included for symmetry with assertIsNone.

<h3 id="assertItemsEqual"><code>assertItemsEqual(expected_seq, actual_seq, msg=None)</code></h3>

An unordered sequence specific comparison. It asserts that
actual_seq and expected_seq have the same element counts.
Equivalent to::

    self.assertEqual(Counter(iter(actual_seq)),
                     Counter(iter(expected_seq)))

Asserts that each element has the same count in both sequences.
Example:
    - [0, 1, 1] and [1, 0, 1] compare equal.
    - [0, 0, 1] and [0, 1] compare unequal.

<h3 id="assertLess"><code>assertLess(a, b, msg=None)</code></h3>

Just like self.assertTrue(a < b), but with a nicer default message.

<h3 id="assertLessEqual"><code>assertLessEqual(a, b, msg=None)</code></h3>

Just like self.assertTrue(a <= b), but with a nicer default message.

<h3 id="assertListEqual"><code>assertListEqual(list1, list2, msg=None)</code></h3>

A list-specific equality assertion.

#### Args:

    list1: The first list to compare.
    list2: The second list to compare.
    msg: Optional message to use on failure instead of a list of
            differences.

<h3 id="assertMultiLineEqual"><code>assertMultiLineEqual(first, second, msg=None)</code></h3>

Assert that two multi-line strings are equal.

<h3 id="assertNDArrayNear"><code>assertNDArrayNear(ndarray1, ndarray2, err)</code></h3>

Asserts that two numpy arrays have near values.

#### Args:

* <b>`ndarray1`</b>: a numpy ndarray.
* <b>`ndarray2`</b>: a numpy ndarray.
* <b>`err`</b>: a float. The maximum absolute difference allowed.

<h3 id="assertNear"><code>assertNear(f1, f2, err, msg=None)</code></h3>

Asserts that two floats are near each other.

Checks that |f1 - f2| < err and asserts a test failure
if not.

#### Args:

* <b>`f1`</b>: A float value.
* <b>`f2`</b>: A float value.
* <b>`err`</b>: A float value.
* <b>`msg`</b>: An optional string message to append to the failure message.

<h3 id="assertNotAlmostEqual"><code>assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)</code></h3>

Fail if the two objects are equal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
between the two objects is less than the given delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most signficant digit).

Objects that are equal automatically fail.

<h3 id="assertNotAlmostEquals"><code>assertNotAlmostEquals(first, second, places=None, msg=None, delta=None)</code></h3>

Fail if the two objects are equal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
between the two objects is less than the given delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most signficant digit).

Objects that are equal automatically fail.

<h3 id="assertNotEqual"><code>assertNotEqual(first, second, msg=None)</code></h3>

Fail if the two objects are equal as determined by the '!='
operator.

<h3 id="assertNotEquals"><code>assertNotEquals(first, second, msg=None)</code></h3>

Fail if the two objects are equal as determined by the '!='
operator.

<h3 id="assertNotIn"><code>assertNotIn(member, container, msg=None)</code></h3>

Just like self.assertTrue(a not in b), but with a nicer default message.

<h3 id="assertNotIsInstance"><code>assertNotIsInstance(obj, cls, msg=None)</code></h3>

Included for symmetry with assertIsInstance.

<h3 id="assertNotRegexpMatches"><code>assertNotRegexpMatches(text, unexpected_regexp, msg=None)</code></h3>

Fail the test if the text matches the regular expression.

<h3 id="assertProtoEquals"><code>assertProtoEquals(expected_message_maybe_ascii, message)</code></h3>

Asserts that message is same as parsed expected_message_ascii.

Creates another prototype of message, reads the ascii message into it and
then compares them using self._AssertProtoEqual().

#### Args:

* <b>`expected_message_maybe_ascii`</b>: proto message in original or ascii form
* <b>`message`</b>: the message to validate

<h3 id="assertProtoEqualsVersion"><code>assertProtoEqualsVersion(expected, actual, producer=versions.GRAPH_DEF_VERSION, min_consumer=versions.GRAPH_DEF_VERSION_MIN_CONSUMER)</code></h3>



<h3 id="assertRaises"><code>assertRaises(excClass, callableObj=None, *args, **kwargs)</code></h3>

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

<h3 id="assertRaisesOpError"><code>assertRaisesOpError(expected_err_re_or_predicate)</code></h3>



<h3 id="assertRaisesRegexp"><code>assertRaisesRegexp(expected_exception, expected_regexp, callable_obj=None, *args, **kwargs)</code></h3>

Asserts that the message in a raised exception matches a regexp.

#### Args:

    expected_exception: Exception class expected to be raised.
    expected_regexp: Regexp (re pattern object or string) expected
            to be found in error message.
    callable_obj: Function to be called.
    args: Extra args.
    kwargs: Extra kwargs.

<h3 id="assertRaisesWithPredicateMatch"><code>assertRaisesWithPredicateMatch(*args, **kwds)</code></h3>

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

<h3 id="assertRegexpMatches"><code>assertRegexpMatches(text, expected_regexp, msg=None)</code></h3>

Fail the test unless the text matches the regular expression.

<h3 id="assertSequenceEqual"><code>assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)</code></h3>

An equality assertion for ordered sequences (like lists and tuples).

For the purposes of this function, a valid ordered sequence type is one
which can be indexed, has a length, and has an equality operator.

#### Args:

    seq1: The first sequence to compare.
    seq2: The second sequence to compare.
    seq_type: The expected datatype of the sequences, or None if no
            datatype should be enforced.
    msg: Optional message to use on failure instead of a list of
            differences.

<h3 id="assertSetEqual"><code>assertSetEqual(set1, set2, msg=None)</code></h3>

A set-specific equality assertion.

#### Args:

    set1: The first set to compare.
    set2: The second set to compare.
    msg: Optional message to use on failure instead of a list of
            differences.

assertSetEqual uses ducktyping to support different types of sets, and
is optimized for sets specifically (parameters must support a
difference method).

<h3 id="assertShapeEqual"><code>assertShapeEqual(np_array, tf_tensor)</code></h3>

Asserts that a Numpy ndarray and a TensorFlow tensor have the same shape.

#### Args:

* <b>`np_array`</b>: A Numpy ndarray or Numpy scalar.
* <b>`tf_tensor`</b>: A Tensor.


#### Raises:

* <b>`TypeError`</b>: If the arguments have the wrong type.

<h3 id="assertStartsWith"><code>assertStartsWith(actual, expected_start, msg=None)</code></h3>

Assert that actual.startswith(expected_start) is True.

#### Args:

* <b>`actual`</b>: str
* <b>`expected_start`</b>: str
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertTrue"><code>assertTrue(expr, msg=None)</code></h3>

Check that the expression is true.

<h3 id="assertTupleEqual"><code>assertTupleEqual(tuple1, tuple2, msg=None)</code></h3>

A tuple-specific equality assertion.

#### Args:

    tuple1: The first tuple to compare.
    tuple2: The second tuple to compare.
    msg: Optional message to use on failure instead of a list of
            differences.

<h3 id="assert_"><code>assert_(expr, msg=None)</code></h3>

Check that the expression is true.

<h3 id="checkedThread"><code>checkedThread(target, args=None, kwargs=None)</code></h3>

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

<h3 id="countTestCases"><code>countTestCases()</code></h3>



<h3 id="debug"><code>debug()</code></h3>

Run the test without collecting errors in a TestResult

<h3 id="defaultTestResult"><code>defaultTestResult()</code></h3>



<h3 id="doCleanups"><code>doCleanups()</code></h3>

Execute all cleanup functions. Normally called for you after
tearDown.

<h3 id="fail"><code>fail(msg=None)</code></h3>

Fail immediately, with the given message.

<h3 id="failIf"><code>failIf(*args, **kwargs)</code></h3>



<h3 id="failIfAlmostEqual"><code>failIfAlmostEqual(*args, **kwargs)</code></h3>



<h3 id="failIfEqual"><code>failIfEqual(*args, **kwargs)</code></h3>



<h3 id="failUnless"><code>failUnless(*args, **kwargs)</code></h3>



<h3 id="failUnlessAlmostEqual"><code>failUnlessAlmostEqual(*args, **kwargs)</code></h3>



<h3 id="failUnlessEqual"><code>failUnlessEqual(*args, **kwargs)</code></h3>



<h3 id="failUnlessRaises"><code>failUnlessRaises(*args, **kwargs)</code></h3>



<h3 id="get_temp_dir"><code>get_temp_dir()</code></h3>

Returns a unique temporary directory for the test to use.

Across different test runs, this method will return a different folder.
This will ensure that across different runs tests will not be able to
pollute each others environment.

#### Returns:

  string, the path to the unique temporary directory created for this test.

<h3 id="id"><code>id()</code></h3>



<h3 id="run"><code>run(result=None)</code></h3>



<h3 id="setUp"><code>setUp()</code></h3>



<h3 id="setUpClass"><code>setUpClass(cls)</code></h3>

Hook method for setting up class fixture before running tests in the class.

<h3 id="shortDescription"><code>shortDescription()</code></h3>

Returns a one-line description of the test, or None if no
description has been provided.

The default implementation of this method returns the first line of
the specified test method's docstring.

<h3 id="skipTest"><code>skipTest(reason)</code></h3>

Skip this test.

<h3 id="tearDown"><code>tearDown()</code></h3>



<h3 id="tearDownClass"><code>tearDownClass(cls)</code></h3>

Hook method for deconstructing the class fixture after running all tests in the class.

<h3 id="test_session"><code>test_session(*args, **kwds)</code></h3>

Returns a TensorFlow Session for use in executing tests.

This method should be used for all functional tests.

Use the `use_gpu` and `force_gpu` options to control where ops are run. If
`force_gpu` is True, all ops are pinned to `/gpu:0`. Otherwise, if `use_gpu`
is True, TensorFlow tries to run as many ops on the GPU as possible. If both
`force_gpu and `use_gpu` are False, all ops are pinned to the CPU.

Example:

  class MyOperatorTest(test_util.TensorFlowTestCase):
    def testMyOperator(self):
      with self.test_session(use_gpu=True):
        valid_input = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = MyOperator(valid_input).eval()
        self.assertEqual(result, [1.0, 2.0, 3.0, 5.0, 8.0]
        invalid_input = [-1.0, 2.0, 7.0]
        with self.assertRaisesOpError("negative input not supported"):
          MyOperator(invalid_input).eval()

#### Args:

* <b>`graph`</b>: Optional graph to use during the returned session.
* <b>`config`</b>: An optional config_pb2.ConfigProto to use to configure the
    session.
* <b>`use_gpu`</b>: If True, attempt to run as many ops as possible on GPU.
* <b>`force_gpu`</b>: If True, pin all ops to `/gpu:0`.


#### Returns:

  A Session object that should be used as a context manager to surround
  the graph building and execution code in a test case.



## Class Members

<h3 id="longMessage"><code>longMessage</code></h3>

<h3 id="maxDiff"><code>maxDiff</code></h3>



Defined in [`tensorflow/python/framework/test_util.py`](https://www.tensorflow.org/code/tensorflow/python/framework/test_util.py).

