description: A ProtocolMessage

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.SessionLog" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="CHECKPOINT"/>
<meta itemprop="property" content="START"/>
<meta itemprop="property" content="STATUS_UNSPECIFIED"/>
<meta itemprop="property" content="STOP"/>
<meta itemprop="property" content="SessionStatus"/>
</div>

# tf.compat.v1.SessionLog

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/core/util/event.proto">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A ProtocolMessage

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.summary.SessionLog`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`checkpoint_path`
</td>
<td>
`string checkpoint_path`
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
`string msg`
</td>
</tr><tr>
<td>
`status`
</td>
<td>
`SessionStatus status`
</td>
</tr>
</table>



## Class Variables

* `CHECKPOINT = 3` <a id="CHECKPOINT"></a>
* `START = 1` <a id="START"></a>
* `STATUS_UNSPECIFIED = 0` <a id="STATUS_UNSPECIFIED"></a>
* `STOP = 2` <a id="STOP"></a>
* `SessionStatus` <a id="SessionStatus"></a>
