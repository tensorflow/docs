description: Returns whether TensorFlow can access a GPU. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.test.is_gpu_available" />
<meta itemprop="path" content="Stable" />
</div>

# tf.test.is_gpu_available

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/test_util.py#L1547-L1597">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns whether TensorFlow can access a GPU. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.test.is_gpu_available`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.test.is_gpu_available(
    cuda_only=(False), min_cuda_compute_capability=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.config.list_physical_devices('GPU')` instead.

Warning: if a non-GPU version of the package is installed, the function would
also return False. Use <a href="../../tf/test/is_built_with_cuda.md"><code>tf.test.is_built_with_cuda</code></a> to validate if TensorFlow
was build with CUDA support.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cuda_only`
</td>
<td>
limit the search to CUDA GPUs.
</td>
</tr><tr>
<td>
`min_cuda_compute_capability`
</td>
<td>
a (major,minor) pair that indicates the minimum
CUDA compute capability required, or None if no requirement.
</td>
</tr>
</table>


Note that the keyword arg name "cuda_only" is misleading (since routine will
return true when a GPU device is available irrespective of whether TF was
built with CUDA support or ROCm support. However no changes here because

++ Changing the name "cuda_only" to something more generic would break
   backward compatibility

++ Adding an equivalent "rocm_only" would require the implementation check
   the build type. This in turn would require doing the same for CUDA and thus
   potentially break backward compatibility

++ Adding a new "cuda_or_rocm_only" would not break backward compatibility,
   but would require most (if not all) callers to update the call to use
   "cuda_or_rocm_only" instead of "cuda_only"

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
True if a GPU device of the requested kind is available.
</td>
</tr>

</table>

