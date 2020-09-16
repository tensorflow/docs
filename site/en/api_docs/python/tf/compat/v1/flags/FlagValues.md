description: Registry of 'Flag' objects.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.FlagValues" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__contains__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="append_flag_values"/>
<meta itemprop="property" content="append_flags_into_file"/>
<meta itemprop="property" content="find_module_defining_flag"/>
<meta itemprop="property" content="find_module_id_defining_flag"/>
<meta itemprop="property" content="flag_values_dict"/>
<meta itemprop="property" content="flags_by_module_dict"/>
<meta itemprop="property" content="flags_by_module_id_dict"/>
<meta itemprop="property" content="flags_into_string"/>
<meta itemprop="property" content="get_flag_value"/>
<meta itemprop="property" content="get_help"/>
<meta itemprop="property" content="get_key_flags_for_module"/>
<meta itemprop="property" content="is_gnu_getopt"/>
<meta itemprop="property" content="is_parsed"/>
<meta itemprop="property" content="key_flags_by_module_dict"/>
<meta itemprop="property" content="main_module_help"/>
<meta itemprop="property" content="mark_as_parsed"/>
<meta itemprop="property" content="module_help"/>
<meta itemprop="property" content="read_flags_from_files"/>
<meta itemprop="property" content="register_flag_by_module"/>
<meta itemprop="property" content="register_flag_by_module_id"/>
<meta itemprop="property" content="register_key_flag_for_module"/>
<meta itemprop="property" content="remove_flag_values"/>
<meta itemprop="property" content="set_default"/>
<meta itemprop="property" content="set_gnu_getopt"/>
<meta itemprop="property" content="unparse_flags"/>
<meta itemprop="property" content="write_help_in_xml_format"/>
</div>

# tf.compat.v1.flags.FlagValues

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Registry of 'Flag' objects.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.FlagValues`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.FlagValues()
</code></pre>



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

## Methods

<h3 id="append_flag_values"><code>append_flag_values</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>append_flag_values(
    flag_values
)
</code></pre>

Appends flags registered in another FlagValues instance.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`flag_values`
</td>
<td>
FlagValues, the FlagValues instance from which to copy flags.
</td>
</tr>
</table>



<h3 id="append_flags_into_file"><code>append_flags_into_file</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>append_flags_into_file(
    filename
)
</code></pre>

Appends all flags assignments from this FlagInfo object to a file.

Output will be in the format of a flagfile.

NOTE: MUST mirror the behavior of the C++ AppendFlagsIntoFile
from https://github.com/gflags/gflags.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`filename`
</td>
<td>
str, name of the file.
</td>
</tr>
</table>



<h3 id="find_module_defining_flag"><code>find_module_defining_flag</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>find_module_defining_flag(
    flagname, default=None
)
</code></pre>

Return the name of the module defining this flag, or default.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`flagname`
</td>
<td>
str, name of the flag to lookup.
</td>
</tr><tr>
<td>
`default`
</td>
<td>
Value to return if flagname is not defined. Defaults
to None.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The name of the module which registered the flag with this name.
If no such module exists (i.e. no flag with this name exists),
we return default.
</td>
</tr>

</table>



<h3 id="find_module_id_defining_flag"><code>find_module_id_defining_flag</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>find_module_id_defining_flag(
    flagname, default=None
)
</code></pre>

Return the ID of the module defining this flag, or default.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`flagname`
</td>
<td>
str, name of the flag to lookup.
</td>
</tr><tr>
<td>
`default`
</td>
<td>
Value to return if flagname is not defined. Defaults
to None.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The ID of the module which registered the flag with this name.
If no such module exists (i.e. no flag with this name exists),
we return default.
</td>
</tr>

</table>



<h3 id="flag_values_dict"><code>flag_values_dict</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flag_values_dict()
</code></pre>

Returns a dictionary that maps flag names to flag values.


<h3 id="flags_by_module_dict"><code>flags_by_module_dict</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flags_by_module_dict()
</code></pre>

Returns the dictionary of module_name -> list of defined flags.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dictionary.  Its keys are module names (strings).  Its values
are lists of Flag objects.
</td>
</tr>

</table>



<h3 id="flags_by_module_id_dict"><code>flags_by_module_id_dict</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flags_by_module_id_dict()
</code></pre>

Returns the dictionary of module_id -> list of defined flags.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dictionary.  Its keys are module IDs (ints).  Its values
are lists of Flag objects.
</td>
</tr>

</table>



<h3 id="flags_into_string"><code>flags_into_string</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flags_into_string()
</code></pre>

Returns a string with the flags assignments from this FlagValues object.

This function ignores flags whose value is None.  Each flag
assignment is separated by a newline.

NOTE: MUST mirror the behavior of the C++ CommandlineFlagsIntoString
from https://github.com/gflags/gflags.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
str, the string with the flags assignments from this FlagValues object.
The flags are ordered by (module_name, flag_name).
</td>
</tr>

</table>



<h3 id="get_flag_value"><code>get_flag_value</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_flag_value(
    name, default
)
</code></pre>

Returns the value of a flag (if not None) or a default value.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
str, the name of a flag.
</td>
</tr><tr>
<td>
`default`
</td>
<td>
Default value to use if the flag value is None.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Requested flag value or default.
</td>
</tr>

</table>



<h3 id="get_help"><code>get_help</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_help(
    prefix='', include_special_flags=(True)
)
</code></pre>

Returns a help string for all known flags.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`prefix`
</td>
<td>
str, per-line output prefix.
</td>
</tr><tr>
<td>
`include_special_flags`
</td>
<td>
bool, whether to include description of
SPECIAL_FLAGS, i.e. --flagfile and --undefok.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
str, formatted help message.
</td>
</tr>

</table>



<h3 id="get_key_flags_for_module"><code>get_key_flags_for_module</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_key_flags_for_module(
    module
)
</code></pre>

Returns the list of key flags for a module.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`module`
</td>
<td>
module|str, the module to get key flags from.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
[Flag], a new list of Flag instances.  Caller may update this list as
</td>
</tr>
<tr>
<td>
`desired`
</td>
<td>
none of those changes will affect the internals of this
FlagValue instance.
</td>
</tr>
</table>



<h3 id="is_gnu_getopt"><code>is_gnu_getopt</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_gnu_getopt()
</code></pre>




<h3 id="is_parsed"><code>is_parsed</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_parsed()
</code></pre>

Returns whether flags were parsed.


<h3 id="key_flags_by_module_dict"><code>key_flags_by_module_dict</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>key_flags_by_module_dict()
</code></pre>

Returns the dictionary of module_name -> list of key flags.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dictionary.  Its keys are module names (strings).  Its values
are lists of Flag objects.
</td>
</tr>

</table>



<h3 id="main_module_help"><code>main_module_help</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>main_module_help()
</code></pre>

Describes the key flags of the main module.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
str, describing the key flags of the main module.
</td>
</tr>

</table>



<h3 id="mark_as_parsed"><code>mark_as_parsed</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>mark_as_parsed()
</code></pre>

Explicitly marks flags as parsed.

Use this when the caller knows that this FlagValues has been parsed as if
a __call__() invocation has happened.  This is only a public method for
use by things like appcommands which do additional command like parsing.

<h3 id="module_help"><code>module_help</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>module_help(
    module
)
</code></pre>

Describes the key flags of a module.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`module`
</td>
<td>
module|str, the module to describe the key flags for.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
str, describing the key flags of a module.
</td>
</tr>

</table>



<h3 id="read_flags_from_files"><code>read_flags_from_files</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>read_flags_from_files(
    argv, force_gnu=(True)
)
</code></pre>

Processes command line args, but also allow args to be read from file.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`argv`
</td>
<td>
[str], a list of strings, usually sys.argv[1:], which may contain
one or more flagfile directives of the form --flagfile="./filename".
Note that the name of the program (sys.argv[0]) should be omitted.
</td>
</tr><tr>
<td>
`force_gnu`
</td>
<td>
bool, if False, --flagfile parsing obeys the
FLAGS.is_gnu_getopt() value. If True, ignore the value and always
follow gnu_getopt semantics.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A new list which has the original list combined with what we read
from any flagfile(s).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`IllegalFlagValueError`
</td>
<td>
Raised when --flagfile is provided with no
argument.
</td>
</tr>
</table>


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

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>register_flag_by_module(
    module_name, flag
)
</code></pre>

Records the module that defines a specific flag.

We keep track of which flag is defined by which module so that we
can later sort the flags by module.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`module_name`
</td>
<td>
str, the name of a Python module.
</td>
</tr><tr>
<td>
`flag`
</td>
<td>
Flag, the Flag instance that is key to the module.
</td>
</tr>
</table>



<h3 id="register_flag_by_module_id"><code>register_flag_by_module_id</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>register_flag_by_module_id(
    module_id, flag
)
</code></pre>

Records the module that defines a specific flag.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`module_id`
</td>
<td>
int, the ID of the Python module.
</td>
</tr><tr>
<td>
`flag`
</td>
<td>
Flag, the Flag instance that is key to the module.
</td>
</tr>
</table>



<h3 id="register_key_flag_for_module"><code>register_key_flag_for_module</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>register_key_flag_for_module(
    module_name, flag
)
</code></pre>

Specifies that a flag is a key flag for a module.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`module_name`
</td>
<td>
str, the name of a Python module.
</td>
</tr><tr>
<td>
`flag`
</td>
<td>
Flag, the Flag instance that is key to the module.
</td>
</tr>
</table>



<h3 id="remove_flag_values"><code>remove_flag_values</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>remove_flag_values(
    flag_values
)
</code></pre>

Remove flags that were previously appended from another FlagValues.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`flag_values`
</td>
<td>
FlagValues, the FlagValues instance containing flags to
remove.
</td>
</tr>
</table>



<h3 id="set_default"><code>set_default</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_default(
    name, value
)
</code></pre>

Changes the default value of the named flag object.

The flag's current value is also updated if the flag is currently using
the default value, i.e. not specified in the command line, and not set
by FLAGS.name = value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
str, the name of the flag to modify.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
The new default value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`UnrecognizedFlagError`
</td>
<td>
Raised when there is no registered flag named name.
</td>
</tr><tr>
<td>
`IllegalFlagValueError`
</td>
<td>
Raised when value is not valid.
</td>
</tr>
</table>



<h3 id="set_gnu_getopt"><code>set_gnu_getopt</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_gnu_getopt(
    gnu_getopt=(True)
)
</code></pre>

Sets whether or not to use GNU style scanning.

GNU style allows mixing of flag and non-flag arguments. See
http://docs.python.org/library/getopt.html#getopt.gnu_getopt

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`gnu_getopt`
</td>
<td>
bool, whether or not to use GNU style scanning.
</td>
</tr>
</table>



<h3 id="unparse_flags"><code>unparse_flags</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>unparse_flags()
</code></pre>

Unparses all flags to the point before any FLAGS(argv) was called.


<h3 id="write_help_in_xml_format"><code>write_help_in_xml_format</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>write_help_in_xml_format(
    outfile=None
)
</code></pre>

Outputs flag documentation in XML format.

NOTE: We use element names that are consistent with those used by
the C++ command-line flag library, from
https://github.com/gflags/gflags.
We also use a few new elements (e.g., <key>), but we do not
interfere / overlap with existing XML elements used by the C++
library.  Please maintain this consistency.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`outfile`
</td>
<td>
File object we write to.  Default None means sys.stdout.
</td>
</tr>
</table>



<h3 id="__call__"><code>__call__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    argv, known_only=(False)
)
</code></pre>

Parses flags from argv; stores parsed flags into this FlagValues object.

All unparsed arguments are returned.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`argv`
</td>
<td>
a tuple/list of strings.
</td>
</tr><tr>
<td>
`known_only`
</td>
<td>
bool, if True, parse and remove known flags; return the rest
untouched. Unknown flags specified by --undefok are not returned.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The list of arguments not parsed as options, including argv[0].
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`Error`
</td>
<td>
Raised on any parsing error.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
Raised on passing wrong type of arguments.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
Raised on flag value parsing error.
</td>
</tr>
</table>



<h3 id="__contains__"><code>__contains__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__contains__(
    name
)
</code></pre>

Returns True if name is a value (flag) in the dict.


<h3 id="__getitem__"><code>__getitem__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    name
)
</code></pre>

Returns the Flag object for the flag --name.


<h3 id="__iter__"><code>__iter__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>




<h3 id="__len__"><code>__len__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__len__()
</code></pre>






