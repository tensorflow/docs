description: Represents an iterator of a <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.Iterator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="get_next"/>
<meta itemprop="property" content="get_next_as_optional"/>
</div>

# tf.data.Iterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/iterator_ops.py#L546-L636">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents an iterator of a <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.

<!-- Placeholder for "Used in" -->

<a href="../../tf/data/Iterator.md"><code>tf.data.Iterator</code></a> is the primary mechanism for enumerating elements of a
<a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>. It supports the Python Iterator protocol, which means
it can be iterated over using a for-loop:

```
>>> dataset = tf.data.Dataset.range(2)
>>> for element in dataset:
...   print(element)
tf.Tensor(0, shape=(), dtype=int64)
tf.Tensor(1, shape=(), dtype=int64)
```

or by fetching individual elements explicitly via `get_next()`:

```
>>> dataset = tf.data.Dataset.range(2)
>>> iterator = iter(dataset)
>>> print(iterator.get_next())
tf.Tensor(0, shape=(), dtype=int64)
>>> print(iterator.get_next())
tf.Tensor(1, shape=(), dtype=int64)
```

In addition, non-raising iteration is supported via `get_next_as_optional()`,
which returns the next element (if available) wrapped in a
<a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a>.

```
>>> dataset = tf.data.Dataset.from_tensors(42)
>>> iterator = iter(dataset)
>>> optional = iterator.get_next_as_optional()
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
>>> optional = iterator.get_next_as_optional()
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
The type specification of an element of this iterator.

```
>>> dataset = tf.data.Dataset.from_tensors(42)
>>> iterator = iter(dataset)
>>> iterator.element_spec
tf.TensorSpec(shape=(), dtype=tf.int32, name=None)
```
</td>
</tr>
</table>



## Methods

<h3 id="get_next"><code>get_next</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/iterator_ops.py#L598-L613">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>get_next()
</code></pre>

Returns a nested structure of <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>s containing the next element.

```
>>> dataset = tf.data.Dataset.from_tensors(42)
>>> iterator = iter(dataset)
>>> print(iterator.get_next())
tf.Tensor(42, shape=(), dtype=int32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A nested structure of <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> objects.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>
<tr class="alt">
<td colspan="2">
<a href="../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a>: If the end of the iterator has been reached.
</td>
</tr>

</table>



<h3 id="get_next_as_optional"><code>get_next_as_optional</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/iterator_ops.py#L615-L636">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>get_next_as_optional()
</code></pre>

Returns a <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> which contains the next element.

If the iterator has reached the end of the sequence, the returned
<a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> will have no value.

```
>>> dataset = tf.data.Dataset.from_tensors(42)
>>> iterator = iter(dataset)
>>> optional = iterator.get_next_as_optional()
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
>>> print(optional.get_value())
tf.Tensor(42, shape=(), dtype=int32)
>>> optional = iterator.get_next_as_optional()
>>> print(optional.has_value())
tf.Tensor(False, shape=(), dtype=bool)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> object representing the next element.
</td>
</tr>

</table>



<h3 id="__iter__"><code>__iter__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>






