# SimpleCalculator
(*simple_calculator*)

### Available Operations

* [calculate](#calculate) - Calculate

## calculate

Calculates the expression using the specified operation.

### Example Usage

```python
import calculator
from calculator.models import operations, shared

s = calculator.Calculator()

req = operations.CalculateRequest(
    operation=shared.OperationType.SUBTRACT,
    x=3946.69,
    y=6431.33,
)

res = s.simple_calculator.calculate(req)

if res.res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.CalculateRequest](../../models/operations/calculaterequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CalculateResponse](../../models/operations/calculateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
