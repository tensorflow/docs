description: Structure to create or gather pieces commonly needed to train a model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.Scaffold" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="default_local_init_op"/>
<meta itemprop="property" content="finalize"/>
<meta itemprop="property" content="get_or_default"/>
</div>

# tf.compat.v1.train.Scaffold

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/monitored_session.py#L59-L318">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Structure to create or gather pieces commonly needed to train a model.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.Scaffold(
    init_op=None, init_feed_dict=None, init_fn=None, ready_op=None,
    ready_for_local_init_op=None, local_init_op=None, summary_op=None, saver=None,
    copy_from_scaffold=None, local_init_feed_dict=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

When you build a model for training you usually need ops to initialize
variables, a `Saver` to checkpoint them, an op to collect summaries for
the visualizer, and so on.

Various libraries built on top of the core TensorFlow library take care of
creating some or all of these pieces and storing them in well known
collections in the graph.  The `Scaffold` class helps pick these pieces from
the graph collections, creating and adding them to the collections if needed.

If you call the scaffold constructor without any arguments, it will pick
pieces from the collections, creating default ones if needed when
`scaffold.finalize()` is called.  You can pass arguments to the constructor to
provide your own pieces.  Pieces that you pass to the constructor are not
added to the graph collections.

The following pieces are directly accessible as attributes of the `Scaffold`
object:

* `saver`: A <a href="../../../../tf/compat/v1/train/Saver.md"><code>tf.compat.v1.train.Saver</code></a> object taking care of saving the
variables.
  Picked from and stored into the `SAVERS` collection in the graph by default.
* `init_op`: An op to run to initialize the variables.  Picked from and
  stored into the `INIT_OP` collection in the graph by default.
* `ready_op`: An op to verify that the variables are initialized.  Picked
  from and stored into the `READY_OP` collection in the graph by default.
* `ready_for_local_init_op`: An op to verify that global state has been
  initialized and it is alright to run `local_init_op`.  Picked from and
  stored into the `READY_FOR_LOCAL_INIT_OP` collection in the graph by
  default. This is needed when the initialization of local variables depends
  on the values of global variables.
* `local_init_op`: An op to initialize the local variables.  Picked
  from and stored into the `LOCAL_INIT_OP` collection in the graph by default.
* `summary_op`: An op to run and merge the summaries in the graph.  Picked
  from and stored into the `SUMMARY_OP` collection in the graph by default.

You can also pass the following additional pieces to the constructor:

* `init_feed_dict`: A session feed dictionary that should be used when
   running the init op.
* `init_fn`: A callable to run after the init op to perform additional
  initializations.  The callable will be called as
  `init_fn(scaffold, session)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`init_op`
</td>
<td>
Optional op for initializing variables.
</td>
</tr><tr>
<td>
`init_feed_dict`
</td>
<td>
Optional session feed dictionary to use when running the
init_op.
</td>
</tr><tr>
<td>
`init_fn`
</td>
<td>
Optional function to use to initialize the model after running
the init_op.  Will be called as `init_fn(scaffold, session)`.
</td>
</tr><tr>
<td>
`ready_op`
</td>
<td>
Optional op to verify that the variables are initialized.  Must
return an empty 1D string tensor when the variables are initialized, or
a non-empty 1D string tensor listing the names of the non-initialized
variables.
</td>
</tr><tr>
<td>
`ready_for_local_init_op`
</td>
<td>
Optional op to verify that the global variables
are initialized and `local_init_op` can be run. Must return an empty 1D
string tensor when the global variables are initialized, or a non-empty
1D string tensor listing the names of the non-initialized global
variables.
</td>
</tr><tr>
<td>
`local_init_op`
</td>
<td>
Optional op to initialize local variables.
</td>
</tr><tr>
<td>
`summary_op`
</td>
<td>
Optional op to gather all summaries.  Must return a scalar
string tensor containing a serialized `Summary` proto.
</td>
</tr><tr>
<td>
`saver`
</td>
<td>
Optional <a href="../../../../tf/compat/v1/train/Saver.md"><code>tf.compat.v1.train.Saver</code></a> object to use to save and
restore variables.  May also be a <a href="../../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> object, in which
case object-based checkpoints are saved. This will also load some
object-based checkpoints saved from elsewhere, but that loading may be
fragile since it uses fixed keys rather than performing a full
graph-based match. For example if a variable has two paths from the
`Checkpoint` object because two `Model` objects share the `Layer` object
that owns it, removing one `Model` may change the keys and break
checkpoint loading through this API, whereas a graph-based match would
match the variable through the other `Model`.
</td>
</tr><tr>
<td>
`copy_from_scaffold`
</td>
<td>
Optional scaffold object to copy fields from. Its
fields will be overwritten by the provided fields in this function.
</td>
</tr><tr>
<td>
`local_init_feed_dict`
</td>
<td>
Optional session feed dictionary to use when running
the local_init_op.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`init_feed_dict`
</td>
<td>

</td>
</tr><tr>
<td>
`init_fn`
</td>
<td>

</td>
</tr><tr>
<td>
`init_op`
</td>
<td>

</td>
</tr><tr>
<td>
`local_init_feed_dict`
</td>
<td>

</td>
</tr><tr>
<td>
`local_init_op`
</td>
<td>

</td>
</tr><tr>
<td>
`ready_for_local_init_op`
</td>
<td>

</td>
</tr><tr>
<td>
`ready_op`
</td>
<td>

</td>
</tr><tr>
<td>
`saver`
</td>
<td>

</td>
</tr><tr>
<td>
`summary_op`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="default_local_init_op"><code>default_local_init_op</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/monitored_session.py#L302-L318">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>default_local_init_op()
</code></pre>

Returns an op that groups the default local init ops.

This op is used during session initialization when a Scaffold is
initialized without specifying the local_init_op arg. It includes
<a href="../../../../tf/compat/v1/local_variables_initializer.md"><code>tf.compat.v1.local_variables_initializer</code></a>,
<a href="../../../../tf/compat/v1/tables_initializer.md"><code>tf.compat.v1.tables_initializer</code></a>, and also
initializes local session resources.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The default Scaffold local init op.
</td>
</tr>

</table>



<h3 id="finalize"><code>finalize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/monitored_session.py#L190-L247">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>finalize()
</code></pre>

Creates operations if needed and finalizes the graph.


<h3 id="get_or_default"><code>get_or_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/monitored_session.py#L285-L300">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>get_or_default(
    arg_name, collection_key, default_constructor
)
</code></pre>

Get from cache or create a default operation.




