page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.unsorted_segment_join


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/strings/unsorted_segment_join">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_string_ops.py`



Joins the elements of `inputs` based on `segment_ids`.

### Aliases:

* <a href="/api_docs/python/tf/strings/unsorted_segment_join"><code>tf.compat.v1.strings.unsorted_segment_join</code></a>
* <a href="/api_docs/python/tf/strings/unsorted_segment_join"><code>tf.compat.v2.strings.unsorted_segment_join</code></a>


``` python
tf.strings.unsorted_segment_join(
    inputs,
    segment_ids,
    num_segments,
    separator='',
    name=None
)
```



<!-- Placeholder for "Used in" -->

Computes the string join along segments of a tensor.
Given `segment_ids` with rank `N` and `data` with rank `N+M`:

    `output[i, k1...kM] = strings.join([data[j1...jN, k1...kM])`

where the join is over all [j1...jN] such that segment_ids[j1...jN] = i.
Strings are joined in row-major order.

#### For example:



```python
inputs = [['Y', 'q', 'c'], ['Y', '6', '6'], ['p', 'G', 'a']]
output_array = string_ops.unsorted_segment_join(inputs=inputs,
                                                segment_ids=[1, 0, 1],
                                                num_segments=2,
                                                separator=':'))
# output_array ==> [['Y', '6', '6'], ['Y:p', 'q:G', 'c:a']]


inputs = ['this', 'is', 'a', 'test']
output_array = string_ops.unsorted_segment_join(inputs=inputs,
                                                segment_ids=[0, 0, 0, 0],
                                                num_segments=1,
                                                separator=':'))
# output_array ==> ['this:is:a:test']
```

#### Args:


* <b>`inputs`</b>: A `Tensor` of type `string`. The input to be joined.
* <b>`segment_ids`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  A tensor whose shape is a prefix of data.shape.  Negative segment ids are not
  supported.
* <b>`num_segments`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  A scalar.
* <b>`separator`</b>: An optional `string`. Defaults to `""`.
  The separator to use when joining.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
