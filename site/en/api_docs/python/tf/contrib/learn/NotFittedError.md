


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.learn.NotFittedError

### `class tf.contrib.learn.NotFittedError`

Exception class to raise if estimator is used before fitting.

This class inherits from both ValueError and AttributeError to help with
exception handling and backward compatibility.

Examples:
>>> from sklearn.svm import LinearSVC
>>> from sklearn.exceptions import NotFittedError
>>> try:
...     LinearSVC().predict([[1, 2], [2, 3], [3, 4]])
... except NotFittedError as e:
...     print(repr(e))
...                        # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
NotFittedError('This LinearSVC instance is not fitted yet',)

Copied from
https://github.com/scikit-learn/scikit-learn/master/sklearn/exceptions.py

## Class Members

<h3 id="__init__"><code>__init__</code></h3>

<h3 id="args"><code>args</code></h3>

<h3 id="message"><code>message</code></h3>



Defined in [`tensorflow/contrib/learn/python/learn/estimators/_sklearn.py`](https://www.tensorflow.org/code/tensorflow/contrib/learn/python/learn/estimators/_sklearn.py).

