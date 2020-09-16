description: Represents a value that may or may not be present.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.Optional" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="empty"/>
<meta itemprop="property" content="from_value"/>
<meta itemprop="property" content="get_value"/>
<meta itemprop="property" content="has_value"/>
</div>

# tf.experimental.Optional

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/optional_ops.py#L38-L163">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents a value that may or may not be present.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.data.experimental.Optional`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.Optional`, `tf.compat.v1.experimental.Optional`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

A <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> can represent the result of an operation that may
fail as a value, rather than raising an exception and halting execution. For
example, <a href="../../tf/data/Iterator.md#get_next_as_optional"><code>tf.data.Iterator.get_next_as_optional()</code></a> returns a
<a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> that either contains the next element of an
iterator if one exists, or an "empty" value that indicates the end of the
sequence has been reached.

<a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> can only be used with values that are convertible
to <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or `tf.CompositeTensor`.

One can create a <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> from a value using the
`from_value()` method:

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
>>> print(optional.get_value())
tf.Tensor(42, shape=(), dtype=int32)
```

or without a value using the `empty()` method:

```
>>> optional = tf.experimental.Optional.empty(
...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))
>>> print(optional.has_value())
tf.Tensor(False, shape=(), dtype=bool)
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`element_spec`
</td>
<td>
The type specification of an element of this optional.

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.element_spec)
tf.TensorSpec(shape=(), dtype=tf.int32, name=None)
```
</td>
</tr>
</table>



## Methods

<h3 id="empty"><code>empty</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/optional_ops.py#L118-L137">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>empty(
    element_spec
)
</code></pre>

Returns an `Optional` that has no value.

NOTE: This method takes an argument that defines the structure of the value
that would be contained in the returned `Optional` if it had a value.

```
>>> optional = tf.experimental.Optional.empty(
...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))
>>> print(optional.has_value())
tf.Tensor(False, shape=(), dtype=bool)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`element_spec`
</td>
<td>
A nested structure of <a href="../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> objects matching the
structure of an element of this optional.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> with no value.
</td>
</tr>

</table>



<h3 id="from_value"><code>from_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/optional_ops.py#L139-L163">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>from_value(
    value
)
</code></pre>

Returns a <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> that wraps the given value.

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
>>> print(optional.get_value())
tf.Tensor(42, shape=(), dtype=int32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
A value to wrap. The value must be convertible to <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or
`tf.CompositeTensor`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> that wraps `value`.
</td>
</tr>

</table>



<h3 id="get_value"><code>get_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/optional_ops.py#L84-L102">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>get_value(
    name=None
)
</code></pre>

Returns the value wrapped by this optional.

If this optional does not have a value (i.e. `self.has_value()` evaluates to
`False`), this operation will raise <a href="../../tf/errors/InvalidArgumentError.md"><code>tf.errors.InvalidArgumentError</code></a> at
runtime.

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.get_value())
tf.Tensor(42, shape=(), dtype=int32)
```

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/optional_ops.py#L68-L82">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>has_value(
    name=None
)
</code></pre>

Returns a tensor that evaluates to `True` if this optional has a value.

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
```

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
A scalar <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type <a href="../../tf.md#bool"><code>tf.bool</code></a>.
</td>
</tr>

</table>





