description: Raised when a flag is unrecognized.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.UnrecognizedFlagError" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.compat.v1.flags.UnrecognizedFlagError

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Raised when a flag is unrecognized.

Inherits From: [`Error`](../../../../tf/compat/v1/flags/Error.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.UnrecognizedFlagError`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.UnrecognizedFlagError(
    flagname, flagvalue='', suggestions=None
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`flagname`
</td>
<td>
str, the name of the unrecognized flag.
</td>
</tr><tr>
<td>
`flagvalue`
</td>
<td>
The value of the flag, empty if the flag is not defined.
</td>
</tr>
</table>



