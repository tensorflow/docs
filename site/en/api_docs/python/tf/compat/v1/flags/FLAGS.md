description: Registry of 'Flag' objects.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.FLAGS" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.FLAGS

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Registry of 'Flag' objects.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.FLAGS`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.FLAGS(
    *args, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

A 'FlagValues' can then scan command line arguments, passing flag
arguments through to the 'Flag' objects that it owns.  It also
provides easy access to the flag values.  Typically only one
'FlagValues' object is needed by an application: flags.FLAGS

This class is heavily overloaded:

'Flag' objects are registered via __setitem__:
     FLAGS['longname'] = x   # register a new flag

The .value attribute of the registered 'Flag' objects can be accessed
as attributes of this 'FlagValues' object, through __getattr__.  Both
the long and short name of the original 'Flag' objects can be used to
access its value:
     FLAGS.longname          # parsed flag value
     FLAGS.x                 # parsed flag value (short name)

Command line arguments are scanned and passed to the registered 'Flag'
objects through the __call__ method.  Unparsed arguments, including
argv[0] (e.g. the program name) are returned.
     argv = FLAGS(sys.argv)  # scan command line arguments

The original registered Flag objects can be retrieved through the use
of the dictionary-like operator, __getitem__:
     x = FLAGS['longname']   # access the registered Flag object

The str() operator of a 'FlagValues' object provides help for all of
the registered 'Flag' objects.