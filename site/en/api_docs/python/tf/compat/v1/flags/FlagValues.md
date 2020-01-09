page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.FlagValues


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



## Class `FlagValues`

Registry of 'Flag' objects.



### Aliases:

* Class `tf.compat.v1.app.flags.FlagValues`


<!-- Placeholder for "Used in" -->

A 'FlagValues' can then scan command line arguments, passing flag
arguments through to the 'Flag' objects that it owns.  It also
provides easy access to the flag values.  Typically only one
'FlagValues' object is needed by an application: flags.FLAGS

This class is heavily overloaded:

'Flag' objects are registered via __setitem__:
     FLAGS['longname'] = x   # register a new flag

The .value attribute of the registered 'Flag' objects can be accessed
as attributes of this 'FlagValues' object, through __getattr__.  Both
the long and short name of the original 'Flag' objects can be used to
access its value:
     FLAGS.longname          # parsed flag value
     FLAGS.x                 # parsed flag value (short name)

Command line arguments are scanned and passed to the registered 'Flag'
objects through the __call__ method.  Unparsed arguments, including
argv[0] (e.g. the program name) are returned.
     argv = FLAGS(sys.argv)  # scan command line arguments

The original registered Flag objects can be retrieved through the use
of the dictionary-like operator, __getitem__:
     x = FLAGS['longname']   # access the registered Flag object

The str() operator of a 'FlagValues' object provides help for all of
the registered 'Flag' objects.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    argv,
    known_only=False
)
```

Parses flags from argv; stores parsed flags into this FlagValues object.

All unparsed arguments are returned.

#### Args:


* <b>`argv`</b>: a tuple/list of strings.
* <b>`known_only`</b>: bool, if True, parse and remove known flags; return the rest
    untouched. Unknown flags specified by --undefok are not returned.


#### Returns:

The list of arguments not parsed as options, including argv[0].



#### Raises:


* <b>`Error`</b>: Raised on any parsing error.
* <b>`TypeError`</b>: Raised on passing wrong type of arguments.
* <b>`ValueError`</b>: Raised on flag value parsing error.

<h3 id="__contains__"><code>__contains__</code></h3>

``` python
__contains__(name)
```

Returns True if name is a value (flag) in the dict.


<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(name)
```

Returns the Flag object for the flag --name.


<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```




<h3 id="__len__"><code>__len__</code></h3>

``` python
__len__()
```




<h3 id="append_flag_values"><code>append_flag_values</code></h3>

``` python
append_flag_values(flag_values)
```

Appends flags registered in another FlagValues instance.


#### Args:


* <b>`flag_values`</b>: FlagValues, the FlagValues instance from which to copy flags.

<h3 id="append_flags_into_file"><code>append_flags_into_file</code></h3>

``` python
append_flags_into_file(filename)
```

Appends all flags assignments from this FlagInfo object to a file.

Output will be in the format of a flagfile.

NOTE: MUST mirror the behavior of the C++ AppendFlagsIntoFile
from https://github.com/gflags/gflags.

#### Args:


* <b>`filename`</b>: str, name of the file.

<h3 id="find_module_defining_flag"><code>find_module_defining_flag</code></h3>

``` python
find_module_defining_flag(
    flagname,
    default=None
)
```

Return the name of the module defining this flag, or default.


#### Args:


* <b>`flagname`</b>: str, name of the flag to lookup.
* <b>`default`</b>: Value to return if flagname is not defined. Defaults
    to None.


#### Returns:

The name of the module which registered the flag with this name.
If no such module exists (i.e. no flag with this name exists),
we return default.


<h3 id="find_module_id_defining_flag"><code>find_module_id_defining_flag</code></h3>

``` python
find_module_id_defining_flag(
    flagname,
    default=None
)
```

Return the ID of the module defining this flag, or default.


#### Args:


* <b>`flagname`</b>: str, name of the flag to lookup.
* <b>`default`</b>: Value to return if flagname is not defined. Defaults
    to None.


#### Returns:

The ID of the module which registered the flag with this name.
If no such module exists (i.e. no flag with this name exists),
we return default.


<h3 id="flag_values_dict"><code>flag_values_dict</code></h3>

``` python
flag_values_dict()
```

Returns a dictionary that maps flag names to flag values.


<h3 id="flags_by_module_dict"><code>flags_by_module_dict</code></h3>

``` python
flags_by_module_dict()
```

Returns the dictionary of module_name -> list of defined flags.


#### Returns:

A dictionary.  Its keys are module names (strings).  Its values
are lists of Flag objects.


<h3 id="flags_by_module_id_dict"><code>flags_by_module_id_dict</code></h3>

``` python
flags_by_module_id_dict()
```

Returns the dictionary of module_id -> list of defined flags.


#### Returns:

A dictionary.  Its keys are module IDs (ints).  Its values
are lists of Flag objects.


<h3 id="flags_into_string"><code>flags_into_string</code></h3>

``` python
flags_into_string()
```

Returns a string with the flags assignments from this FlagValues object.

This function ignores flags whose value is None.  Each flag
assignment is separated by a newline.

NOTE: MUST mirror the behavior of the C++ CommandlineFlagsIntoString
from https://github.com/gflags/gflags.

#### Returns:

str, the string with the flags assignments from this FlagValues object.
The flags are ordered by (module_name, flag_name).


<h3 id="get_flag_value"><code>get_flag_value</code></h3>

``` python
get_flag_value(
    name,
    default
)
```

Returns the value of a flag (if not None) or a default value.


#### Args:


* <b>`name`</b>: str, the name of a flag.
* <b>`default`</b>: Default value to use if the flag value is None.


#### Returns:

Requested flag value or default.


<h3 id="get_help"><code>get_help</code></h3>

``` python
get_help(
    prefix='',
    include_special_flags=True
)
```

Returns a help string for all known flags.


#### Args:


* <b>`prefix`</b>: str, per-line output prefix.
* <b>`include_special_flags`</b>: bool, whether to include description of
  SPECIAL_FLAGS, i.e. --flagfile and --undefok.


#### Returns:

str, formatted help message.


<h3 id="get_key_flags_for_module"><code>get_key_flags_for_module</code></h3>

``` python
get_key_flags_for_module(module)
```

Returns the list of key flags for a module.


#### Args:


* <b>`module`</b>: module|str, the module to get key flags from.


#### Returns:

[Flag], a new list of Flag instances.  Caller may update this list as

* <b>`desired`</b>: none of those changes will affect the internals of this
FlagValue instance.

<h3 id="is_gnu_getopt"><code>is_gnu_getopt</code></h3>

``` python
is_gnu_getopt()
```




<h3 id="is_parsed"><code>is_parsed</code></h3>

``` python
is_parsed()
```

Returns whether flags were parsed.


<h3 id="key_flags_by_module_dict"><code>key_flags_by_module_dict</code></h3>

``` python
key_flags_by_module_dict()
```

Returns the dictionary of module_name -> list of key flags.


#### Returns:

A dictionary.  Its keys are module names (strings).  Its values
are lists of Flag objects.


<h3 id="main_module_help"><code>main_module_help</code></h3>

``` python
main_module_help()
```

Describes the key flags of the main module.


#### Returns:

str, describing the key flags of the main module.


<h3 id="mark_as_parsed"><code>mark_as_parsed</code></h3>

``` python
mark_as_parsed()
```

Explicitly marks flags as parsed.

Use this when the caller knows that this FlagValues has been parsed as if
a __call__() invocation has happened.  This is only a public method for
use by things like appcommands which do additional command like parsing.

<h3 id="module_help"><code>module_help</code></h3>

``` python
module_help(module)
```

Describes the key flags of a module.


#### Args:


* <b>`module`</b>: module|str, the module to describe the key flags for.


#### Returns:

str, describing the key flags of a module.


<h3 id="read_flags_from_files"><code>read_flags_from_files</code></h3>

``` python
read_flags_from_files(
    argv,
    force_gnu=True
)
```

Processes command line args, but also allow args to be read from file.


#### Args:


* <b>`argv`</b>: [str], a list of strings, usually sys.argv[1:], which may contain
    one or more flagfile directives of the form --flagfile="./filename".
    Note that the name of the program (sys.argv[0]) should be omitted.
* <b>`force_gnu`</b>: bool, if False, --flagfile parsing obeys the
    FLAGS.is_gnu_getopt() value. If True, ignore the value and always
    follow gnu_getopt semantics.


#### Returns:

A new list which has the original list combined with what we read
from any flagfile(s).



#### Raises:


* <b>`IllegalFlagValueError`</b>: Raised when --flagfile is provided with no
    argument.

This function is called by FLAGS(argv).
It scans the input list for a flag that looks like:
--flagfile=<somefile>. Then it opens <somefile>, reads all valid key
and value pairs and inserts them into the input list in exactly the
place where the --flagfile arg is found.

Note that your application's flags are still defined the usual way
using absl.flags DEFINE_flag() type functions.

Notes (assuming we're getting a commandline of some sort as our input):
--> For duplicate flags, the last one we hit should "win".
--> Since flags that appear later win, a flagfile's settings can be "weak"
    if the --flagfile comes at the beginning of the argument sequence,
    and it can be "strong" if the --flagfile comes at the end.
--> A further "--flagfile=<otherfile.cfg>" CAN be nested in a flagfile.
    It will be expanded in exactly the spot where it is found.
--> In a flagfile, a line beginning with # or // is a comment.
--> Entirely blank lines _should_ be ignored.

<h3 id="register_flag_by_module"><code>register_flag_by_module</code></h3>

``` python
register_flag_by_module(
    module_name,
    flag
)
```

Records the module that defines a specific flag.

We keep track of which flag is defined by which module so that we
can later sort the flags by module.

#### Args:


* <b>`module_name`</b>: str, the name of a Python module.
* <b>`flag`</b>: Flag, the Flag instance that is key to the module.

<h3 id="register_flag_by_module_id"><code>register_flag_by_module_id</code></h3>

``` python
register_flag_by_module_id(
    module_id,
    flag
)
```

Records the module that defines a specific flag.


#### Args:


* <b>`module_id`</b>: int, the ID of the Python module.
* <b>`flag`</b>: Flag, the Flag instance that is key to the module.

<h3 id="register_key_flag_for_module"><code>register_key_flag_for_module</code></h3>

``` python
register_key_flag_for_module(
    module_name,
    flag
)
```

Specifies that a flag is a key flag for a module.


#### Args:


* <b>`module_name`</b>: str, the name of a Python module.
* <b>`flag`</b>: Flag, the Flag instance that is key to the module.

<h3 id="remove_flag_values"><code>remove_flag_values</code></h3>

``` python
remove_flag_values(flag_values)
```

Remove flags that were previously appended from another FlagValues.


#### Args:


* <b>`flag_values`</b>: FlagValues, the FlagValues instance containing flags to
    remove.

<h3 id="set_default"><code>set_default</code></h3>

``` python
set_default(
    name,
    value
)
```

Changes the default value of the named flag object.

The flag's current value is also updated if the flag is currently using
the default value, i.e. not specified in the command line, and not set
by FLAGS.name = value.

#### Args:


* <b>`name`</b>: str, the name of the flag to modify.
* <b>`value`</b>: The new default value.


#### Raises:


* <b>`UnrecognizedFlagError`</b>: Raised when there is no registered flag named name.
* <b>`IllegalFlagValueError`</b>: Raised when value is not valid.

<h3 id="set_gnu_getopt"><code>set_gnu_getopt</code></h3>

``` python
set_gnu_getopt(gnu_getopt=True)
```

Sets whether or not to use GNU style scanning.

GNU style allows mixing of flag and non-flag arguments. See
http://docs.python.org/library/getopt.html#getopt.gnu_getopt

#### Args:


* <b>`gnu_getopt`</b>: bool, whether or not to use GNU style scanning.

<h3 id="unparse_flags"><code>unparse_flags</code></h3>

``` python
unparse_flags()
```

Unparses all flags to the point before any FLAGS(argv) was called.


<h3 id="write_help_in_xml_format"><code>write_help_in_xml_format</code></h3>

``` python
write_help_in_xml_format(outfile=None)
```

Outputs flag documentation in XML format.

NOTE: We use element names that are consistent with those used by
the C++ command-line flag library, from
https://github.com/gflags/gflags.
We also use a few new elements (e.g., <key>), but we do not
interfere / overlap with existing XML elements used by the C++
library.  Please maintain this consistency.

#### Args:


* <b>`outfile`</b>: File object we write to.  Default None means sys.stdout.
