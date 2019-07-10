page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.TestCase

## Class `TestCase`

Base class for tests that need to test TensorFlow.



### Aliases:

* Class `tf.compat.v1.test.TestCase`
* Class `tf.compat.v2.test.TestCase`
* Class `tf.test.TestCase`



Defined in [`python/framework/test_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/test_util.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(methodName='runTest')
```






## Child Classes
[`class failureException`](../../tf/test/TestCase/failureException)

## Methods

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

Asserts that two structures of numpy arrays or Tensors, have near values.

`a` and `b` can be arbitrarily nested structures. A layer of a nested
structure can be a `dict`, `namedtuple`, `tuple` or `list`.

#### Args:


* <b>`a`</b>: The expected numpy `ndarray`, or anything that can be converted into a
  numpy `ndarray` (including Tensor), or any arbitrarily nested of
  structure of these.
* <b>`b`</b>: The actual numpy `ndarray`, or anything that can be converted into a
  numpy `ndarray` (including Tensor), or any arbitrarily nested of
  structure of these.
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

Asserts that two numpy arrays or Tensors have the same values.


#### Args:


* <b>`a`</b>: the expected numpy ndarray or anything can be converted to one.
* <b>`b`</b>: the actual numpy ndarray or anything can be converted to one.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertAllGreater"><code>assertAllGreater</code></h3>

``` python
assertAllGreater(
    a,
    comparison_target
)
```

Assert element values are all greater than a target value.


#### Args:


* <b>`a`</b>: The numpy `ndarray`, or anything that can be converted into a numpy
  `ndarray` (including Tensor).
* <b>`comparison_target`</b>: The target value of comparison.

<h3 id="assertAllGreaterEqual"><code>assertAllGreaterEqual</code></h3>

``` python
assertAllGreaterEqual(
    a,
    comparison_target
)
```

Assert element values are all greater than or equal to a target value.


#### Args:


* <b>`a`</b>: The numpy `ndarray`, or anything that can be converted into a numpy
  `ndarray` (including Tensor).
* <b>`comparison_target`</b>: The target value of comparison.

<h3 id="assertAllInRange"><code>assertAllInRange</code></h3>

``` python
assertAllInRange(
    target,
    lower_bound,
    upper_bound,
    open_lower_bound=False,
    open_upper_bound=False
)
```

Assert that elements in a Tensor are all in a given range.


#### Args:


* <b>`target`</b>: The numpy `ndarray`, or anything that can be converted into a
  numpy `ndarray` (including Tensor).
* <b>`lower_bound`</b>: lower bound of the range
* <b>`upper_bound`</b>: upper bound of the range
* <b>`open_lower_bound`</b>: (`bool`) whether the lower bound is open (i.e., > rather
  than the default >=)
* <b>`open_upper_bound`</b>: (`bool`) whether the upper bound is open (i.e., < rather
  than the default <=)


#### Raises:


* <b>`AssertionError`</b>:   if the value tensor does not have an ordered numeric type (float* or
    int*), or
  if there are nan values, or
  if any of the elements do not fall in the specified range.

<h3 id="assertAllInSet"><code>assertAllInSet</code></h3>

``` python
assertAllInSet(
    target,
    expected_set
)
```

Assert that elements of a Tensor are all in a given closed set.


#### Args:


* <b>`target`</b>: The numpy `ndarray`, or anything that can be converted into a
  numpy `ndarray` (including Tensor).
* <b>`expected_set`</b>: (`list`, `tuple` or `set`) The closed set that the elements
  of the value of `target` are expected to fall into.


#### Raises:


* <b>`AssertionError`</b>:   if any of the elements do not fall into `expected_set`.

<h3 id="assertAllLess"><code>assertAllLess</code></h3>

``` python
assertAllLess(
    a,
    comparison_target
)
```

Assert element values are all less than a target value.


#### Args:


* <b>`a`</b>: The numpy `ndarray`, or anything that can be converted into a numpy
  `ndarray` (including Tensor).
* <b>`comparison_target`</b>: The target value of comparison.

<h3 id="assertAllLessEqual"><code>assertAllLessEqual</code></h3>

``` python
assertAllLessEqual(
    a,
    comparison_target
)
```

Assert element values are all less than or equal to a target value.


#### Args:


* <b>`a`</b>: The numpy `ndarray`, or anything that can be converted into a numpy
  `ndarray` (including Tensor).
* <b>`comparison_target`</b>: The target value of comparison.

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
as significant digits (measured from the most signficant digit).

If the two objects compare equal then they will automatically
compare almost equal.

<h3 id="assertAlmostEquals"><code>assertAlmostEquals</code></h3>

``` python
assertAlmostEquals(
    *args,
    **kwargs
)
```




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

<h3 id="assertBetween"><code>assertBetween</code></h3>

``` python
assertBetween(
    value,
    minv,
    maxv,
    msg=None
)
```

Asserts that value is between minv and maxv (inclusive).


<h3 id="assertCommandFails"><code>assertCommandFails</code></h3>

``` python
assertCommandFails(
    command,
    regexes,
    env=None,
    close_fds=True,
    msg=None
)
```

Asserts a shell command fails and the error matches a regex in a list.


#### Args:


* <b>`command`</b>: List or string representing the command to run.
* <b>`regexes`</b>: the list of regular expression strings.
* <b>`env`</b>: Dictionary of environment variable settings. If None, no environment
    variables will be set for the child process. This is to make tests
    more hermetic. NOTE: this behavior is different than the standard
    subprocess module.
* <b>`close_fds`</b>: Whether or not to close all open fd's in the child after
    forking.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertCommandSucceeds"><code>assertCommandSucceeds</code></h3>

``` python
assertCommandSucceeds(
    command,
    regexes=(b'',),
    env=None,
    close_fds=True,
    msg=None
)
```

Asserts that a shell command succeeds (i.e. exits with code 0).


#### Args:


* <b>`command`</b>: List or string representing the command to run.
* <b>`regexes`</b>: List of regular expression byte strings that match success.
* <b>`env`</b>: Dictionary of environment variable settings. If None, no environment
    variables will be set for the child process. This is to make tests
    more hermetic. NOTE: this behavior is different than the standard
    subprocess module.
* <b>`close_fds`</b>: Whether or not to close all open fd's in the child after
    forking.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertContainsExactSubsequence"><code>assertContainsExactSubsequence</code></h3>

``` python
assertContainsExactSubsequence(
    container,
    subsequence,
    msg=None
)
```

Asserts that "container" contains "subsequence" as an exact subsequence.

Asserts that "container" contains all the elements of "subsequence", in
order, and without other elements interspersed. For example, [1, 2, 3] is an
exact subsequence of [0, 0, 1, 2, 3, 0] but not of [0, 0, 1, 2, 0, 3, 0].

#### Args:


* <b>`container`</b>: the list we're testing for subsequence inclusion.
* <b>`subsequence`</b>: the list we hope will be an exact subsequence of container.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertContainsInOrder"><code>assertContainsInOrder</code></h3>

``` python
assertContainsInOrder(
    strings,
    target,
    msg=None
)
```

Asserts that the strings provided are found in the target in order.

This may be useful for checking HTML output.

#### Args:


* <b>`strings`</b>: A list of strings, such as [ 'fox', 'dog' ]
* <b>`target`</b>: A target string in which to look for the strings, such as
    'The quick brown fox jumped over the lazy dog'.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertContainsSubsequence"><code>assertContainsSubsequence</code></h3>

``` python
assertContainsSubsequence(
    container,
    subsequence,
    msg=None
)
```

Asserts that "container" contains "subsequence" as a subsequence.

Asserts that "container" contains all the elements of "subsequence", in
order, but possibly with other elements interspersed. For example, [1, 2, 3]
is a subsequence of [0, 0, 1, 2, 0, 3, 0] but not of [0, 0, 1, 3, 0, 2, 0].

#### Args:


* <b>`container`</b>: the list we're testing for subsequence inclusion.
* <b>`subsequence`</b>: the list we hope will be a subsequence of container.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertContainsSubset"><code>assertContainsSubset</code></h3>

``` python
assertContainsSubset(
    expected_subset,
    actual_set,
    msg=None
)
```

Checks whether actual iterable is a superset of expected iterable.


<h3 id="assertCountEqual"><code>assertCountEqual</code></h3>

``` python
assertCountEqual(
    first,
    second,
    msg=None
)
```

An unordered sequence comparison asserting that the same elements,
regardless of order.  If the same element occurs more than once,
it verifies that the elements occur the same number of times.

    self.assertEqual(Counter(list(first)),
                     Counter(list(second)))

 Example:
    - [0, 1, 1] and [1, 0, 1] compare equal.
    - [0, 0, 1] and [0, 1] compare unequal.

<h3 id="assertDTypeEqual"><code>assertDTypeEqual</code></h3>

``` python
assertDTypeEqual(
    target,
    expected_dtype
)
```

Assert ndarray data type is equal to expected.


#### Args:


* <b>`target`</b>: The numpy `ndarray`, or anything that can be converted into a
  numpy `ndarray` (including Tensor).
* <b>`expected_dtype`</b>: Expected data type.

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
    subset,
    dictionary,
    msg=None
)
```

Checks whether dictionary is a superset of subset.


<h3 id="assertDictEqual"><code>assertDictEqual</code></h3>

``` python
assertDictEqual(
    a,
    b,
    msg=None
)
```

Raises AssertionError if a and b are not equal dictionaries.


#### Args:


* <b>`a`</b>: A dict, the expected value.
* <b>`b`</b>: A dict, the actual value.
* <b>`msg`</b>: An optional str, the associated message.


#### Raises:


* <b>`AssertionError`</b>: if the dictionaries are not equal.

<h3 id="assertEmpty"><code>assertEmpty</code></h3>

``` python
assertEmpty(
    container,
    msg=None
)
```

Asserts that an object has zero length.


#### Args:


* <b>`container`</b>: Anything that implements the collections.Sized interface.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertEndsWith"><code>assertEndsWith</code></h3>

``` python
assertEndsWith(
    actual,
    expected_end,
    msg=None
)
```

Asserts that actual.endswith(expected_end) is True.


#### Args:


* <b>`actual`</b>: str
* <b>`expected_end`</b>: str
* <b>`msg`</b>: Optional message to report on failure.

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
    *args,
    **kwargs
)
```




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
    first,
    second,
    msg=None
)
```

An unordered sequence comparison asserting that the same elements,
regardless of order.  If the same element occurs more than once,
it verifies that the elements occur the same number of times.

    self.assertEqual(Counter(list(first)),
                     Counter(list(second)))

 Example:
    - [0, 1, 1] and [1, 0, 1] compare equal.
    - [0, 0, 1] and [0, 1] compare unequal.

<h3 id="assertJsonEqual"><code>assertJsonEqual</code></h3>

``` python
assertJsonEqual(
    first,
    second,
    msg=None
)
```

Asserts that the JSON objects defined in two strings are equal.

A summary of the differences will be included in the failure message
using assertSameStructure.

#### Args:


* <b>`first`</b>: A string contining JSON to decode and compare to second.
* <b>`second`</b>: A string contining JSON to decode and compare to first.
* <b>`msg`</b>: Additional text to include in the failure message.

<h3 id="assertLen"><code>assertLen</code></h3>

``` python
assertLen(
    container,
    expected_len,
    msg=None
)
```

Asserts that an object has the expected length.


#### Args:


* <b>`container`</b>: Anything that implements the collections.Sized interface.
* <b>`expected_len`</b>: The expected length of the container.
* <b>`msg`</b>: Optional message to report on failure.

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

<h3 id="assertLogs"><code>assertLogs</code></h3>

``` python
assertLogs(
    logger=None,
    level=None
)
```

Fail unless a log message of level *level* or higher is emitted
on *logger_name* or its children.  If omitted, *level* defaults to
INFO and *logger* defaults to the root logger.

This method must be used as a context manager, and will yield
a recording object with two attributes: `output` and `records`.
At the end of the context manager, the `output` attribute will
be a list of the matching formatted log messages and the
`records` attribute will be a list of the corresponding LogRecord
objects.

Example::

    with self.assertLogs('foo', level='INFO') as cm:
        logging.getLogger('foo').info('first message')
        logging.getLogger('foo.bar').error('second message')
    self.assertEqual(cm.output, ['INFO:foo:first message',
                                 'ERROR:foo.bar:second message'])

<h3 id="assertMultiLineEqual"><code>assertMultiLineEqual</code></h3>

``` python
assertMultiLineEqual(
    first,
    second,
    msg=None,
    **kwargs
)
```

Asserts that two multi-line strings are equal.


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

<h3 id="assertNoCommonElements"><code>assertNoCommonElements</code></h3>

``` python
assertNoCommonElements(
    expected_seq,
    actual_seq,
    msg=None
)
```

Checks whether actual iterable and expected iterable are disjoint.


<h3 id="assertNotAllClose"><code>assertNotAllClose</code></h3>

``` python
assertNotAllClose(
    a,
    b,
    **kwargs
)
```

Assert that two numpy arrays, or Tensors, do not have near values.


#### Args:


* <b>`a`</b>: the first value to compare.
* <b>`b`</b>: the second value to compare.
* <b>`**kwargs`</b>: additional keyword arguments to be passed to the underlying
  `assertAllClose` call.


#### Raises:


* <b>`AssertionError`</b>: If `a` and `b` are unexpectedly close at all elements.

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
as significant digits (measured from the most signficant digit).

Objects that are equal automatically fail.

<h3 id="assertNotAlmostEquals"><code>assertNotAlmostEquals</code></h3>

``` python
assertNotAlmostEquals(
    *args,
    **kwargs
)
```




<h3 id="assertNotEmpty"><code>assertNotEmpty</code></h3>

``` python
assertNotEmpty(
    container,
    msg=None
)
```

Asserts that an object has non-zero length.


#### Args:


* <b>`container`</b>: Anything that implements the collections.Sized interface.
* <b>`msg`</b>: Optional message to report on failure.

<h3 id="assertNotEndsWith"><code>assertNotEndsWith</code></h3>

``` python
assertNotEndsWith(
    actual,
    unexpected_end,
    msg=None
)
```

Asserts that actual.endswith(unexpected_end) is False.


#### Args:


* <b>`actual`</b>: str
* <b>`unexpected_end`</b>: str
* <b>`msg`</b>: Optional message to report on failure.

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
    *args,
    **kwargs
)
```




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


<h3 id="assertNotRegex"><code>assertNotRegex</code></h3>

``` python
assertNotRegex(
    text,
    unexpected_regex,
    msg=None
)
```

Fail the test if the text matches the regular expression.


<h3 id="assertNotStartsWith"><code>assertNotStartsWith</code></h3>

``` python
assertNotStartsWith(
    actual,
    unexpected_start,
    msg=None
)
```

Asserts that actual.startswith(unexpected_start) is False.


#### Args:


* <b>`actual`</b>: str
* <b>`unexpected_start`</b>: str
* <b>`msg`</b>: Optional message to report on failure.

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

An optional keyword argument 'msg' can be provided when assertRaises
is used as a context object.

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




<h3 id="assertRaisesRegex"><code>assertRaisesRegex</code></h3>

``` python
assertRaisesRegex(
    expected_exception,
    expected_regex,
    callable_obj=None,
    *args,
    **kwargs
)
```

Asserts that the message in a raised exception matches a regex.


#### Args:


* <b>`expected_exception`</b>: Exception class expected to be raised.
* <b>`expected_regex`</b>: Regex (re pattern object or string) expected
        to be found in error message.
* <b>`callable_obj`</b>: Function to be called.
* <b>`msg`</b>: Optional message used in case of failure. Can only be used
        when assertRaisesRegex is used as a context manager.
* <b>`args`</b>: Extra args.
* <b>`kwargs`</b>: Extra kwargs.

<h3 id="assertRaisesRegexp"><code>assertRaisesRegexp</code></h3>

``` python
assertRaisesRegexp(
    expected_exception,
    expected_regex,
    callable_obj=None,
    *args,
    **kwargs
)
```

Asserts that the message in a raised exception matches a regex.


#### Args:


* <b>`expected_exception`</b>: Exception class expected to be raised.
* <b>`expected_regex`</b>: Regex (re pattern object or string) expected
        to be found in error message.
* <b>`callable_obj`</b>: Function to be called.
* <b>`msg`</b>: Optional message used in case of failure. Can only be used
        when assertRaisesRegex is used as a context manager.
* <b>`args`</b>: Extra args.
* <b>`kwargs`</b>: Extra kwargs.

<h3 id="assertRaisesWithLiteralMatch"><code>assertRaisesWithLiteralMatch</code></h3>

``` python
assertRaisesWithLiteralMatch(
    expected_exception,
    expected_exception_message,
    callable_obj=None,
    *args,
    **kwargs
)
```

Asserts that the message in a raised exception equals the given string.

Unlike assertRaisesRegex, this method takes a literal string, not
a regular expression.

with self.assertRaisesWithLiteralMatch(ExType, 'message'):
  DoSomething()

#### Args:


* <b>`expected_exception`</b>: Exception class expected to be raised.
* <b>`expected_exception_message`</b>: String message expected in the raised
    exception.  For a raise exception e, expected_exception_message must
    equal str(e).
* <b>`callable_obj`</b>: Function to be called, or None to return a context.
* <b>`*args`</b>: Extra args.
* <b>`**kwargs`</b>: Extra kwargs.


#### Returns:

A context manager if callable_obj is None. Otherwise, None.



#### Raises:

self.failureException if callable_obj does not raise a matching exception.


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
  of one argument that inspects the passed-in exception and returns True
  (success) or False (please fail the test). Otherwise, the error message
  is expected to match this regular expression partially.


#### Returns:

A context manager to surround code that is expected to raise an
exception.


<h3 id="assertRegex"><code>assertRegex</code></h3>

``` python
assertRegex(
    text,
    expected_regex,
    msg=None
)
```

Fail the test unless the text matches the regular expression.


<h3 id="assertRegexMatch"><code>assertRegexMatch</code></h3>

``` python
assertRegexMatch(
    actual_str,
    regexes,
    message=None
)
```

Asserts that at least one regex in regexes matches str.

If possible you should use `assertRegex`, which is a simpler
version of this method. `assertRegex` takes a single regular
expression (a string or re compiled object) instead of a list.

#### Notes:


1. This function uses substring matching, i.e. the matching
   succeeds if *any* substring of the error message matches *any*
   regex in the list.  This is more convenient for the user than
   full-string matching.

2. If regexes is the empty list, the matching will always fail.

3. Use regexes=[''] for a regex that will always pass.

4. '.' matches any single character *except* the newline.  To
   match any character, use '(.|\n)'.

5. '^' matches the beginning of each line, not just the beginning
   of the string.  Similarly, '$' matches the end of each line.

6. An exception will be thrown if regexes contains an invalid
   regex.

#### Args:


* <b>`actual_str`</b>:  The string we try to match with the items in regexes.
* <b>`regexes`</b>:  The regular expressions we want to match against str.
    See "Notes" above for detailed notes on how this is interpreted.
* <b>`message`</b>:  The message to be printed if the test fails.

<h3 id="assertRegexpMatches"><code>assertRegexpMatches</code></h3>

``` python
assertRegexpMatches(
    *args,
    **kwargs
)
```




<h3 id="assertSameElements"><code>assertSameElements</code></h3>

``` python
assertSameElements(
    expected_seq,
    actual_seq,
    msg=None
)
```

Asserts that two sequences have the same elements (in any order).

This method, unlike assertCountEqual, doesn't care about any
duplicates in the expected and actual sequences.

  >> assertSameElements([1, 1, 1, 0, 0, 0], [0, 1])
  # Doesn't raise an AssertionError

If possible, you should use assertCountEqual instead of
assertSameElements.

#### Args:


* <b>`expected_seq`</b>: A sequence containing elements we are expecting.
* <b>`actual_seq`</b>: The sequence that we are testing.
* <b>`msg`</b>: The message to be printed if the test fails.

<h3 id="assertSameStructure"><code>assertSameStructure</code></h3>

``` python
assertSameStructure(
    a,
    b,
    aname='a',
    bname='b',
    msg=None
)
```

Asserts that two values contain the same structural content.

The two arguments should be data trees consisting of trees of dicts and
lists. They will be deeply compared by walking into the contents of dicts
and lists; other items will be compared using the == operator.
If the two structures differ in content, the failure message will indicate
the location within the structures where the first difference is found.
This may be helpful when comparing large structures.

Mixed Sequence and Set types are supported. Mixed Mapping types are
supported, but the order of the keys will not be considered in the
comparison.

#### Args:


* <b>`a`</b>: The first structure to compare.
* <b>`b`</b>: The second structure to compare.
* <b>`aname`</b>: Variable name to use for the first structure in assertion messages.
* <b>`bname`</b>: Variable name to use for the second structure.
* <b>`msg`</b>: Additional text to include in the failure message.

<h3 id="assertSequenceAlmostEqual"><code>assertSequenceAlmostEqual</code></h3>

``` python
assertSequenceAlmostEqual(
    expected_seq,
    actual_seq,
    places=None,
    msg=None,
    delta=None
)
```

An approximate equality assertion for ordered sequences.

Fail if the two sequences are unequal as determined by their value
differences rounded to the given number of decimal places (default 7) and
comparing to zero, or by comparing that the difference between each value
in the two sequences is more than the given delta.

Note that decimal places (from zero) are usually not the same as significant
digits (measured from the most signficant digit).

If the two sequences compare equal then they will automatically compare
almost equal.

#### Args:


* <b>`expected_seq`</b>: A sequence containing elements we are expecting.
* <b>`actual_seq`</b>: The sequence that we are testing.
* <b>`places`</b>: The number of decimal places to compare.
* <b>`msg`</b>: The message to be printed if the test fails.
* <b>`delta`</b>: The OK difference between compared values.

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

<h3 id="assertSequenceStartsWith"><code>assertSequenceStartsWith</code></h3>

``` python
assertSequenceStartsWith(
    prefix,
    whole,
    msg=None
)
```

An equality assertion for the beginning of ordered sequences.

If prefix is an empty sequence, it will raise an error unless whole is also
an empty sequence.

If prefix is not a sequence, it will raise an error if the first element of
whole does not match.

#### Args:


* <b>`prefix`</b>: A sequence expected at the beginning of the whole parameter.
* <b>`whole`</b>: The sequence in which to look for prefix.
* <b>`msg`</b>: Optional message to report on failure.

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

<h3 id="assertTotallyOrdered"><code>assertTotallyOrdered</code></h3>

``` python
assertTotallyOrdered(
    *groups,
    **kwargs
)
```

Asserts that total ordering has been implemented correctly.

For example, say you have a class A that compares only on its attribute x.
Comparators other than __lt__ are omitted for brevity.

class A(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __hash__(self):
    return hash(self.x)

  def __lt__(self, other):
    try:
      return self.x < other.x
    except AttributeError:
      return NotImplemented

assertTotallyOrdered will check that instances can be ordered correctly.
For example,

self.assertTotallyOrdered(
  [None],  # None should come before everything else.
  [1],     # Integers sort earlier.
  [A(1, 'a')],
  [A(2, 'b')],  # 2 is after 1.
  [A(3, 'c'), A(3, 'd')],  # The second argument is irrelevant.
  [A(4, 'z')],
  ['foo'])  # Strings sort last.

#### Args:


* <b>`*groups`</b>: A list of groups of elements.  Each group of elements is a list
    of objects that are equal.  The elements in each group must be less
    than the elements in the group after it.  For example, these groups are
    totally ordered: [None], [1], [2, 2], [3].
 **kwargs: optional msg keyword argument can be passed.

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

<h3 id="assertUrlEqual"><code>assertUrlEqual</code></h3>

``` python
assertUrlEqual(
    a,
    b,
    msg=None
)
```

Asserts that urls are equal, ignoring ordering of query params.


<h3 id="assertWarns"><code>assertWarns</code></h3>

``` python
assertWarns(
    expected_warning,
    callable_obj=None,
    *args,
    **kwargs
)
```

Fail unless a warning of class warnClass is triggered
by callable_obj when invoked with arguments args and keyword
arguments kwargs.  If a different type of warning is
triggered, it will not be handled: depending on the other
warning filtering rules in effect, it might be silenced, printed
out, or raised as an exception.

If called with callable_obj omitted or None, will return a
context object used like this::

     with self.assertWarns(SomeWarning):
         do_something()

An optional keyword argument 'msg' can be provided when assertWarns
is used as a context object.

The context manager keeps a reference to the first matching
warning as the 'warning' attribute; similarly, the 'filename'
and 'lineno' attributes give you information about the line
of Python code from which the warning was triggered.
This allows you to inspect the warning after the assertion::

    with self.assertWarns(SomeWarning) as cm:
        do_something()
    the_warning = cm.warning
    self.assertEqual(the_warning.some_attribute, 147)

<h3 id="assertWarnsRegex"><code>assertWarnsRegex</code></h3>

``` python
assertWarnsRegex(
    expected_warning,
    expected_regex,
    callable_obj=None,
    *args,
    **kwargs
)
```

Asserts that the message in a triggered warning matches a regexp.
Basic functioning is similar to assertWarns() with the addition
that only warnings whose messages also match the regular expression
are considered successful matches.

#### Args:


* <b>`expected_warning`</b>: Warning class expected to be triggered.
* <b>`expected_regex`</b>: Regex (re pattern object or string) expected
        to be found in error message.
* <b>`callable_obj`</b>: Function to be called.
* <b>`msg`</b>: Optional message used in case of failure. Can only be used
        when assertWarnsRegex is used as a context manager.
* <b>`args`</b>: Extra args.
* <b>`kwargs`</b>: Extra kwargs.

<h3 id="assert_"><code>assert_</code></h3>

``` python
assert_(
    *args,
    **kwargs
)
```




<h3 id="cached_session"><code>cached_session</code></h3>

``` python
cached_session(
    *args,
    **kwds
)
```

Returns a TensorFlow Session for use in executing tests.

This method behaves differently than self.session(): for performance reasons
`cached_session` will by default reuse the same session within the same
test. The session returned by this function will only be closed at the end
of the test (in the TearDown function).

Use the `use_gpu` and `force_gpu` options to control where ops are run. If
`force_gpu` is True, all ops are pinned to `/device:GPU:0`. Otherwise, if
`use_gpu` is True, TensorFlow tries to run as many ops on the GPU as
possible. If both `force_gpu and `use_gpu` are False, all ops are pinned to
the CPU.

#### Example:


```python
class MyOperatorTest(test_util.TensorFlowTestCase):
  def testMyOperator(self):
    with self.cached_session(use_gpu=True) as sess:
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


#### Yields:

A Session object that should be used as a context manager to surround
the graph building and execution code in a test case.


<h3 id="captureWritesToStream"><code>captureWritesToStream</code></h3>

``` python
captureWritesToStream(
    *args,
    **kwds
)
```

A context manager that captures the writes to a given stream.

This context manager captures all writes to a given stream inside of a
`CapturedWrites` object. When this context manager is created, it yields
the `CapturedWrites` object. The captured contents can be accessed  by
calling `.contents()` on the `CapturedWrites`.

For this function to work, the stream must have a file descriptor that
can be modified using `os.dup` and `os.dup2`, and the stream must support
a `.flush()` method. The default python sys.stdout and sys.stderr are
examples of this. Note that this does not work in Colab or Jupyter
notebooks, because those use alternate stdout streams.

#### Example:


```python
class MyOperatorTest(test_util.TensorFlowTestCase):
  def testMyOperator(self):
    input = [1.0, 2.0, 3.0, 4.0, 5.0]
    with self.captureWritesToStream(sys.stdout) as captured:
      result = MyOperator(input).eval()
    self.assertStartsWith(captured.contents(), "This was printed.")
```

#### Args:


* <b>`stream`</b>: The stream whose writes should be captured. This stream must have
  a file descriptor, support writing via using that file descriptor, and
  must have a `.flush()` method.


#### Yields:

A `CapturedWrites` object that contains all writes to the specified stream
made during this context.


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




<h3 id="create_tempdir"><code>create_tempdir</code></h3>

``` python
create_tempdir(
    name=None,
    cleanup=None
)
```

Create a temporary directory specific to the test.

NOTE: The directory and its contents will be recursively cleared before
creation. This ensures that there is no pre-existing state.

This creates a named directory on disk that is isolated to this test, and
will be properly cleaned up by the test. This avoids several pitfalls of
creating temporary directories for test purposes, as well as makes it easier
to setup directories and verify their contents.

See also: `create_tempfile()` for creating temporary files.

#### Args:


* <b>`name`</b>: Optional name of the directory. If not given, a unique
  name will be generated and used.
* <b>`cleanup`</b>: Optional cleanup policy on when/if to remove the directory (and
  all its contents) at the end of the test. If None, then uses
  `self.tempfile_cleanup`.


#### Returns:

A _TempDir representing the created directory.


<h3 id="create_tempfile"><code>create_tempfile</code></h3>

``` python
create_tempfile(
    file_path=None,
    content=None,
    mode='w',
    encoding='utf8',
    errors='strict',
    cleanup=None
)
```

Create a temporary file specific to the test.

This creates a named file on disk that is isolated to this test, and will
be properly cleaned up by the test. This avoids several pitfalls of
creating temporary files for test purposes, as well as makes it easier
to setup files, their data, read them back, and inspect them when
a test fails.

NOTE: This will zero-out the file. This ensures there is no pre-existing
state.

See also: `create_tempdir()` for creating temporary directories.

#### Args:


* <b>`file_path`</b>: Optional file path for the temp file. If not given, a unique
  file name will be generated and used. Slashes are allowed in the name;
  any missing intermediate directories will be created. NOTE: This path is
  the path that will be cleaned up, including any directories in the path,
  e.g., 'foo/bar/baz.txt' will `rm -r foo`.
* <b>`content`</b>: Optional string or
  bytes to initially write to the file. If not
  specified, then an empty file is created.
* <b>`mode`</b>: Mode string to use when writing content. Only used if `content` is
  non-empty.
* <b>`encoding`</b>: Encoding to use when writing string content. Only used if
  `content` is text.
* <b>`errors`</b>: How to handle text to bytes encoding errors. Only used if
  `content` is text.
* <b>`cleanup`</b>: Optional cleanup policy on when/if to remove the directory (and
  all its contents) at the end of the test. If None, then uses
  `self.tempfile_cleanup`.


#### Returns:

A _TempFile representing the created file.


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
fail(
    msg=None,
    prefix=None
)
```

Fail immediately with the given message, optionally prefixed.


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




<h3 id="session"><code>session</code></h3>

``` python
session(
    *args,
    **kwds
)
```

Returns a TensorFlow Session for use in executing tests.

Note that this will set this session and the graph as global defaults.

Use the `use_gpu` and `force_gpu` options to control where ops are run. If
`force_gpu` is True, all ops are pinned to `/device:GPU:0`. Otherwise, if
`use_gpu` is True, TensorFlow tries to run as many ops on the GPU as
possible. If both `force_gpu and `use_gpu` are False, all ops are pinned to
the CPU.

#### Example:


```python
class MyOperatorTest(test_util.TensorFlowTestCase):
  def testMyOperator(self):
    with self.session(use_gpu=True):
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


#### Yields:

A Session object that should be used as a context manager to surround
the graph building and execution code in a test case.


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

Formats both the test method name and the first line of its docstring.

If no docstring is given, only returns the method name.

This method overrides unittest.TestCase.shortDescription(), which
only returns the first line of the docstring, obscuring the name
of the test upon failure.

#### Returns:


* <b>`desc`</b>: A short description of a test method.

<h3 id="skipTest"><code>skipTest</code></h3>

``` python
skipTest(reason)
```

Skip this test.


<h3 id="subTest"><code>subTest</code></h3>

``` python
subTest(
    *args,
    **kwds
)
```

Return a context manager that will return the enclosed block
of code in a subtest identified by the optional message and
keyword parameters.  A failure in the subtest marks the test
case as failed but resumes execution at the end of the enclosed
block, allowing further test code to be executed.

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
    graph=None,
    config=None,
    use_gpu=False,
    force_gpu=False
)
```

Use cached_session instead. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `self.session()` or `self.cached_session()` instead.



## Class Members

* `longMessage = True` <a id="longMessage"></a>
* `maxDiff = 1600` <a id="maxDiff"></a>
* `tempfile_cleanup` <a id="tempfile_cleanup"></a>
