


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.errors

### Module `tf.errors`

Exception types for TensorFlow errors.

## Members

Constant ABORTED

Constant ALREADY_EXISTS

[`class AbortedError`](../tf/errors/AbortedError): The operation was aborted, typically due to a concurrent action.

[`class AlreadyExistsError`](../tf/errors/AlreadyExistsError): Raised when an entity that we attempted to create already exists.

Constant CANCELLED

[`class CancelledError`](../tf/errors/CancelledError): Raised when an operation or step is cancelled.

Constant DATA_LOSS

Constant DEADLINE_EXCEEDED

[`class DataLossError`](../tf/errors/DataLossError): Raised when unrecoverable data loss or corruption is encountered.

[`class DeadlineExceededError`](../tf/errors/DeadlineExceededError): Raised when a deadline expires before an operation could complete.

Constant FAILED_PRECONDITION

[`class FailedPreconditionError`](../tf/errors/FailedPreconditionError): Operation was rejected because the system is not in a state to execute it.

Constant INTERNAL

Constant INVALID_ARGUMENT

[`class InternalError`](../tf/errors/InternalError): Raised when the system experiences an internal error.

[`class InvalidArgumentError`](../tf/errors/InvalidArgumentError): Raised when an operation receives an invalid argument.

Constant NOT_FOUND

[`class NotFoundError`](../tf/errors/NotFoundError): Raised when a requested entity (e.g., a file or directory) was not found.

Constant OK

Constant OUT_OF_RANGE

[`class OpError`](../tf/OpError): A generic error that is raised when TensorFlow execution fails.

[`class OutOfRangeError`](../tf/errors/OutOfRangeError): Raised when an operation iterates past the valid input range.

Constant PERMISSION_DENIED

[`class PermissionDeniedError`](../tf/errors/PermissionDeniedError): Raised when the caller does not have permission to run an operation.

Constant RESOURCE_EXHAUSTED

[`class ResourceExhaustedError`](../tf/errors/ResourceExhaustedError): Some resource has been exhausted.

Constant UNAUTHENTICATED

Constant UNAVAILABLE

Constant UNIMPLEMENTED

Constant UNKNOWN

[`class UnauthenticatedError`](../tf/errors/UnauthenticatedError): The request does not have valid authentication credentials.

[`class UnavailableError`](../tf/errors/UnavailableError): Raised when the runtime is currently unavailable.

[`class UnimplementedError`](../tf/errors/UnimplementedError): Raised when an operation has not been implemented.

[`class UnknownError`](../tf/errors/UnknownError): Unknown error.

[`error_code_from_exception_type(...)`](../tf/errors/error_code_from_exception_type)

[`exception_type_from_error_code(...)`](../tf/errors/exception_type_from_error_code)

[`raise_exception_on_not_ok_status(...)`](../tf/errors/raise_exception_on_not_ok_status)

Defined in [`tensorflow/python/framework/errors.py`](https://www.tensorflow.org/code/tensorflow/python/framework/errors.py).

