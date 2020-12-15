description: Returns a iterator for reading Event protocol buffers from an event file.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.summary_iterator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.summary_iterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/summary/summary_iterator.py#L43-L95">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a iterator for reading `Event` protocol buffers from an event file.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.summary_iterator(
    path
)
</code></pre>



<!-- Placeholder for "Used in" -->

You can use this function to read events written to an event file. It returns
a Python iterator that yields `Event` protocol buffers.

Example: Print the contents of an events file.

```python
for e in tf.compat.v1.train.summary_iterator(path to events file):
    print(e)
```

Example: Print selected summary values.

```python
# This example supposes that the events file contains summaries with a
# summary value tag 'loss'.  These could have been added by calling
# `add_summary()`, passing the output of a scalar summary op created with
# with: `tf.compat.v1.summary.scalar('loss', loss_tensor)`.
for e in tf.compat.v1.train.summary_iterator(path to events file):
    for v in e.summary.value:
        if v.tag == 'loss':
            print(v.simple_value)
```
Example: Continuously check for new summary values.

```python
summaries = tf.compat.v1.train.summary_iterator(path to events file)
while True:
  for e in summaries:
      for v in e.summary.value:
          if v.tag == 'loss':
              print(v.simple_value)
  # Wait for a bit before checking the file for any new events
  time.sleep(wait time)
```

See the protocol buffer definitions of
[Event](https://www.tensorflow.org/code/tensorflow/core/util/event.proto)
and
[Summary](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
for more information about their attributes.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`path`
</td>
<td>
The path to an event file created by a `SummaryWriter`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A iterator that yields `Event` protocol buffers
</td>
</tr>

</table>

