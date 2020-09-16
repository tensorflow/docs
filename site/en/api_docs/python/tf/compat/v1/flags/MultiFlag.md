description: A flag that can appear multiple time on the command-line.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.MultiFlag" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__ge__"/>
<meta itemprop="property" content="__gt__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__le__"/>
<meta itemprop="property" content="__lt__"/>
<meta itemprop="property" content="flag_type"/>
<meta itemprop="property" content="parse"/>
<meta itemprop="property" content="serialize"/>
<meta itemprop="property" content="unparse"/>
</div>

# tf.compat.v1.flags.MultiFlag

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A flag that can appear multiple time on the command-line.

Inherits From: [`Flag`](../../../../tf/compat/v1/flags/Flag.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.MultiFlag`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.MultiFlag(
    *args, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

The value of such a flag is a list that contains the individual values
from all the appearances of that flag on the command-line.

See the __doc__ for Flag for most behavior of this class.  Only
differences in behavior are described here:

  * The default value may be either a single value or an iterable of values.
    A single value is transformed into a single-item list of that value.

  * The value of the flag is always a list, even if the option was
    only supplied once, and even if the default value is a single
    value



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="flag_type"><code>flag_type</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flag_type()
</code></pre>

See base class.


<h3 id="parse"><code>parse</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>parse(
    arguments
)
</code></pre>

Parses one or more arguments with the installed parser.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`arguments`
</td>
<td>
a single argument or a list of arguments (typically a
list of default values); a single argument is converted
internally into a list containing one item.
</td>
</tr>
</table>



<h3 id="serialize"><code>serialize</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>serialize()
</code></pre>

Serializes the flag.


<h3 id="unparse"><code>unparse</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>unparse()
</code></pre>




<h3 id="__eq__"><code>__eq__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__ge__"><code>__ge__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ge__(
    other, NotImplemented=NotImplemented
)
</code></pre>

Return a >= b.  Computed by @total_ordering from (not a < b).


<h3 id="__gt__"><code>__gt__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__gt__(
    other, NotImplemented=NotImplemented
)
</code></pre>

Return a > b.  Computed by @total_ordering from (not a < b) and (a != b).


<h3 id="__le__"><code>__le__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__le__(
    other, NotImplemented=NotImplemented
)
</code></pre>

Return a <= b.  Computed by @total_ordering from (a < b) or (a == b).


<h3 id="__lt__"><code>__lt__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__lt__(
    other
)
</code></pre>

Return self<value.




