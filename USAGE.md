<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->