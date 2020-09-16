description: Base class for tests that need to test TensorFlow.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.test.TestCase" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="failureException"/>
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="addClassCleanup"/>
<meta itemprop="property" content="addCleanup"/>
<meta itemprop="property" content="addTypeEqualityFunc"/>
<meta itemprop="property" content="assertAllClose"/>
<meta itemprop="property" content="assertAllCloseAccordingToType"/>
<meta itemprop="property" content="assertAllEqual"/>
<meta itemprop="property" content="assertAllGreater"/>
<meta itemprop="property" content="assertAllGreaterEqual"/>
<meta itemprop="property" content="assertAllInRange"/>
<meta itemprop="property" content="assertAllInSet"/>
<meta itemprop="property" content="assertAllLess"/>
<meta itemprop="property" content="assertAllLessEqual"/>
<meta itemprop="property" content="assertAlmostEqual"/>
<meta itemprop="property" content="assertAlmostEquals"/>
<meta itemprop="property" content="assertArrayNear"/>
<meta itemprop="property" content="assertBetween"/>
<meta itemprop="property" content="assertCommandFails"/>
<meta itemprop="property" content="assertCommandSucceeds"/>
<meta itemprop="property" content="assertContainsExactSubsequence"/>
<meta itemprop="property" content="assertContainsInOrder"/>
<meta itemprop="property" content="assertContainsSubsequence"/>
<meta itemprop="property" content="assertContainsSubset"/>
<meta itemprop="property" content="assertCountEqual"/>
<meta itemprop="property" content="assertDTypeEqual"/>
<meta itemprop="property" content="assertDeviceEqual"/>
<meta itemprop="property" content="assertDictContainsSubset"/>
<meta itemprop="property" content="assertDictEqual"/>
<meta itemprop="property" content="assertEmpty"/>
<meta itemprop="property" content="assertEndsWith"/>
<meta itemprop="property" content="assertEqual"/>
<meta itemprop="property" content="assertEquals"/>
<meta itemprop="property" content="assertFalse"/>
<meta itemprop="property" content="assertGreater"/>
<meta itemprop="property" content="assertGreaterEqual"/>
<meta itemprop="property" content="assertIn"/>
<meta itemprop="property" content="assertIs"/>
<meta itemprop="property" content="assertIsInstance"/>
<meta itemprop="property" content="assertIsNone"/>
<meta itemprop="property" content="assertIsNot"/>
<meta itemprop="property" content="assertIsNotNone"/>
<meta itemprop="property" content="assertItemsEqual"/>
<meta itemprop="property" content="assertJsonEqual"/>
<meta itemprop="property" content="assertLen"/>
<meta itemprop="property" content="assertLess"/>
<meta itemprop="property" content="assertLessEqual"/>
<meta itemprop="property" content="assertListEqual"/>
<meta itemprop="property" content="assertLogs"/>
<meta itemprop="property" content="assertMultiLineEqual"/>
<meta itemprop="property" content="assertNDArrayNear"/>
<meta itemprop="property" content="assertNear"/>
<meta itemprop="property" content="assertNoCommonElements"/>
<meta itemprop="property" content="assertNotAllClose"/>
<meta itemprop="property" content="assertNotAllEqual"/>
<meta itemprop="property" content="assertNotAlmostEqual"/>
<meta itemprop="property" content="assertNotAlmostEquals"/>
<meta itemprop="property" content="assertNotEmpty"/>
<meta itemprop="property" content="assertNotEndsWith"/>
<meta itemprop="property" content="assertNotEqual"/>
<meta itemprop="property" content="assertNotEquals"/>
<meta itemprop="property" content="assertNotIn"/>
<meta itemprop="property" content="assertNotIsInstance"/>
<meta itemprop="property" content="assertNotRegex"/>
<meta itemprop="property" content="assertNotRegexpMatches"/>
<meta itemprop="property" content="assertNotStartsWith"/>
<meta itemprop="property" content="assertProtoEquals"/>
<meta itemprop="property" content="assertProtoEqualsVersion"/>
<meta itemprop="property" content="assertRaises"/>
<meta itemprop="property" content="assertRaisesOpError"/>
<meta itemprop="property" content="assertRaisesRegex"/>
<meta itemprop="property" content="assertRaisesRegexp"/>
<meta itemprop="property" content="assertRaisesWithLiteralMatch"/>
<meta itemprop="property" content="assertRaisesWithPredicateMatch"/>
<meta itemprop="property" content="assertRegex"/>
<meta itemprop="property" content="assertRegexMatch"/>
<meta itemprop="property" content="assertRegexpMatches"/>
<meta itemprop="property" content="assertSameElements"/>
<meta itemprop="property" content="assertSameStructure"/>
<meta itemprop="property" content="assertSequenceAlmostEqual"/>
<meta itemprop="property" content="assertSequenceEqual"/>
<meta itemprop="property" content="assertSequenceStartsWith"/>
<meta itemprop="property" content="assertSetEqual"/>
<meta itemprop="property" content="assertShapeEqual"/>
<meta itemprop="property" content="assertStartsWith"/>
<meta itemprop="property" content="assertTotallyOrdered"/>
<meta itemprop="property" content="assertTrue"/>
<meta itemprop="property" content="assertTupleEqual"/>
<meta itemprop="property" content="assertUrlEqual"/>
<meta itemprop="property" content="assertWarns"/>
<meta itemprop="property" content="assertWarnsRegex"/>
<meta itemprop="property" content="assert_"/>
<meta itemprop="property" content="cached_session"/>
<meta itemprop="property" content="captureWritesToStream"/>
<meta itemprop="property" content="checkedThread"/>
<meta itemprop="property" content="countTestCases"/>
<meta itemprop="property" content="create_tempdir"/>
<meta itemprop="property" content="create_tempfile"/>
<meta itemprop="property" content="debug"/>
<meta itemprop="property" content="defaultTestResult"/>
<meta itemprop="property" content="doClassCleanups"/>
<meta itemprop="property" content="doCleanups"/>
<meta itemprop="property" content="enter_context"/>
<meta itemprop="property" content="evaluate"/>
<meta itemprop="property" content="fail"/>
<meta itemprop="property" content="failIf"/>
<meta itemprop="property" content="failIfAlmostEqual"/>
<meta itemprop="property" content="failIfEqual"/>
<meta itemprop="property" content="failUnless"/>
<meta itemprop="property" content="failUnlessAlmostEqual"/>
<meta itemprop="property" content="failUnlessEqual"/>
<meta itemprop="property" content="failUnlessRaises"/>
<meta itemprop="property" content="get_temp_dir"/>
<meta itemprop="property" content="id"/>
<meta itemprop="property" content="run"/>
<meta itemprop="property" content="session"/>
<meta itemprop="property" content="setUp"/>
<meta itemprop="property" content="setUpClass"/>
<meta itemprop="property" content="shortDescription"/>
<meta itemprop="property" content="skipTest"/>
<meta itemprop="property" content="subTest"/>
<meta itemprop="property" content="tearDown"/>
<meta itemprop="property" content="tearDownClass"/>
<meta itemprop="property" content="test_session"/>
<meta itemprop="property" content="longMessage"/>
<meta itemprop="property" content="maxDiff"/>
<meta itemprop="property" content="tempfile_cleanup"/>
</div>

# tf.test.TestCase

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L1922-L3160">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base class for tests that need to test TensorFlow.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.test.TestCase`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.test.TestCase(
    methodName='runTest'
)
</code></pre>



<!-- Placeholder for "Used in" -->


## Child Classes
[`class failureException`](../../tf/test/TestCase/failureException.md)

## Methods

<h3 id="addClassCleanup"><code>addClassCleanup</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>addClassCleanup(
    function, *args, /, **kwargs
)
</code></pre>

Same as addCleanup, except the cleanup items are called even if
setUpClass fails (unlike tearDownClass).

<h3 id="addCleanup"><code>addCleanup</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>addCleanup(
    function, /, *args, **kwargs
)
</code></pre>

Add a function, with arguments, to be called when the test is
completed. Functions added are called on a LIFO basis and are
called after tearDown on test failure or success.

Cleanup items are called even if setUp fails (unlike tearDown).

<h3 id="addTypeEqualityFunc"><code>addTypeEqualityFunc</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>addTypeEqualityFunc(
    typeobj, function
)
</code></pre>

Add a type specific assertEqual style function to compare a type.

This method is for use by TestCase subclasses that need to register
their own type equality functions to provide nicer error messages.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`typeobj`
</td>
<td>
The data type to call this function on when both values
are of the same type in assertEqual().
</td>
</tr><tr>
<td>
`function`
</td>
<td>
The callable taking two arguments and an optional
msg= argument that raises self.failureException with a
useful error message when the two arguments are not equal.
</td>
</tr>
</table>



<h3 id="assertAllClose"><code>assertAllClose</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2574-L2607">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAllClose(
    a, b, rtol=1e-06, atol=1e-06, msg=None
)
</code></pre>

Asserts that two structures of numpy arrays or Tensors, have near values.

`a` and `b` can be arbitrarily nested structures. A layer of a nested
structure can be a `dict`, `namedtuple`, `tuple` or `list`.

Note: the implementation follows
[`numpy.allclose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)
(and numpy.testing.assert_allclose). It checks whether two arrays are
element-wise equal within a tolerance. The relative difference
(`rtol * abs(b)`) and the absolute difference `atol` are added together
to compare against the absolute difference between `a` and `b`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
The expected numpy `ndarray`, or anything that can be converted into a
numpy `ndarray` (including Tensor), or any arbitrarily nested of
structure of these.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
The actual numpy `ndarray`, or anything that can be converted into a
numpy `ndarray` (including Tensor), or any arbitrarily nested of
structure of these.
</td>
</tr><tr>
<td>
`rtol`
</td>
<td>
relative tolerance.
</td>
</tr><tr>
<td>
`atol`
</td>
<td>
absolute tolerance.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if only one of `a[p]` and `b[p]` is a dict or
`a[p]` and `b[p]` have different length, where `[p]` denotes a path
to the nested structure, e.g. given `a = [(1, 1), {'d': (6, 7)}]` and
`[p] = [1]['d']`, then `a[p] = (6, 7)`.
</td>
</tr>
</table>



<h3 id="assertAllCloseAccordingToType"><code>assertAllCloseAccordingToType</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2609-L2655">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAllCloseAccordingToType(
    a, b, rtol=1e-06, atol=1e-06, float_rtol=1e-06, float_atol=1e-06,
    half_rtol=0.001, half_atol=0.001, bfloat16_rtol=0.01, bfloat16_atol=0.01,
    msg=None
)
</code></pre>

Like assertAllClose, but also suitable for comparing fp16 arrays.

In particular, the tolerance is reduced to 1e-3 if at least
one of the arguments is of type float16.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
the expected numpy ndarray or anything can be converted to one.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
the actual numpy ndarray or anything can be converted to one.
</td>
</tr><tr>
<td>
`rtol`
</td>
<td>
relative tolerance.
</td>
</tr><tr>
<td>
`atol`
</td>
<td>
absolute tolerance.
</td>
</tr><tr>
<td>
`float_rtol`
</td>
<td>
relative tolerance for float32.
</td>
</tr><tr>
<td>
`float_atol`
</td>
<td>
absolute tolerance for float32.
</td>
</tr><tr>
<td>
`half_rtol`
</td>
<td>
relative tolerance for float16.
</td>
</tr><tr>
<td>
`half_atol`
</td>
<td>
absolute tolerance for float16.
</td>
</tr><tr>
<td>
`bfloat16_rtol`
</td>
<td>
relative tolerance for bfloat16.
</td>
</tr><tr>
<td>
`bfloat16_atol`
</td>
<td>
absolute tolerance for bfloat16.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertAllEqual"><code>assertAllEqual</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2676-L2739">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAllEqual(
    a, b, msg=None
)
</code></pre>

Asserts that two numpy arrays or Tensors have the same values.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
the expected numpy ndarray or anything can be converted to one.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
the actual numpy ndarray or anything can be converted to one.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertAllGreater"><code>assertAllGreater</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2756-L2766">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAllGreater(
    a, comparison_target
)
</code></pre>

Assert element values are all greater than a target value.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
The numpy `ndarray`, or anything that can be converted into a numpy
`ndarray` (including Tensor).
</td>
</tr><tr>
<td>
`comparison_target`
</td>
<td>
The target value of comparison.
</td>
</tr>
</table>



<h3 id="assertAllGreaterEqual"><code>assertAllGreaterEqual</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2780-L2790">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAllGreaterEqual(
    a, comparison_target
)
</code></pre>

Assert element values are all greater than or equal to a target value.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
The numpy `ndarray`, or anything that can be converted into a numpy
`ndarray` (including Tensor).
</td>
</tr><tr>
<td>
`comparison_target`
</td>
<td>
The target value of comparison.
</td>
</tr>
</table>



<h3 id="assertAllInRange"><code>assertAllInRange</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2835-L2892">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAllInRange(
    target, lower_bound, upper_bound, open_lower_bound=(False),
    open_upper_bound=(False)
)
</code></pre>

Assert that elements in a Tensor are all in a given range.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`target`
</td>
<td>
The numpy `ndarray`, or anything that can be converted into a
numpy `ndarray` (including Tensor).
</td>
</tr><tr>
<td>
`lower_bound`
</td>
<td>
lower bound of the range
</td>
</tr><tr>
<td>
`upper_bound`
</td>
<td>
upper bound of the range
</td>
</tr><tr>
<td>
`open_lower_bound`
</td>
<td>
(`bool`) whether the lower bound is open (i.e., > rather
than the default >=)
</td>
</tr><tr>
<td>
`open_upper_bound`
</td>
<td>
(`bool`) whether the upper bound is open (i.e., < rather
than the default <=)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AssertionError`
</td>
<td>
if the value tensor does not have an ordered numeric type (float* or
int*), or
if there are nan values, or
if any of the elements do not fall in the specified range.
</td>
</tr>
</table>



<h3 id="assertAllInSet"><code>assertAllInSet</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2894-L2914">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAllInSet(
    target, expected_set
)
</code></pre>

Assert that elements of a Tensor are all in a given closed set.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`target`
</td>
<td>
The numpy `ndarray`, or anything that can be converted into a
numpy `ndarray` (including Tensor).
</td>
</tr><tr>
<td>
`expected_set`
</td>
<td>
(`list`, `tuple` or `set`) The closed set that the elements
of the value of `target` are expected to fall into.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AssertionError`
</td>
<td>
if any of the elements do not fall into `expected_set`.
</td>
</tr>
</table>



<h3 id="assertAllLess"><code>assertAllLess</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2768-L2778">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAllLess(
    a, comparison_target
)
</code></pre>

Assert element values are all less than a target value.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
The numpy `ndarray`, or anything that can be converted into a numpy
`ndarray` (including Tensor).
</td>
</tr><tr>
<td>
`comparison_target`
</td>
<td>
The target value of comparison.
</td>
</tr>
</table>



<h3 id="assertAllLessEqual"><code>assertAllLessEqual</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2792-L2802">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAllLessEqual(
    a, comparison_target
)
</code></pre>

Assert element values are all less than or equal to a target value.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
The numpy `ndarray`, or anything that can be converted into a numpy
`ndarray` (including Tensor).
</td>
</tr><tr>
<td>
`comparison_target`
</td>
<td>
The target value of comparison.
</td>
</tr>
</table>



<h3 id="assertAlmostEqual"><code>assertAlmostEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAlmostEqual(
    first, second, places=None, msg=None, delta=None
)
</code></pre>

Fail if the two objects are unequal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
difference between the two objects is more than the given
delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most significant digit).

If the two objects compare equal then they will automatically
compare almost equal.

<h3 id="assertAlmostEquals"><code>assertAlmostEquals</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertAlmostEquals(
    *args, **kwargs
)
</code></pre>




<h3 id="assertArrayNear"><code>assertArrayNear</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2416-L2431">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertArrayNear(
    farray1, farray2, err, msg=None
)
</code></pre>

Asserts that two float arrays are near each other.

Checks that for all elements of farray1 and farray2
|f1 - f2| < err.  Asserts a test failure if not.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`farray1`
</td>
<td>
a list of float values.
</td>
</tr><tr>
<td>
`farray2`
</td>
<td>
a list of float values.
</td>
</tr><tr>
<td>
`err`
</td>
<td>
a float value.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertBetween"><code>assertBetween</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertBetween(
    value, minv, maxv, msg=None
)
</code></pre>

Asserts that value is between minv and maxv (inclusive).


<h3 id="assertCommandFails"><code>assertCommandFails</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertCommandFails(
    command, regexes, env=None, close_fds=(True), msg=None
)
</code></pre>

Asserts a shell command fails and the error matches a regex in a list.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`command`
</td>
<td>
List or string representing the command to run.
</td>
</tr><tr>
<td>
`regexes`
</td>
<td>
the list of regular expression strings.
</td>
</tr><tr>
<td>
`env`
</td>
<td>
Dictionary of environment variable settings. If None, no environment
variables will be set for the child process. This is to make tests
more hermetic. NOTE: this behavior is different than the standard
subprocess module.
</td>
</tr><tr>
<td>
`close_fds`
</td>
<td>
Whether or not to close all open fd's in the child after
forking.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertCommandSucceeds"><code>assertCommandSucceeds</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertCommandSucceeds(
    command, regexes=(b'',), env=None, close_fds=(True), msg=None
)
</code></pre>

Asserts that a shell command succeeds (i.e. exits with code 0).


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`command`
</td>
<td>
List or string representing the command to run.
</td>
</tr><tr>
<td>
`regexes`
</td>
<td>
List of regular expression byte strings that match success.
</td>
</tr><tr>
<td>
`env`
</td>
<td>
Dictionary of environment variable settings. If None, no environment
variables will be set for the child process. This is to make tests
more hermetic. NOTE: this behavior is different than the standard
subprocess module.
</td>
</tr><tr>
<td>
`close_fds`
</td>
<td>
Whether or not to close all open fd's in the child after
forking.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertContainsExactSubsequence"><code>assertContainsExactSubsequence</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertContainsExactSubsequence(
    container, subsequence, msg=None
)
</code></pre>

Asserts that "container" contains "subsequence" as an exact subsequence.

Asserts that "container" contains all the elements of "subsequence", in
order, and without other elements interspersed. For example, [1, 2, 3] is an
exact subsequence of [0, 0, 1, 2, 3, 0] but not of [0, 0, 1, 2, 0, 3, 0].

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`container`
</td>
<td>
the list we're testing for subsequence inclusion.
</td>
</tr><tr>
<td>
`subsequence`
</td>
<td>
the list we hope will be an exact subsequence of container.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertContainsInOrder"><code>assertContainsInOrder</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertContainsInOrder(
    strings, target, msg=None
)
</code></pre>

Asserts that the strings provided are found in the target in order.

This may be useful for checking HTML output.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`strings`
</td>
<td>
A list of strings, such as [ 'fox', 'dog' ]
</td>
</tr><tr>
<td>
`target`
</td>
<td>
A target string in which to look for the strings, such as
'The quick brown fox jumped over the lazy dog'.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertContainsSubsequence"><code>assertContainsSubsequence</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertContainsSubsequence(
    container, subsequence, msg=None
)
</code></pre>

Asserts that "container" contains "subsequence" as a subsequence.

Asserts that "container" contains all the elements of "subsequence", in
order, but possibly with other elements interspersed. For example, [1, 2, 3]
is a subsequence of [0, 0, 1, 2, 0, 3, 0] but not of [0, 0, 1, 3, 0, 2, 0].

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`container`
</td>
<td>
the list we're testing for subsequence inclusion.
</td>
</tr><tr>
<td>
`subsequence`
</td>
<td>
the list we hope will be a subsequence of container.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertContainsSubset"><code>assertContainsSubset</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertContainsSubset(
    expected_subset, actual_set, msg=None
)
</code></pre>

Checks whether actual iterable is a superset of expected iterable.


<h3 id="assertCountEqual"><code>assertCountEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertCountEqual(
    first, second, msg=None
)
</code></pre>

Asserts that two iterables have the same elements, the same number of
times, without regard to order.

    self.assertEqual(Counter(list(first)),
                     Counter(list(second)))

 Example:
    - [0, 1, 1] and [1, 0, 1] compare equal.
    - [0, 0, 1] and [0, 1] compare unequal.

<h3 id="assertDTypeEqual"><code>assertDTypeEqual</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2916-L2929">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertDTypeEqual(
    target, expected_dtype
)
</code></pre>

Assert ndarray data type is equal to expected.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`target`
</td>
<td>
The numpy `ndarray`, or anything that can be converted into a
numpy `ndarray` (including Tensor).
</td>
</tr><tr>
<td>
`expected_dtype`
</td>
<td>
Expected data type.
</td>
</tr>
</table>



<h3 id="assertDeviceEqual"><code>assertDeviceEqual</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2997-L3009">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertDeviceEqual(
    device1, device2, msg=None
)
</code></pre>

Asserts that the two given devices are the same.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`device1`
</td>
<td>
A string device name or TensorFlow `DeviceSpec` object.
</td>
</tr><tr>
<td>
`device2`
</td>
<td>
A string device name or TensorFlow `DeviceSpec` object.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertDictContainsSubset"><code>assertDictContainsSubset</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertDictContainsSubset(
    subset, dictionary, msg=None
)
</code></pre>

Checks whether dictionary is a superset of subset.


<h3 id="assertDictEqual"><code>assertDictEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertDictEqual(
    a, b, msg=None
)
</code></pre>

Raises AssertionError if a and b are not equal dictionaries.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
A dict, the expected value.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
A dict, the actual value.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
An optional str, the associated message.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AssertionError`
</td>
<td>
if the dictionaries are not equal.
</td>
</tr>
</table>



<h3 id="assertEmpty"><code>assertEmpty</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertEmpty(
    container, msg=None
)
</code></pre>

Asserts that an object has zero length.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`container`
</td>
<td>
Anything that implements the collections.abc.Sized interface.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertEndsWith"><code>assertEndsWith</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertEndsWith(
    actual, expected_end, msg=None
)
</code></pre>

Asserts that actual.endswith(expected_end) is True.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`actual`
</td>
<td>
str
</td>
</tr><tr>
<td>
`expected_end`
</td>
<td>
str
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertEqual"><code>assertEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertEqual(
    first, second, msg=None
)
</code></pre>

Fail if the two objects are unequal as determined by the '=='
operator.

<h3 id="assertEquals"><code>assertEquals</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertEquals(
    *args, **kwargs
)
</code></pre>




<h3 id="assertFalse"><code>assertFalse</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertFalse(
    expr, msg=None
)
</code></pre>

Check that the expression is false.


<h3 id="assertGreater"><code>assertGreater</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertGreater(
    a, b, msg=None
)
</code></pre>

Just like self.assertTrue(a > b), but with a nicer default message.


<h3 id="assertGreaterEqual"><code>assertGreaterEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertGreaterEqual(
    a, b, msg=None
)
</code></pre>

Just like self.assertTrue(a >= b), but with a nicer default message.


<h3 id="assertIn"><code>assertIn</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertIn(
    member, container, msg=None
)
</code></pre>

Just like self.assertTrue(a in b), but with a nicer default message.


<h3 id="assertIs"><code>assertIs</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertIs(
    expr1, expr2, msg=None
)
</code></pre>

Just like self.assertTrue(a is b), but with a nicer default message.


<h3 id="assertIsInstance"><code>assertIsInstance</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertIsInstance(
    obj, cls, msg=None
)
</code></pre>

Same as self.assertTrue(isinstance(obj, cls)), with a nicer
default message.

<h3 id="assertIsNone"><code>assertIsNone</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertIsNone(
    obj, msg=None
)
</code></pre>

Same as self.assertTrue(obj is None), with a nicer default message.


<h3 id="assertIsNot"><code>assertIsNot</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertIsNot(
    expr1, expr2, msg=None
)
</code></pre>

Just like self.assertTrue(a is not b), but with a nicer default message.


<h3 id="assertIsNotNone"><code>assertIsNotNone</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertIsNotNone(
    obj, msg=None
)
</code></pre>

Included for symmetry with assertIsNone.


<h3 id="assertItemsEqual"><code>assertItemsEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertItemsEqual(
    first, second, msg=None
)
</code></pre>

Asserts that two iterables have the same elements, the same number of
times, without regard to order.

    self.assertEqual(Counter(list(first)),
                     Counter(list(second)))

 Example:
    - [0, 1, 1] and [1, 0, 1] compare equal.
    - [0, 0, 1] and [0, 1] compare unequal.

<h3 id="assertJsonEqual"><code>assertJsonEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertJsonEqual(
    first, second, msg=None
)
</code></pre>

Asserts that the JSON objects defined in two strings are equal.

A summary of the differences will be included in the failure message
using assertSameStructure.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`first`
</td>
<td>
A string containing JSON to decode and compare to second.
</td>
</tr><tr>
<td>
`second`
</td>
<td>
A string containing JSON to decode and compare to first.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Additional text to include in the failure message.
</td>
</tr>
</table>



<h3 id="assertLen"><code>assertLen</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertLen(
    container, expected_len, msg=None
)
</code></pre>

Asserts that an object has the expected length.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`container`
</td>
<td>
Anything that implements the collections.abc.Sized interface.
</td>
</tr><tr>
<td>
`expected_len`
</td>
<td>
The expected length of the container.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertLess"><code>assertLess</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertLess(
    a, b, msg=None
)
</code></pre>

Just like self.assertTrue(a < b), but with a nicer default message.


<h3 id="assertLessEqual"><code>assertLessEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertLessEqual(
    a, b, msg=None
)
</code></pre>

Just like self.assertTrue(a <= b), but with a nicer default message.


<h3 id="assertListEqual"><code>assertListEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertListEqual(
    list1, list2, msg=None
)
</code></pre>

A list-specific equality assertion.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`list1`
</td>
<td>
The first list to compare.
</td>
</tr><tr>
<td>
`list2`
</td>
<td>
The second list to compare.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to use on failure instead of a list of
differences.
</td>
</tr>
</table>



<h3 id="assertLogs"><code>assertLogs</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertLogs(
    logger=None, level=None
)
</code></pre>

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

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertMultiLineEqual(
    first, second, msg=None, **kwargs
)
</code></pre>

Asserts that two multi-line strings are equal.


<h3 id="assertNDArrayNear"><code>assertNDArrayNear</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2436-L2446">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNDArrayNear(
    ndarray1, ndarray2, err, msg=None
)
</code></pre>

Asserts that two numpy arrays have near values.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`ndarray1`
</td>
<td>
a numpy ndarray.
</td>
</tr><tr>
<td>
`ndarray2`
</td>
<td>
a numpy ndarray.
</td>
</tr><tr>
<td>
`err`
</td>
<td>
a float. The maximum absolute difference allowed.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertNear"><code>assertNear</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2398-L2414">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNear(
    f1, f2, err, msg=None
)
</code></pre>

Asserts that two floats are near each other.

Checks that |f1 - f2| < err and asserts a test failure
if not.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`f1`
</td>
<td>
A float value.
</td>
</tr><tr>
<td>
`f2`
</td>
<td>
A float value.
</td>
</tr><tr>
<td>
`err`
</td>
<td>
A float value.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
An optional string message to append to the failure message.
</td>
</tr>
</table>



<h3 id="assertNoCommonElements"><code>assertNoCommonElements</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNoCommonElements(
    expected_seq, actual_seq, msg=None
)
</code></pre>

Checks whether actual iterable and expected iterable are disjoint.


<h3 id="assertNotAllClose"><code>assertNotAllClose</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2657-L2674">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotAllClose(
    a, b, **kwargs
)
</code></pre>

Assert that two numpy arrays, or Tensors, do not have near values.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
the first value to compare.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
the second value to compare.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
additional keyword arguments to be passed to the underlying
`assertAllClose` call.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AssertionError`
</td>
<td>
If `a` and `b` are unexpectedly close at all elements.
</td>
</tr>
</table>



<h3 id="assertNotAllEqual"><code>assertNotAllEqual</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2741-L2754">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotAllEqual(
    a, b, msg=None
)
</code></pre>

Asserts that two numpy arrays or Tensors do not have the same values.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
the expected numpy ndarray or anything can be converted to one.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
the actual numpy ndarray or anything can be converted to one.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertNotAlmostEqual"><code>assertNotAlmostEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotAlmostEqual(
    first, second, places=None, msg=None, delta=None
)
</code></pre>

Fail if the two objects are equal as determined by their
difference rounded to the given number of decimal places
(default 7) and comparing to zero, or by comparing that the
difference between the two objects is less than the given delta.

Note that decimal places (from zero) are usually not the same
as significant digits (measured from the most significant digit).

Objects that are equal automatically fail.

<h3 id="assertNotAlmostEquals"><code>assertNotAlmostEquals</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotAlmostEquals(
    *args, **kwargs
)
</code></pre>




<h3 id="assertNotEmpty"><code>assertNotEmpty</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotEmpty(
    container, msg=None
)
</code></pre>

Asserts that an object has non-zero length.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`container`
</td>
<td>
Anything that implements the collections.abc.Sized interface.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertNotEndsWith"><code>assertNotEndsWith</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotEndsWith(
    actual, unexpected_end, msg=None
)
</code></pre>

Asserts that actual.endswith(unexpected_end) is False.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`actual`
</td>
<td>
str
</td>
</tr><tr>
<td>
`unexpected_end`
</td>
<td>
str
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertNotEqual"><code>assertNotEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotEqual(
    first, second, msg=None
)
</code></pre>

Fail if the two objects are equal as determined by the '!='
operator.

<h3 id="assertNotEquals"><code>assertNotEquals</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotEquals(
    *args, **kwargs
)
</code></pre>




<h3 id="assertNotIn"><code>assertNotIn</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotIn(
    member, container, msg=None
)
</code></pre>

Just like self.assertTrue(a not in b), but with a nicer default message.


<h3 id="assertNotIsInstance"><code>assertNotIsInstance</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotIsInstance(
    obj, cls, msg=None
)
</code></pre>

Included for symmetry with assertIsInstance.


<h3 id="assertNotRegex"><code>assertNotRegex</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotRegex(
    text, unexpected_regex, msg=None
)
</code></pre>

Fail the test if the text matches the regular expression.


<h3 id="assertNotRegexpMatches"><code>assertNotRegexpMatches</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotRegexpMatches(
    *args, **kwargs
)
</code></pre>




<h3 id="assertNotStartsWith"><code>assertNotStartsWith</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertNotStartsWith(
    actual, unexpected_start, msg=None
)
</code></pre>

Asserts that actual.startswith(unexpected_start) is False.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`actual`
</td>
<td>
str
</td>
</tr><tr>
<td>
`unexpected_start`
</td>
<td>
str
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertProtoEquals"><code>assertProtoEquals</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2064-L2088">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertProtoEquals(
    expected_message_maybe_ascii, message, msg=None
)
</code></pre>

Asserts that message is same as parsed expected_message_ascii.

Creates another prototype of message, reads the ascii message into it and
then compares them using self._AssertProtoEqual().

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`expected_message_maybe_ascii`
</td>
<td>
proto message in original or ascii form.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
the message to validate.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertProtoEqualsVersion"><code>assertProtoEqualsVersion</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2090-L2099">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertProtoEqualsVersion(
    expected, actual, producer=versions.GRAPH_DEF_VERSION,
    min_consumer=versions.GRAPH_DEF_VERSION_MIN_CONSUMER, msg=None
)
</code></pre>




<h3 id="assertRaises"><code>assertRaises</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertRaises(
    expected_exception, *args, **kwargs
)
</code></pre>

Fail unless an exception of class expected_exception is raised
by the callable when invoked with specified positional and
keyword arguments. If a different type of exception is
raised, it will not be caught, and the test case will be
deemed to have suffered an error, exactly as for an
unexpected exception.

If called with the callable and arguments omitted, will return a
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2975-L2977">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertRaisesOpError(
    expected_err_re_or_predicate
)
</code></pre>




<h3 id="assertRaisesRegex"><code>assertRaisesRegex</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertRaisesRegex(
    expected_exception, expected_regex, *args, **kwargs
)
</code></pre>

Asserts that the message in a raised exception matches a regex.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`expected_exception`
</td>
<td>
Exception class expected to be raised.
</td>
</tr><tr>
<td>
`expected_regex`
</td>
<td>
Regex (re.Pattern object or string) expected
to be found in error message.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Function to be called and extra positional args.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Extra kwargs.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message used in case of failure. Can only be used
when assertRaisesRegex is used as a context manager.
</td>
</tr>
</table>



<h3 id="assertRaisesRegexp"><code>assertRaisesRegexp</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertRaisesRegexp(
    expected_exception, expected_regex, *args, **kwargs
)
</code></pre>

Asserts that the message in a raised exception matches a regex.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`expected_exception`
</td>
<td>
Exception class expected to be raised.
</td>
</tr><tr>
<td>
`expected_regex`
</td>
<td>
Regex (re.Pattern object or string) expected
to be found in error message.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Function to be called and extra positional args.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Extra kwargs.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message used in case of failure. Can only be used
when assertRaisesRegex is used as a context manager.
</td>
</tr>
</table>



<h3 id="assertRaisesWithLiteralMatch"><code>assertRaisesWithLiteralMatch</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertRaisesWithLiteralMatch(
    expected_exception, expected_exception_message, callable_obj=None, *args,
    **kwargs
)
</code></pre>

Asserts that the message in a raised exception equals the given string.

Unlike assertRaisesRegex, this method takes a literal string, not
a regular expression.

with self.assertRaisesWithLiteralMatch(ExType, 'message'):
  DoSomething()

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`expected_exception`
</td>
<td>
Exception class expected to be raised.
</td>
</tr><tr>
<td>
`expected_exception_message`
</td>
<td>
String message expected in the raised
exception.  For a raise exception e, expected_exception_message must
equal str(e).
</td>
</tr><tr>
<td>
`callable_obj`
</td>
<td>
Function to be called, or None to return a context.
</td>
</tr><tr>
<td>
`*args`
</td>
<td>
Extra args.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Extra kwargs.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager if callable_obj is None. Otherwise, None.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>
<tr class="alt">
<td colspan="2">
self.failureException if callable_obj does not raise a matching exception.
</td>
</tr>

</table>



<h3 id="assertRaisesWithPredicateMatch"><code>assertRaisesWithPredicateMatch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2932-L2971">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@contextlib.contextmanager</code>
<code>assertRaisesWithPredicateMatch(
    exception_type, expected_err_re_or_predicate
)
</code></pre>

Returns a context manager to enclose code expected to raise an exception.

If the exception is an OpError, the op stack is also included in the message
predicate search.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`exception_type`
</td>
<td>
The expected type of exception that should be raised.
</td>
</tr><tr>
<td>
`expected_err_re_or_predicate`
</td>
<td>
If this is callable, it should be a function
of one argument that inspects the passed-in exception and returns True
(success) or False (please fail the test). Otherwise, the error message
is expected to match this regular expression partially.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager to surround code that is expected to raise an
exception.
</td>
</tr>

</table>



<h3 id="assertRegex"><code>assertRegex</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertRegex(
    text, expected_regex, msg=None
)
</code></pre>

Fail the test unless the text matches the regular expression.


<h3 id="assertRegexMatch"><code>assertRegexMatch</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertRegexMatch(
    actual_str, regexes, message=None
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`actual_str`
</td>
<td>
The string we try to match with the items in regexes.
</td>
</tr><tr>
<td>
`regexes`
</td>
<td>
The regular expressions we want to match against str.
See "Notes" above for detailed notes on how this is interpreted.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
The message to be printed if the test fails.
</td>
</tr>
</table>



<h3 id="assertRegexpMatches"><code>assertRegexpMatches</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertRegexpMatches(
    *args, **kwargs
)
</code></pre>




<h3 id="assertSameElements"><code>assertSameElements</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertSameElements(
    expected_seq, actual_seq, msg=None
)
</code></pre>

Asserts that two sequences have the same elements (in any order).

This method, unlike assertCountEqual, doesn't care about any
duplicates in the expected and actual sequences.

  >> assertSameElements([1, 1, 1, 0, 0, 0], [0, 1])
  # Doesn't raise an AssertionError

If possible, you should use assertCountEqual instead of
assertSameElements.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`expected_seq`
</td>
<td>
A sequence containing elements we are expecting.
</td>
</tr><tr>
<td>
`actual_seq`
</td>
<td>
The sequence that we are testing.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
The message to be printed if the test fails.
</td>
</tr>
</table>



<h3 id="assertSameStructure"><code>assertSameStructure</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertSameStructure(
    a, b, aname='a', bname='b', msg=None
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`a`
</td>
<td>
The first structure to compare.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
The second structure to compare.
</td>
</tr><tr>
<td>
`aname`
</td>
<td>
Variable name to use for the first structure in assertion messages.
</td>
</tr><tr>
<td>
`bname`
</td>
<td>
Variable name to use for the second structure.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Additional text to include in the failure message.
</td>
</tr>
</table>



<h3 id="assertSequenceAlmostEqual"><code>assertSequenceAlmostEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertSequenceAlmostEqual(
    expected_seq, actual_seq, places=None, msg=None, delta=None
)
</code></pre>

An approximate equality assertion for ordered sequences.

Fail if the two sequences are unequal as determined by their value
differences rounded to the given number of decimal places (default 7) and
comparing to zero, or by comparing that the difference between each value
in the two sequences is more than the given delta.

Note that decimal places (from zero) are usually not the same as significant
digits (measured from the most significant digit).

If the two sequences compare equal then they will automatically compare
almost equal.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`expected_seq`
</td>
<td>
A sequence containing elements we are expecting.
</td>
</tr><tr>
<td>
`actual_seq`
</td>
<td>
The sequence that we are testing.
</td>
</tr><tr>
<td>
`places`
</td>
<td>
The number of decimal places to compare.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
The message to be printed if the test fails.
</td>
</tr><tr>
<td>
`delta`
</td>
<td>
The OK difference between compared values.
</td>
</tr>
</table>



<h3 id="assertSequenceEqual"><code>assertSequenceEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertSequenceEqual(
    seq1, seq2, msg=None, seq_type=None
)
</code></pre>

An equality assertion for ordered sequences (like lists and tuples).

For the purposes of this function, a valid ordered sequence type is one
which can be indexed, has a length, and has an equality operator.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`seq1`
</td>
<td>
The first sequence to compare.
</td>
</tr><tr>
<td>
`seq2`
</td>
<td>
The second sequence to compare.
</td>
</tr><tr>
<td>
`seq_type`
</td>
<td>
The expected datatype of the sequences, or None if no
datatype should be enforced.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to use on failure instead of a list of
differences.
</td>
</tr>
</table>



<h3 id="assertSequenceStartsWith"><code>assertSequenceStartsWith</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertSequenceStartsWith(
    prefix, whole, msg=None
)
</code></pre>

An equality assertion for the beginning of ordered sequences.

If prefix is an empty sequence, it will raise an error unless whole is also
an empty sequence.

If prefix is not a sequence, it will raise an error if the first element of
whole does not match.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`prefix`
</td>
<td>
A sequence expected at the beginning of the whole parameter.
</td>
</tr><tr>
<td>
`whole`
</td>
<td>
The sequence in which to look for prefix.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertSetEqual"><code>assertSetEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertSetEqual(
    set1, set2, msg=None
)
</code></pre>

A set-specific equality assertion.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`set1`
</td>
<td>
The first set to compare.
</td>
</tr><tr>
<td>
`set2`
</td>
<td>
The second set to compare.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to use on failure instead of a list of
differences.
</td>
</tr>
</table>


assertSetEqual uses ducktyping to support different types of sets, and
is optimized for sets specifically (parameters must support a
difference method).

<h3 id="assertShapeEqual"><code>assertShapeEqual</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2979-L2995">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertShapeEqual(
    np_array, tf_tensor, msg=None
)
</code></pre>

Asserts that a Numpy ndarray and a TensorFlow tensor have the same shape.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`np_array`
</td>
<td>
A Numpy ndarray or Numpy scalar.
</td>
</tr><tr>
<td>
`tf_tensor`
</td>
<td>
A Tensor.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If the arguments have the wrong type.
</td>
</tr>
</table>



<h3 id="assertStartsWith"><code>assertStartsWith</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2101-L2112">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertStartsWith(
    actual, expected_start, msg=None
)
</code></pre>

Assert that actual.startswith(expected_start) is True.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`actual`
</td>
<td>
str
</td>
</tr><tr>
<td>
`expected_start`
</td>
<td>
str
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to report on failure.
</td>
</tr>
</table>



<h3 id="assertTotallyOrdered"><code>assertTotallyOrdered</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertTotallyOrdered(
    *groups, **kwargs
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`*groups`
</td>
<td>
A list of groups of elements.  Each group of elements is a list
of objects that are equal.  The elements in each group must be less
than the elements in the group after it.  For example, these groups are
totally ordered: [None], [1], [2, 2], [3].
**kwargs: optional msg keyword argument can be passed.
</td>
</tr>
</table>



<h3 id="assertTrue"><code>assertTrue</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertTrue(
    expr, msg=None
)
</code></pre>

Check that the expression is true.


<h3 id="assertTupleEqual"><code>assertTupleEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertTupleEqual(
    tuple1, tuple2, msg=None
)
</code></pre>

A tuple-specific equality assertion.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tuple1`
</td>
<td>
The first tuple to compare.
</td>
</tr><tr>
<td>
`tuple2`
</td>
<td>
The second tuple to compare.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message to use on failure instead of a list of
differences.
</td>
</tr>
</table>



<h3 id="assertUrlEqual"><code>assertUrlEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertUrlEqual(
    a, b, msg=None
)
</code></pre>

Asserts that urls are equal, ignoring ordering of query params.


<h3 id="assertWarns"><code>assertWarns</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertWarns(
    expected_warning, *args, **kwargs
)
</code></pre>

Fail unless a warning of class warnClass is triggered
by the callable when invoked with specified positional and
keyword arguments.  If a different type of warning is
triggered, it will not be handled: depending on the other
warning filtering rules in effect, it might be silenced, printed
out, or raised as an exception.

If called with the callable and arguments omitted, will return a
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

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assertWarnsRegex(
    expected_warning, expected_regex, *args, **kwargs
)
</code></pre>

Asserts that the message in a triggered warning matches a regexp.
Basic functioning is similar to assertWarns() with the addition
that only warnings whose messages also match the regular expression
are considered successful matches.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`expected_warning`
</td>
<td>
Warning class expected to be triggered.
</td>
</tr><tr>
<td>
`expected_regex`
</td>
<td>
Regex (re.Pattern object or string) expected
to be found in error message.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Function to be called and extra positional args.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Extra kwargs.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
Optional message used in case of failure. Can only be used
when assertWarnsRegex is used as a context manager.
</td>
</tr>
</table>



<h3 id="assert_"><code>assert_</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assert_(
    *args, **kwargs
)
</code></pre>




<h3 id="cached_session"><code>cached_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2209-L2259">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@contextlib.contextmanager</code>
<code>cached_session(
    graph=None, config=None, use_gpu=(False), force_gpu=(False)
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`graph`
</td>
<td>
Optional graph to use during the returned session.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
An optional config_pb2.ConfigProto to use to configure the
session.
</td>
</tr><tr>
<td>
`use_gpu`
</td>
<td>
If True, attempt to run as many ops as possible on GPU.
</td>
</tr><tr>
<td>
`force_gpu`
</td>
<td>
If True, pin all ops to `/device:GPU:0`.
</td>
</tr>
</table>



#### Yields:

A Session object that should be used as a context manager to surround
the graph building and execution code in a test case.


<h3 id="captureWritesToStream"><code>captureWritesToStream</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2003-L2047">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@contextlib.contextmanager</code>
<code>captureWritesToStream(
    stream
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`stream`
</td>
<td>
The stream whose writes should be captured. This stream must have
a file descriptor, support writing via using that file descriptor, and
must have a `.flush()` method.
</td>
</tr>
</table>



#### Yields:

A `CapturedWrites` object that contains all writes to the specified stream
made during this context.


<h3 id="checkedThread"><code>checkedThread</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2377-L2395">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>checkedThread(
    target, args=None, kwargs=None
)
</code></pre>

Returns a Thread wrapper that asserts 'target' completes successfully.

This method should be used to create all threads in test cases, as
otherwise there is a risk that a thread will silently fail, and/or
assertions made in the thread will not be respected.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`target`
</td>
<td>
A callable object to be executed in the thread.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
The argument tuple for the target invocation. Defaults to ().
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
A dictionary of keyword arguments for the target invocation.
Defaults to {}.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A wrapper for threading.Thread that supports start() and join() methods.
</td>
</tr>

</table>



<h3 id="countTestCases"><code>countTestCases</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>countTestCases()
</code></pre>




<h3 id="create_tempdir"><code>create_tempdir</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_tempdir(
    name=None, cleanup=None
)
</code></pre>

Create a temporary directory specific to the test.

NOTE: The directory and its contents will be recursively cleared before
creation. This ensures that there is no pre-existing state.

This creates a named directory on disk that is isolated to this test, and
will be properly cleaned up by the test. This avoids several pitfalls of
creating temporary directories for test purposes, as well as makes it easier
to setup directories and verify their contents.

See also: `create_tempfile()` for creating temporary files.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Optional name of the directory. If not given, a unique
name will be generated and used.
</td>
</tr><tr>
<td>
`cleanup`
</td>
<td>
Optional cleanup policy on when/if to remove the directory (and
all its contents) at the end of the test. If None, then uses
`self.tempfile_cleanup`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A _TempDir representing the created directory.
</td>
</tr>

</table>



<h3 id="create_tempfile"><code>create_tempfile</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_tempfile(
    file_path=None, content=None, mode='w', encoding='utf8', errors='strict',
    cleanup=None
)
</code></pre>

Create a temporary file specific to the test.

This creates a named file on disk that is isolated to this test, and will
be properly cleaned up by the test. This avoids several pitfalls of
creating temporary files for test purposes, as well as makes it easier
to setup files, their data, read them back, and inspect them when
a test fails.

NOTE: This will zero-out the file. This ensures there is no pre-existing
state.
NOTE: If the file already exists, it will be made writable and overwritten.

See also: `create_tempdir()` for creating temporary directories, and
`_TempDir.create_file` for creating files within a temporary directory.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`file_path`
</td>
<td>
Optional file path for the temp file. If not given, a unique
file name will be generated and used. Slashes are allowed in the name;
any missing intermediate directories will be created. NOTE: This path is
the path that will be cleaned up, including any directories in the path,
e.g., 'foo/bar/baz.txt' will `rm -r foo`.
</td>
</tr><tr>
<td>
`content`
</td>
<td>
Optional string or
bytes to initially write to the file. If not
specified, then an empty file is created.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
Mode string to use when writing content. Only used if `content` is
non-empty.
</td>
</tr><tr>
<td>
`encoding`
</td>
<td>
Encoding to use when writing string content. Only used if
`content` is text.
</td>
</tr><tr>
<td>
`errors`
</td>
<td>
How to handle text to bytes encoding errors. Only used if
`content` is text.
</td>
</tr><tr>
<td>
`cleanup`
</td>
<td>
Optional cleanup policy on when/if to remove the directory (and
all its contents) at the end of the test. If None, then uses
`self.tempfile_cleanup`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A _TempFile representing the created file.
</td>
</tr>

</table>



<h3 id="debug"><code>debug</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>debug()
</code></pre>

Run the test without collecting errors in a TestResult


<h3 id="defaultTestResult"><code>defaultTestResult</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>defaultTestResult()
</code></pre>




<h3 id="doClassCleanups"><code>doClassCleanups</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>doClassCleanups()
</code></pre>

Execute all class cleanup functions. Normally called for you after
tearDownClass.

<h3 id="doCleanups"><code>doCleanups</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>doCleanups()
</code></pre>

Execute all cleanup functions. Normally called for you after
tearDown.

<h3 id="enter_context"><code>enter_context</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>enter_context(
    manager
)
</code></pre>

Returns the CM's value after registering it with the exit stack.

Entering a context pushes it onto a stack of contexts. The context is exited
when the test completes. Contexts are are exited in the reverse order of
entering. They will always be exited, regardless of test failure/success.
The context stack is specific to the test being run.

This is useful to eliminate per-test boilerplate when context managers
are used. For example, instead of decorating every test with `@mock.patch`,
simply do `self.foo = self.enter_context(mock.patch(...))' in `setUp()`.

NOTE: The context managers will always be exited without any error
information. This is an unfortunate implementation detail due to some
internals of how unittest runs tests.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`manager`
</td>
<td>
The context manager to enter.
</td>
</tr>
</table>



<h3 id="evaluate"><code>evaluate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2145-L2162">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>evaluate(
    tensors
)
</code></pre>

Evaluates tensors and returns numpy values.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensors`
</td>
<td>
A Tensor or a nested list/tuple of Tensors.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
tensors numpy values.
</td>
</tr>

</table>



<h3 id="fail"><code>fail</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>fail(
    msg=None, prefix=None
)
</code></pre>

Fail immediately with the given message, optionally prefixed.


<h3 id="failIf"><code>failIf</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>failIf(
    *args, **kwargs
)
</code></pre>




<h3 id="failIfAlmostEqual"><code>failIfAlmostEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>failIfAlmostEqual(
    *args, **kwargs
)
</code></pre>




<h3 id="failIfEqual"><code>failIfEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>failIfEqual(
    *args, **kwargs
)
</code></pre>




<h3 id="failUnless"><code>failUnless</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>failUnless(
    *args, **kwargs
)
</code></pre>




<h3 id="failUnlessAlmostEqual"><code>failUnlessAlmostEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>failUnlessAlmostEqual(
    *args, **kwargs
)
</code></pre>




<h3 id="failUnlessEqual"><code>failUnlessEqual</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>failUnlessEqual(
    *args, **kwargs
)
</code></pre>




<h3 id="failUnlessRaises"><code>failUnlessRaises</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>failUnlessRaises(
    *args, **kwargs
)
</code></pre>




<h3 id="get_temp_dir"><code>get_temp_dir</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L1985-L2001">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_temp_dir()
</code></pre>

Returns a unique temporary directory for the test to use.

If you call this method multiple times during in a test, it will return the
same folder. However, across different runs the directories will be
different. This will ensure that across different runs tests will not be
able to pollute each others environment.
If you need multiple unique directories within a single test, you should
use tempfile.mkdtemp as follows:
  tempfile.mkdtemp(dir=self.get_temp_dir()):

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
string, the path to the unique temporary directory created for this test.
</td>
</tr>

</table>



<h3 id="id"><code>id</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>id()
</code></pre>




<h3 id="run"><code>run</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    result=None
)
</code></pre>




<h3 id="session"><code>session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2165-L2207">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@contextlib.contextmanager</code>
<code>session(
    graph=None, config=None, use_gpu=(False), force_gpu=(False)
)
</code></pre>

A context manager for a TensorFlow Session for use in executing tests.

Note that this will set this session and the graph as global defaults.

Use the `use_gpu` and `force_gpu` options to control where ops are run. If
`force_gpu` is True, all ops are pinned to `/device:GPU:0`. Otherwise, if
`use_gpu` is True, TensorFlow tries to run as many ops on the GPU as
possible. If both `force_gpu and `use_gpu` are False, all ops are pinned to
the CPU.

#### Example:



``` python
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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`graph`
</td>
<td>
Optional graph to use during the returned session.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
An optional config_pb2.ConfigProto to use to configure the
session.
</td>
</tr><tr>
<td>
`use_gpu`
</td>
<td>
If True, attempt to run as many ops as possible on GPU.
</td>
</tr><tr>
<td>
`force_gpu`
</td>
<td>
If True, pin all ops to `/device:GPU:0`.
</td>
</tr>
</table>



#### Yields:

A Session object that should be used as a context manager to surround
the graph building and execution code in a test case.


<h3 id="setUp"><code>setUp</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L1944-L1966">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>setUp()
</code></pre>

Hook method for setting up the test fixture before exercising it.


<h3 id="setUpClass"><code>setUpClass</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>setUpClass()
</code></pre>

Hook method for setting up class fixture before running tests in the class.


<h3 id="shortDescription"><code>shortDescription</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>shortDescription()
</code></pre>

Formats both the test method name and the first line of its docstring.

If no docstring is given, only returns the method name.

This method overrides unittest.TestCase.shortDescription(), which
only returns the first line of the docstring, obscuring the name
of the test upon failure.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`desc`
</td>
<td>
A short description of a test method.
</td>
</tr>
</table>



<h3 id="skipTest"><code>skipTest</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>skipTest(
    reason
)
</code></pre>

Skip this test.


<h3 id="subTest"><code>subTest</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@contextlib.contextmanager</code>
<code>subTest(
    msg=_subtest_msg_sentinel, **params
)
</code></pre>

Return a context manager that will return the enclosed block
of code in a subtest identified by the optional message and
keyword parameters.  A failure in the subtest marks the test
case as failed but resumes execution at the end of the enclosed
block, allowing further test code to be executed.

<h3 id="tearDown"><code>tearDown</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L1968-L1978">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tearDown()
</code></pre>

Hook method for deconstructing the test fixture after testing it.


<h3 id="tearDownClass"><code>tearDownClass</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>tearDownClass()
</code></pre>

Hook method for deconstructing the class fixture after running all tests in the class.


<h3 id="test_session"><code>test_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L2261-L2287">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@contextlib.contextmanager</code>
<code>test_session(
    graph=None, config=None, use_gpu=(False), force_gpu=(False)
)
</code></pre>

Use cached_session instead. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `self.session()` or `self.cached_session()` instead.

<h3 id="__call__"><code>__call__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    *args, **kwds
)
</code></pre>

Call self as a function.


<h3 id="__eq__"><code>__eq__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.




## Class Variables

* `longMessage = True` <a id="longMessage"></a>
* `maxDiff = 1600` <a id="maxDiff"></a>
* `tempfile_cleanup` <a id="tempfile_cleanup"></a>
