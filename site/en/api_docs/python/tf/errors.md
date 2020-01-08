page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.errors





Exception types for TensorFlow errors.

## Classes

[`class AbortedError`](../tf/errors/AbortedError): The operation was aborted, typically due to a concurrent action.

[`class AlreadyExistsError`](../tf/errors/AlreadyExistsError): Raised when an entity that we attempted to create already exists.

[`class CancelledError`](../tf/errors/CancelledError): Raised when an operation or step is cancelled.

[`class DataLossError`](../tf/errors/DataLossError): Raised when unrecoverable data loss or corruption is encountered.

[`class DeadlineExceededError`](../tf/errors/DeadlineExceededError): Raised when a deadline expires before an operation could complete.

[`class FailedPreconditionError`](../tf/errors/FailedPreconditionError): Operation was rejected because the system is not in a state to execute it.

[`class InternalError`](../tf/errors/InternalError): Raised when the system experiences an internal error.

[`class InvalidArgumentError`](../tf/errors/InvalidArgumentError): Raised when an operation receives an invalid argument.

[`class NotFoundError`](../tf/errors/NotFoundError): Raised when a requested entity (e.g., a file or directory) was not found.

[`class OpError`](../tf/errors/OpError): A generic error that is raised when TensorFlow execution fails.

[`class OutOfRangeError`](../tf/errors/OutOfRangeError): Raised when an operation iterates past the valid input range.

[`class PermissionDeniedError`](../tf/errors/PermissionDeniedError): Raised when the caller does not have permission to run an operation.

[`class ResourceExhaustedError`](../tf/errors/ResourceExhaustedError): Some resource has been exhausted.

[`class UnauthenticatedError`](../tf/errors/UnauthenticatedError): The request does not have valid authentication credentials.

[`class UnavailableError`](../tf/errors/UnavailableError): Raised when the runtime is currently unavailable.

[`class UnimplementedError`](../tf/errors/UnimplementedError): Raised when an operation has not been implemented.

[`class UnknownError`](../tf/errors/UnknownError): Unknown error.

[`class raise_exception_on_not_ok_status`](../tf/errors/raise_exception_on_not_ok_status): Context manager to check for C API status.

## Functions

[`error_code_from_exception_type(...)`](../tf/errors/error_code_from_exception_type)

[`exception_type_from_error_code(...)`](../tf/errors/exception_type_from_error_code)

## Other Members

<h3 id="ABORTED"><code>ABORTED</code></h3>

<h3 id="ALREADY_EXISTS"><code>ALREADY_EXISTS</code></h3>

<h3 id="CANCELLED"><code>CANCELLED</code></h3>

<h3 id="DATA_LOSS"><code>DATA_LOSS</code></h3>

<h3 id="DEADLINE_EXCEEDED"><code>DEADLINE_EXCEEDED</code></h3>

<h3 id="FAILED_PRECONDITION"><code>FAILED_PRECONDITION</code></h3>

<h3 id="INTERNAL"><code>INTERNAL</code></h3>

<h3 id="INVALID_ARGUMENT"><code>INVALID_ARGUMENT</code></h3>

<h3 id="NOT_FOUND"><code>NOT_FOUND</code></h3>

<h3 id="OK"><code>OK</code></h3>

<h3 id="OUT_OF_RANGE"><code>OUT_OF_RANGE</code></h3>

<h3 id="PERMISSION_DENIED"><code>PERMISSION_DENIED</code></h3>

<h3 id="RESOURCE_EXHAUSTED"><code>RESOURCE_EXHAUSTED</code></h3>

<h3 id="UNAUTHENTICATED"><code>UNAUTHENTICATED</code></h3>

<h3 id="UNAVAILABLE"><code>UNAVAILABLE</code></h3>

<h3 id="UNIMPLEMENTED"><code>UNIMPLEMENTED</code></h3>

<h3 id="UNKNOWN"><code>UNKNOWN</code></h3>

