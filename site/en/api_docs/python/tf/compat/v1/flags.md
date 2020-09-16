description: Import router for absl.flags. See https://github.com/abseil/abseil-py.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.flags

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/platform/flags.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Import router for absl.flags. See https://github.com/abseil/abseil-py.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags`</p>
</p>
</section>



## Modules

[`tf_decorator`](../../../tf/compat/v1/flags/tf_decorator.md) module: Base TFDecorator class and utility functions for working with decorators.

## Classes

[`class ArgumentParser`](../../../tf/compat/v1/flags/ArgumentParser.md): Base class used to parse and convert arguments.

[`class ArgumentSerializer`](../../../tf/compat/v1/flags/ArgumentSerializer.md): Base class for generating string representations of a flag value.

[`class BaseListParser`](../../../tf/compat/v1/flags/BaseListParser.md): Base class for a parser of lists of strings.

[`class BooleanFlag`](../../../tf/compat/v1/flags/BooleanFlag.md): Basic boolean flag.

[`class BooleanParser`](../../../tf/compat/v1/flags/BooleanParser.md): Parser of boolean values.

[`class CantOpenFlagFileError`](../../../tf/compat/v1/flags/CantOpenFlagFileError.md): Raised when flagfile fails to open.

[`class CsvListSerializer`](../../../tf/compat/v1/flags/CsvListSerializer.md): Base class for generating string representations of a flag value.

[`class DuplicateFlagError`](../../../tf/compat/v1/flags/DuplicateFlagError.md): Raised if there is a flag naming conflict.

[`class EnumClassFlag`](../../../tf/compat/v1/flags/EnumClassFlag.md): Basic enum flag; its value is an enum class's member.

[`class EnumClassParser`](../../../tf/compat/v1/flags/EnumClassParser.md): Parser of an Enum class member.

[`class EnumFlag`](../../../tf/compat/v1/flags/EnumFlag.md): Basic enum flag; its value can be any string from list of enum_values.

[`class EnumParser`](../../../tf/compat/v1/flags/EnumParser.md): Parser of a string enum value (a string value from a given set).

[`class Error`](../../../tf/compat/v1/flags/Error.md): The base class for all flags errors.

[`class Flag`](../../../tf/compat/v1/flags/Flag.md): Information about a command-line flag.

[`class FlagNameConflictsWithMethodError`](../../../tf/compat/v1/flags/FlagNameConflictsWithMethodError.md): Raised when a flag name conflicts with FlagValues methods.

[`class FlagValues`](../../../tf/compat/v1/flags/FlagValues.md): Registry of 'Flag' objects.

[`class FloatParser`](../../../tf/compat/v1/flags/FloatParser.md): Parser of floating point values.

[`class IllegalFlagValueError`](../../../tf/compat/v1/flags/IllegalFlagValueError.md): Raised when the flag command line argument is illegal.

[`class IntegerParser`](../../../tf/compat/v1/flags/IntegerParser.md): Parser of an integer value.

[`class ListParser`](../../../tf/compat/v1/flags/ListParser.md): Parser for a comma-separated list of strings.

[`class ListSerializer`](../../../tf/compat/v1/flags/ListSerializer.md): Base class for generating string representations of a flag value.

[`class MultiEnumClassFlag`](../../../tf/compat/v1/flags/MultiEnumClassFlag.md): A multi_enum_class flag.

[`class MultiFlag`](../../../tf/compat/v1/flags/MultiFlag.md): A flag that can appear multiple time on the command-line.

[`class UnparsedFlagAccessError`](../../../tf/compat/v1/flags/UnparsedFlagAccessError.md): Raised when accessing the flag value from unparsed FlagValues.

[`class UnrecognizedFlagError`](../../../tf/compat/v1/flags/UnrecognizedFlagError.md): Raised when a flag is unrecognized.

[`class ValidationError`](../../../tf/compat/v1/flags/ValidationError.md): Raised when flag validator constraint is not satisfied.

[`class WhitespaceSeparatedListParser`](../../../tf/compat/v1/flags/WhitespaceSeparatedListParser.md): Parser for a whitespace-separated list of strings.

## Functions

[`DEFINE(...)`](../../../tf/compat/v1/flags/DEFINE.md): Registers a generic Flag object.

[`DEFINE_alias(...)`](../../../tf/compat/v1/flags/DEFINE_alias.md): Defines an alias flag for an existing one.

[`DEFINE_bool(...)`](../../../tf/compat/v1/flags/DEFINE_bool.md): Registers a boolean flag.

[`DEFINE_boolean(...)`](../../../tf/compat/v1/flags/DEFINE_bool.md): Registers a boolean flag.

[`DEFINE_enum(...)`](../../../tf/compat/v1/flags/DEFINE_enum.md): Registers a flag whose value can be any string from enum_values.

[`DEFINE_enum_class(...)`](../../../tf/compat/v1/flags/DEFINE_enum_class.md): Registers a flag whose value can be the name of enum members.

[`DEFINE_flag(...)`](../../../tf/compat/v1/flags/DEFINE_flag.md): Registers a 'Flag' object with a 'FlagValues' object.

[`DEFINE_float(...)`](../../../tf/compat/v1/flags/DEFINE_float.md): Registers a flag whose value must be a float.

[`DEFINE_integer(...)`](../../../tf/compat/v1/flags/DEFINE_integer.md): Registers a flag whose value must be an integer.

[`DEFINE_list(...)`](../../../tf/compat/v1/flags/DEFINE_list.md): Registers a flag whose value is a comma-separated list of strings.

[`DEFINE_multi(...)`](../../../tf/compat/v1/flags/DEFINE_multi.md): Registers a generic MultiFlag that parses its args with a given parser.

[`DEFINE_multi_enum(...)`](../../../tf/compat/v1/flags/DEFINE_multi_enum.md): Registers a flag whose value can be a list strings from enum_values.

[`DEFINE_multi_enum_class(...)`](../../../tf/compat/v1/flags/DEFINE_multi_enum_class.md): Registers a flag whose value can be a list of enum members.

[`DEFINE_multi_float(...)`](../../../tf/compat/v1/flags/DEFINE_multi_float.md): Registers a flag whose value can be a list of arbitrary floats.

[`DEFINE_multi_integer(...)`](../../../tf/compat/v1/flags/DEFINE_multi_integer.md): Registers a flag whose value can be a list of arbitrary integers.

[`DEFINE_multi_string(...)`](../../../tf/compat/v1/flags/DEFINE_multi_string.md): Registers a flag whose value can be a list of any strings.

[`DEFINE_spaceseplist(...)`](../../../tf/compat/v1/flags/DEFINE_spaceseplist.md): Registers a flag whose value is a whitespace-separated list of strings.

[`DEFINE_string(...)`](../../../tf/compat/v1/flags/DEFINE_string.md): Registers a flag whose value can be any string.

[`FLAGS(...)`](../../../tf/compat/v1/flags/FLAGS.md): Registry of 'Flag' objects.

[`adopt_module_key_flags(...)`](../../../tf/compat/v1/flags/adopt_module_key_flags.md): Declares that all flags key to a module are key to the current module.

[`declare_key_flag(...)`](../../../tf/compat/v1/flags/declare_key_flag.md): Declares one flag as key to the current module.

[`disclaim_key_flags(...)`](../../../tf/compat/v1/flags/disclaim_key_flags.md): Declares that the current module will not define any more key flags.

[`doc_to_help(...)`](../../../tf/compat/v1/flags/doc_to_help.md): Takes a __doc__ string and reformats it as help.

[`flag_dict_to_args(...)`](../../../tf/compat/v1/flags/flag_dict_to_args.md): Convert a dict of values into process call parameters.

[`get_help_width(...)`](../../../tf/compat/v1/flags/get_help_width.md): Returns the integer width of help lines that is used in TextWrap.

[`mark_bool_flags_as_mutual_exclusive(...)`](../../../tf/compat/v1/flags/mark_bool_flags_as_mutual_exclusive.md): Ensures that only one flag among flag_names is True.

[`mark_flag_as_required(...)`](../../../tf/compat/v1/flags/mark_flag_as_required.md): Ensures that flag is not None during program execution.

[`mark_flags_as_mutual_exclusive(...)`](../../../tf/compat/v1/flags/mark_flags_as_mutual_exclusive.md): Ensures that only one flag among flag_names is not None.

[`mark_flags_as_required(...)`](../../../tf/compat/v1/flags/mark_flags_as_required.md): Ensures that flags are not None during program execution.

[`multi_flags_validator(...)`](../../../tf/compat/v1/flags/multi_flags_validator.md): A function decorator for defining a multi-flag validator.

[`register_multi_flags_validator(...)`](../../../tf/compat/v1/flags/register_multi_flags_validator.md): Adds a constraint to multiple flags.

[`register_validator(...)`](../../../tf/compat/v1/flags/register_validator.md): Adds a constraint, which will be enforced during program execution.

[`text_wrap(...)`](../../../tf/compat/v1/flags/text_wrap.md): Wraps a given text to a maximum line length and returns it.

[`validator(...)`](../../../tf/compat/v1/flags/validator.md): A function decorator for defining a flag validator.

