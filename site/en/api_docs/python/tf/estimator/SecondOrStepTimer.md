description: Timer that triggers at most once every N seconds or once every N steps.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.SecondOrStepTimer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="last_triggered_step"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="should_trigger_for_step"/>
<meta itemprop="property" content="update_last_triggered_step"/>
</div>

# tf.estimator.SecondOrStepTimer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/basic_session_run_hooks.py#L91-L155">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Timer that triggers at most once every N seconds or once every N steps.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.SecondOrStepTimer`, `tf.compat.v1.train.SecondOrStepTimer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.SecondOrStepTimer(
    every_secs=None, every_steps=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This symbol is also exported to v2 in tf.estimator namespace. See
https://github.com/tensorflow/estimator/blob/master/tensorflow_estimator/python/estimator/hooks/basic_session_run_hooks.py

## Methods

<h3 id="last_triggered_step"><code>last_triggered_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/basic_session_run_hooks.py#L154-L155">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>last_triggered_step()
</code></pre>

Returns the last triggered time step or None if never triggered.


<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/basic_session_run_hooks.py#L110-L112">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset()
</code></pre>

Resets the timer.


<h3 id="should_trigger_for_step"><code>should_trigger_for_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/basic_session_run_hooks.py#L114-L139">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>should_trigger_for_step(
    step
)
</code></pre>

Return true if the timer should trigger for the specified step.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`step`
</td>
<td>
Training step to trigger on.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
True if the difference between the current time and the time of the last
trigger exceeds `every_secs`, or if the difference between the current
step and the last triggered step exceeds `every_steps`. False otherwise.
</td>
</tr>

</table>



<h3 id="update_last_triggered_step"><code>update_last_triggered_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/basic_session_run_hooks.py#L141-L152">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_last_triggered_step(
    step
)
</code></pre>

Update the last triggered time and step number.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`step`
</td>
<td>
The current step.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A pair `(elapsed_time, elapsed_steps)`, where `elapsed_time` is the number
of seconds between the current trigger and the last one (a float), and
`elapsed_steps` is the number of steps between the current trigger and
the last one. Both values will be set to `None` on the first trigger.
</td>
</tr>

</table>





