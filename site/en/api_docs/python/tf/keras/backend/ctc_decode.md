page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ctc_decode

Decodes the output of a softmax.

### Aliases:

* `tf.compat.v1.keras.backend.ctc_decode`
* `tf.compat.v2.keras.backend.ctc_decode`
* `tf.keras.backend.ctc_decode`

``` python
tf.keras.backend.ctc_decode(
    y_pred,
    input_length,
    greedy=True,
    beam_width=100,
    top_paths=1
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

Can use either greedy search (also known as best path)
or a constrained dictionary search.

#### Arguments:


* <b>`y_pred`</b>: tensor `(samples, time_steps, num_categories)`
    containing the prediction, or output of the softmax.
* <b>`input_length`</b>: tensor `(samples, )` containing the sequence length for
    each batch item in `y_pred`.
* <b>`greedy`</b>: perform much faster best-path search if `true`.
    This does not use a dictionary.
* <b>`beam_width`</b>: if `greedy` is `false`: a beam search decoder will be used
    with a beam of this width.
* <b>`top_paths`</b>: if `greedy` is `false`,
    how many of the most probable paths will be returned.


#### Returns:


* <b>`Tuple`</b>:     List: if `greedy` is `true`, returns a list of one element that
        contains the decoded sequence.
        If `false`, returns the `top_paths` most probable
        decoded sequences.
        Important: blank labels are returned as `-1`.
    Tensor `(top_paths, )` that contains
        the log probability of each decoded sequence.