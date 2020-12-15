description: Returns True if first argument is a typecode lower/equal in type hierarchy.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.numpy.issubdtype" />
<meta itemprop="path" content="Stable" />
</div>

# tf.experimental.numpy.issubdtype

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns True if first argument is a typecode lower/equal in type hierarchy.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.experimental.numpy.issubdtype(
    arg1, arg2
)
</code></pre>



<!-- Placeholder for "Used in" -->

Parameters
----------
arg1, arg2 : dtype_like
    dtype or string representing a typecode.

Returns
-------
out : bool

See Also
--------
issubsctype, issubclass_
numpy.core.numerictypes : Overview of numpy type hierarchy.

Examples
--------
>>> np.issubdtype('S1', np.string_)
True
>>> np.issubdtype(np.float64, np.float32)
False