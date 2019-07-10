page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.errors

Exception types for TensorFlow errors.

<!-- Placeholder for "Used in" -->


## Classes

[`class AbortedError`](../../../tf/errors/AbortedError): The operation was aborted, typically due to a concurrent action.

[`class AlreadyExistsError`](../../../tf/errors/AlreadyExistsError): Raised when an entity that we attempted to create already exists.

[`class CancelledError`](../../../tf/errors/CancelledError): Raised when an operation or step is cancelled.

[`class DataLossError`](../../../tf/errors/DataLossError): Raised when unrecoverable data loss or corruption is encountered.

[`class DeadlineExceededError`](../../../tf/errors/DeadlineExceededError): Raised when a deadline expires before an operation could complete.

[`class FailedPreconditionError`](../../../tf/errors/FailedPreconditionError): Operation was rejected because the system is not in a state to execute it.

[`class InternalError`](../../../tf/errors/InternalError): Raised when the system experiences an internal error.

[`class InvalidArgumentError`](../../../tf/errors/InvalidArgumentError): Raised when an operation receives an invalid argument.

[`class NotFoundError`](../../../tf/errors/NotFoundError): Raised when a requested entity (e.g., a file or directory) was not found.

[`class OpError`](../../../tf/errors/OpError): A generic error that is raised when TensorFlow execution fails.

[`class OutOfRangeError`](../../../tf/errors/OutOfRangeError): Raised when an operation iterates past the valid input range.

[`class PermissionDeniedError`](../../../tf/errors/PermissionDeniedError): Raised when the caller does not have permission to run an operation.

[`class ResourceExhaustedError`](../../../tf/errors/ResourceExhaustedError): Some resource has been exhausted.

[`class UnauthenticatedError`](../../../tf/errors/UnauthenticatedError): The request does not have valid authentication credentials.

[`class UnavailableError`](../../../tf/errors/UnavailableError): Raised when the runtime is currently unavailable.

[`class UnimplementedError`](../../../tf/errors/UnimplementedError): Raised when an operation has not been implemented.

[`class UnknownError`](../../../tf/errors/UnknownError): Unknown error.

[`class raise_exception_on_not_ok_status`](../../../tf/errors/raise_exception_on_not_ok_status): Context manager to check for C API status.

## Functions

[`error_code_from_exception_type(...)`](../../../tf/errors/error_code_from_exception_type)

[`exception_type_from_error_code(...)`](../../../tf/errors/exception_type_from_error_code)

## Other Members

* `ABORTED = 10` <a id="ABORTED"></a>
* `ALREADY_EXISTS = 6` <a id="ALREADY_EXISTS"></a>
* `CANCELLED = 1` <a id="CANCELLED"></a>
* `DATA_LOSS = 15` <a id="DATA_LOSS"></a>
* `DEADLINE_EXCEEDED = 4` <a id="DEADLINE_EXCEEDED"></a>
* `FAILED_PRECONDITION = 9` <a id="FAILED_PRECONDITION"></a>
* `INTERNAL = 13` <a id="INTERNAL"></a>
* `INVALID_ARGUMENT = 3` <a id="INVALID_ARGUMENT"></a>
* `NOT_FOUND = 5` <a id="NOT_FOUND"></a>
* `OK = 0` <a id="OK"></a>
* `OUT_OF_RANGE = 11` <a id="OUT_OF_RANGE"></a>
* `PERMISSION_DENIED = 7` <a id="PERMISSION_DENIED"></a>
* `RESOURCE_EXHAUSTED = 8` <a id="RESOURCE_EXHAUSTED"></a>
* `UNAUTHENTICATED = 16` <a id="UNAUTHENTICATED"></a>
* `UNAVAILABLE = 14` <a id="UNAVAILABLE"></a>
* `UNIMPLEMENTED = 12` <a id="UNIMPLEMENTED"></a>
* `UNKNOWN = 2` <a id="UNKNOWN"></a>
