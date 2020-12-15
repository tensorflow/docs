description: Get a dictionary describing TensorFlow's build environment.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sysconfig.get_build_info" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sysconfig.get_build_info

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/platform/sysconfig.py#L90-L112">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get a dictionary describing TensorFlow's build environment.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sysconfig.get_build_info`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sysconfig.get_build_info()
</code></pre>



<!-- Placeholder for "Used in" -->

Values are generated when TensorFlow is compiled, and are static for each
TensorFlow package. The return value is a dictionary with string keys such as:

  - cuda_version
  - cudnn_version
  - is_cuda_build
  - is_rocm_build
  - msvcp_dll_names
  - nvcuda_dll_name
  - cudart_dll_name
  - cudnn_dll_name

Note that the actual keys and values returned by this function is subject to
change across different versions of TensorFlow or across platforms.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Dictionary describing TensorFlow's build environment.
</td>
</tr>

</table>

