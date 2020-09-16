description: Wraps a value that may/may not be present at runtime.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.Optional" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="from_value"/>
<meta itemprop="property" content="get_value"/>
<meta itemprop="property" content="has_value"/>
<meta itemprop="property" content="none_from_structure"/>
</div>

# tf.data.experimental.Optional

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/ops/optional_ops.py#L36-L121">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Wraps a value that may/may not be present at runtime.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.Optional`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

An `Optional` can represent the result of an operation that may fail as a
value, rather than raising an exception and halting execution. For example,
<a href="../../../tf/data/experimental/get_next_as_optional.md"><code>tf.data.experimental.get_next_as_optional</code></a> returns an `Optional` that either
contains the next value of an iterator if one exists, or a "none" value that
indicates the end of the sequence has been reached.

`Optional` can only be used by values that are convertible to `Tensor` or
`CompositeTensor`.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`value_structure`
</td>
<td>
The structure of the components of this optional.
</td>
</tr>
</table>



## Methods

<h3 id="from_value"><code>from_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/ops/optional_ops.py#L87-L105">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>from_value(
    value
)
</code></pre>

Returns an `Optional` that wraps the given value.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
A value to wrap. The value must be convertible to `Tensor` or
`CompositeTensor`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Optional` that wraps `value`.
</td>
</tr>

</table>



<h3 id="get_value"><code>get_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/ops/optional_ops.py#L61-L75">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>get_value(
    name=None
)
</code></pre>

Returns the value wrapped by this optional.

If this optional does not have a value (i.e. `self.has_value()` evaluates
to `False`), this operation will raise <a href="../../../tf/errors/InvalidArgumentError.md"><code>tf.errors.InvalidArgumentError</code></a>
at runtime.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
(Optional.) A name for the created operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The wrapped value.
</td>
</tr>

</table>



<h3 id="has_value"><code>has_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/ops/optional_ops.py#L49-L59">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>has_value(
    name=None
)
</code></pre>

Returns a tensor that evaluates to `True` if this optional has a value.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
(Optional.) A name for the created operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a> of type <a href="../../../tf.md#bool"><code>tf.bool</code></a>.
</td>
</tr>

</table>



<h3 id="none_from_structure"><code>none_from_structure</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/ops/optional_ops.py#L107-L121">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>none_from_structure(
    value_structure
)
</code></pre>

Returns an `Optional` that has no value.

NOTE: This method takes an argument that defines the structure of the value
that would be contained in the returned `Optional` if it had a value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value_structure`
</td>
<td>
A `Structure` object representing the structure of the
components of this optional.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Optional` that has no value.
</td>
</tr>

</table>





