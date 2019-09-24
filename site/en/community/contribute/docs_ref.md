# Contribute to the TensorFlow API documentation

## Testable docstrings

TensorFlow uses [DocTest](https://docs.python.org/3/library/doctest.html) to
test the Python docstrings. The snippet in the docstring has to be executable
Python code. To enable testing, use the `>>>` (carets) in front of the code so
that doctest can recognize it as a test and execute it. For example,

```
def concat():
  """Docstring for concat.

  Example usage:

  >>> t1 = [[[1, 2], [2, 3]], [[4, 4], [5, 3]]]
  >>> t2 = [[[7, 4], [8, 4]], [[2,10], [15, 11]]]
  >>> concat([t1, t2], -1)
  <tf.Tensor: id=..., shape=(2, 2, 4), dtype=int32, numpy= array([[[1, 2, 7, 4], [2, 3, 8, 4]], [[4, 4, 2, 10], [5, 3, 15, 11]]], dtype=int32)>
  """

  <code here>
```

Currently, lots of code uses backticks (```) to identify code. To make the code
testable with DocTest:

*   Remove the backticks (```) and use the carets (>>>) in front of each line.
    Use (...) in front of continued lines.

*   (```) can still be used for non-python code or code that cannot be tested
    for some reason.

### Docstring considerations

*   **Output format**: The output of the snippet needs to be directly beneath
    the code that’s generating the output. Also, the output in the docstring has
    to be exactly equal to what the output would be after the code is executed.
    See the above example. Also, check out
    [this part](https://docs.python.org/3/library/doctest.html#warnings) in the
    doctest documentation. If the output exceeds the 80 line limit, you can put
    the extra output on the new line and doctest will recognize it. See
    multi-line blocks below for the input.

*   **Globals**: The `tf`, `np` and `os` modules are always available in
    TensorFlow's doctest.

*   **Using symbols**: In doctest you can directly access symbols defined in the
    same file. To use a symbol that’s not defined in the current file, please
    use TensorFlow’s public API `tf.xxx` instead of `xxx`. As you can see in the
    example below, `random.normal` is accessed via `tf.random.normal`. This is
    because `random.normal` is not visible in `NewLayer`.

    ```
    def NewLayer():
      “””This layer does cool stuff.

      Example usage:

      >>> x = tf.random.normal((1, 28, 28, 3))
      >>> new_layer = NewLayer(x)
      >>> new_layer
      <tf.Tensor id=52, shape=(1, 14, 14, 3), dtype=int32, numpy=...>
      “””
    ```

*   **Non-deterministic output**: Use ellipsis(`...`) for the uncertain parts
    and doctest will ignore that substring.

    ```
    >>> x = tf.random.normal((1,))
    >>> print(x)
    <tf.Tensor: id=26, shape=(1,), dtype=float32, numpy=..., dtype=float32)>
    ```

*   **Multi-line blocks**: Doctest is strict about the difference between a
    single and a multi-line statement. Note the usage of (...) below:

    ```
    >>> if x > 0:
    ... print("X is positive")
    >>> model.compile(
    ... loss="mse",
    ... optimizer="adam")
    ```

*   **Exceptions**: Exception details are ignored except the Exception that’s
    raised. See
    [this](https://docs.python.org/3/library/doctest.html#doctest.IGNORE_EXCEPTION_DETAIL)
    for more details.

    ```
    >>> np_var = np.array([1, 2])
    >>> tf.keras.backend.is_keras_tensor(np_var)
    Traceback (most recent call last):
    ...
    ValueError: Unexpectedly found an instance of type `<class 'numpy.ndarray'>`.
    ```
