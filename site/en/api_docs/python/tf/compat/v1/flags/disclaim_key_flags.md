description: Declares that the current module will not define any more key flags.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.disclaim_key_flags" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.disclaim_key_flags

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Declares that the current module will not define any more key flags.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.disclaim_key_flags`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.disclaim_key_flags()
</code></pre>



<!-- Placeholder for "Used in" -->

Normally, the module that calls the DEFINE_xxx functions claims the
flag to be its key flag.  This is undesirable for modules that
define additional DEFINE_yyy functions with its own flag parsers and
serializers, since that module will accidentally claim flags defined
by DEFINE_yyy as its key flags.  After calling this function, the
module disclaims flag definitions thereafter, so the key flags will
be correctly attributed to the caller of DEFINE_yyy.

After calling this function, the module will not be able to define
any more flags.  This function will affect all FlagValues objects.