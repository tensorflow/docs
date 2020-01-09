page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.text_wrap


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Wraps a given text to a maximum line length and returns it.

### Aliases:

* `tf.compat.v1.app.flags.text_wrap`


``` python
tf.compat.v1.flags.text_wrap(
    text,
    length=None,
    indent='',
    firstline_indent=None
)
```



<!-- Placeholder for "Used in" -->

It turns lines that only contain whitespace into empty lines, keeps new lines,
and expands tabs using 4 spaces.

#### Args:


* <b>`text`</b>: str, text to wrap.
* <b>`length`</b>: int, maximum length of a line, includes indentation.
    If this is None then use get_help_width()
* <b>`indent`</b>: str, indent for all but first line.
* <b>`firstline_indent`</b>: str, indent for first line; if None, fall back to indent.


#### Returns:

str, the wrapped text.



#### Raises:


* <b>`ValueError`</b>: Raised if indent or firstline_indent not shorter than length.
