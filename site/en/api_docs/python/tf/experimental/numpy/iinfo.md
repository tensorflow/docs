description: iinfo(type)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.numpy.iinfo" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.experimental.numpy.iinfo

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



iinfo(type)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.experimental.numpy.iinfo(
    int_type
)
</code></pre>



<!-- Placeholder for "Used in" -->

Machine limits for integer types.

Attributes
----------
bits : int
    The number of bits occupied by the type.
min : int
    The smallest integer expressible by the type.
max : int
    The largest integer expressible by the type.

Parameters
----------
int_type : integer type, dtype, or instance
    The kind of integer data type to get information about.

See Also
--------
finfo : The equivalent for floating point data types.

Examples
--------
With types:

```
>>> ii16 = np.iinfo(np.int16)
>>> ii16.min
-32768
>>> ii16.max
32767
>>> ii32 = np.iinfo(np.int32)
>>> ii32.min
-2147483648
>>> ii32.max
2147483647
```

#### With instances:



```
>>> ii32 = np.iinfo(np.int32(10))
>>> ii32.min
-2147483648
>>> ii32.max
2147483647
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`max`
</td>
<td>
Maximum value of given dtype.
</td>
</tr><tr>
<td>
`min`
</td>
<td>
Minimum value of given dtype.
</td>
</tr>
</table>



