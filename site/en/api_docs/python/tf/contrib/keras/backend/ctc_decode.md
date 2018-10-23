

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.ctc_decode

### `tf.contrib.keras.backend.ctc_decode`

``` python
ctc_decode(
    y_pred,
    input_length,
    greedy=True,
    beam_width=100,
    top_paths=1
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Decodes the output of a softmax.

Can use either greedy search (also known as best path)
or a constrained dictionary search.

#### Arguments:

    y_pred: tensor `(samples, time_steps, num_categories)`
        containing the prediction, or output of the softmax.
    input_length: tensor `(samples, )` containing the sequence length for
        each batch item in `y_pred`.
    greedy: perform much faster best-path search if `true`.
        This does not use a dictionary.
    beam_width: if `greedy` is `false`: a beam search decoder will be used
        with a beam of this width.
    top_paths: if `greedy` is `false`,
        how many of the most probable paths will be returned.


#### Returns:

    Tuple:
        List: if `greedy` is `true`, returns a list of one element that
            contains the decoded sequence.
            If `false`, returns the `top_paths` most probable
            decoded sequences.
            Important: blank labels are returned as `-1`.
        Tensor `(top_paths, )` that contains
            the log probability of each decoded sequence.