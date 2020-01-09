page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.path_to_str


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/compat.py#L128-L164">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts input which is a `PathLike` object to `str` type.

### Aliases:

* `tf.compat.v1.compat.path_to_str`
* `tf.compat.v2.compat.path_to_str`


``` python
tf.compat.path_to_str(path)
```



<!-- Placeholder for "Used in" -->

Converts from any python constant representation of a `PathLike` object to
a string. If the input is not a `PathLike` object, simply returns the input.

#### Args:


* <b>`path`</b>: An object that can be converted to path representation.


#### Returns:

A `str` object.



#### Usage:

In case a simplified `str` version of the path is needed from an
`os.PathLike` object



#### Examples:


```python3
>>> tf.compat.path_to_str('C:\XYZ\tensorflow\./.././tensorflow')
'C:\XYZ\tensorflow\./.././tensorflow' # Windows OS
>>> tf.compat.path_to_str(Path('C:\XYZ\tensorflow\./.././tensorflow'))
'C:\XYZ\tensorflow\..\tensorflow' # Windows OS
>>> tf.compat.path_to_str(Path('./corpus'))
'corpus' # Linux OS
>>> tf.compat.path_to_str('./.././Corpus')
'./.././Corpus' # Linux OS
>>> tf.compat.path_to_str(Path('./.././Corpus'))
'../Corpus' # Linux OS
>>> tf.compat.path_to_str(Path('./..////../'))
'../..' # Linux OS

```
