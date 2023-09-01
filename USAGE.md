<!-- Start SDK Example Usage -->


```python
import calculator
from calculator.models import operations, shared

s = calculator.Calculator()

req = operations.CalculateRequest(
    operation=shared.OperationType.MULTIPLY,
    x=5928.45,
    y=7151.9,
)

res = s.simple_calculator.calculate(req)

if res.calculate_200_text_plain_number is not None:
    # handle response
```
<!-- End SDK Example Usage -->