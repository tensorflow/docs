description: Enum defining the optimizations to apply when generating tflite graphs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lite.Optimize" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="DEFAULT"/>
<meta itemprop="property" content="OPTIMIZE_FOR_LATENCY"/>
<meta itemprop="property" content="OPTIMIZE_FOR_SIZE"/>
</div>

# tf.lite.Optimize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/lite/python/lite.py#L91-L130">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enum defining the optimizations to apply when generating tflite graphs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.lite.Optimize`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

Some optimizations may come at the cost of accuracy.

DEFAULT
    Default optimization strategy.

    Converter will do its best to improve size and latency based on the
    information provided.
    Enhanced optimizations are gained by providing a representative_dataset.
    This is recommended, and is currently equivalent to the modes below.
    Currently, weights will be quantized and if representative_dataset is
    provided, activations for quantizable operations will also be quantized.

OPTIMIZE_FOR_SIZE
    Deprecated. Does the same as DEFAULT.

OPTIMIZE_FOR_LATENCY
    Deprecated. Does the same as DEFAULT.

## Class Variables

* `DEFAULT` <a id="DEFAULT"></a>
* `OPTIMIZE_FOR_LATENCY` <a id="OPTIMIZE_FOR_LATENCY"></a>
* `OPTIMIZE_FOR_SIZE` <a id="OPTIMIZE_FOR_SIZE"></a>
