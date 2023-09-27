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
    operation=shared.OperationType.MULTIPLY,
    x=8472.52,
    y=4236.55,
)

res = s.simple_calculator.calculate(req)

if res.calculate_200_text_plain_number is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.CalculateRequest](../../models/operations/calculaterequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CalculateResponse](../../models/operations/calculateresponse.md)**

