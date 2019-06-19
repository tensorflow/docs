page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.compute_gradient

``` python
tf.test.compute_gradient(
    x,
    x_shape,
    y,
    y_shape,
    x_init_value=None,
    delta=0.001,
    init_targets=None,
    extra_feed_dict=None
)
```



Defined in [`tensorflow/python/ops/gradient_checker.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/gradient_checker.py).

See the guide: [Testing > Gradient checking](../../../../api_guides/python/test#Gradient_checking)

Computes and returns the theoretical and numerical Jacobian.

If `x` or `y` is complex, the Jacobian will still be real but the
corresponding Jacobian dimension(s) will be twice as large.  This is required
even if both input and output is complex since TensorFlow graphs are not
necessarily holomorphic, and may have gradients not expressible as complex
numbers.  For example, if `x` is complex with shape `[m]` and `y` is complex
with shape `[n]`, each Jacobian `J` will have shape `[m * 2, n * 2]` with

    J[::2, ::2] = d(Re y)/d(Re x)
    J[::2, 1::2] = d(Im y)/d(Re x)
    J[1::2, ::2] = d(Re y)/d(Im x)
    J[1::2, 1::2] = d(Im y)/d(Im x)

#### Args:

* <b>`x`</b>: a tensor or list of tensors
* <b>`x_shape`</b>: the dimensions of x as a tuple or an array of ints. If x is a list,
  then this is the list of shapes.
* <b>`y`</b>: a tensor
* <b>`y_shape`</b>: the dimensions of y as a tuple or an array of ints.
* <b>`x_init_value`</b>: (optional) a numpy array of the same shape as "x"
    representing the initial value of x. If x is a list, this should be a list
    of numpy arrays.  If this is none, the function will pick a random tensor
    as the initial value.
* <b>`delta`</b>: (optional) the amount of perturbation.
* <b>`init_targets`</b>: list of targets to run to initialize model params.
    TODO(mrry): remove this argument.
* <b>`extra_feed_dict`</b>: dict that allows fixing specified tensor values
    during the Jacobian calculation.


#### Returns:

Two 2-d numpy arrays representing the theoretical and numerical
Jacobian for dy/dx. Each has "x_size" rows and "y_size" columns
where "x_size" is the number of elements in x and "y_size" is the
number of elements in y. If x is a list, returns a list of two numpy arrays.