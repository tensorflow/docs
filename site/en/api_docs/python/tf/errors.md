

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.errors

### Module `tf.errors`



Defined in [`tensorflow/python/framework/errors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/framework/errors.py).

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

[`class OpError`](../tf/OpError): A generic error that is raised when TensorFlow execution fails.

[`class OutOfRangeError`](../tf/errors/OutOfRangeError): Raised when an operation iterates past the valid input range.

[`class PermissionDeniedError`](../tf/errors/PermissionDeniedError): Raised when the caller does not have permission to run an operation.

[`class ResourceExhaustedError`](../tf/errors/ResourceExhaustedError): Some resource has been exhausted.

[`class UnauthenticatedError`](../tf/errors/UnauthenticatedError): The request does not have valid authentication credentials.

[`class UnavailableError`](../tf/errors/UnavailableError): Raised when the runtime is currently unavailable.

[`class UnimplementedError`](../tf/errors/UnimplementedError): Raised when an operation has not been implemented.

[`class UnknownError`](../tf/errors/UnknownError): Unknown error.

## Functions

[`error_code_from_exception_type(...)`](../tf/errors/error_code_from_exception_type)

[`exception_type_from_error_code(...)`](../tf/errors/exception_type_from_error_code)

[`raise_exception_on_not_ok_status(...)`](../tf/errors/raise_exception_on_not_ok_status)

## Other Members

`ABORTED`

`ALREADY_EXISTS`

`CANCELLED`

`DATA_LOSS`

`DEADLINE_EXCEEDED`

`FAILED_PRECONDITION`

`INTERNAL`

`INVALID_ARGUMENT`

`NOT_FOUND`

`OK`

`OUT_OF_RANGE`

`PERMISSION_DENIED`

`RESOURCE_EXHAUSTED`

`UNAUTHENTICATED`

`UNAVAILABLE`

`UNIMPLEMENTED`

`UNKNOWN`

