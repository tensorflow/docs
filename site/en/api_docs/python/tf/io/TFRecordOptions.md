page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.TFRecordOptions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L44-L150">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TFRecordOptions`

Options used for manipulating TFRecord files.



### Aliases:

* Class `tf.compat.v1.io.TFRecordOptions`
* Class `tf.compat.v1.python_io.TFRecordOptions`
* Class `tf.compat.v2.io.TFRecordOptions`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L52-L100">View source</a>

``` python
__init__(
    compression_type=None,
    flush_mode=None,
    input_buffer_size=None,
    output_buffer_size=None,
    window_bits=None,
    compression_level=None,
    compression_method=None,
    mem_level=None,
    compression_strategy=None
)
```

Creates a `TFRecordOptions` instance.

Options only effect TFRecordWriter when compression_type is not `None`.
Documentation, details, and defaults can be found in
[`zlib_compression_options.h`](https://www.tensorflow.org/code/tensorflow/core/lib/io/zlib_compression_options.h)
and in the [zlib manual](http://www.zlib.net/manual.html).
Leaving an option as `None` allows C++ to set a reasonable default.

#### Args:


* <b>`compression_type`</b>: `"GZIP"`, `"ZLIB"`, or `""` (no compression).
* <b>`flush_mode`</b>: flush mode or `None`, Default: Z_NO_FLUSH.
* <b>`input_buffer_size`</b>: int or `None`.
* <b>`output_buffer_size`</b>: int or `None`.
* <b>`window_bits`</b>: int or `None`.
* <b>`compression_level`</b>: 0 to 9, or `None`.
* <b>`compression_method`</b>: compression method or `None`.
* <b>`mem_level`</b>: 1 to 9, or `None`.
* <b>`compression_strategy`</b>: strategy or `None`. Default: Z_DEFAULT_STRATEGY.


#### Returns:

A `TFRecordOptions` object.



#### Raises:


* <b>`ValueError`</b>: If compression_type is invalid.



## Methods

<h3 id="get_compression_type_string"><code>get_compression_type_string</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L102-L126">View source</a>

``` python
@classmethod
get_compression_type_string(
    cls,
    options
)
```

Convert various option types to a unified string.


#### Args:


* <b>`options`</b>: `TFRecordOption`, `TFRecordCompressionType`, or string.


#### Returns:

Compression type as string (e.g. `'ZLIB'`, `'GZIP'`, or `''`).



#### Raises:


* <b>`ValueError`</b>: If compression_type is invalid.



## Class Members

* `compression_type_map` <a id="compression_type_map"></a>
