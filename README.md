# calculator

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/calculator.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
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
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [simple_calculator](docs/sdks/simplecalculator/README.md)

* [calculate](docs/sdks/simplecalculator/README.md#calculate) - Calculate
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |


## Example

```python
import calculator
from calculator.models import operations, shared

s = calculator.Calculator()

req = operations.CalculateRequest(
    operation=shared.OperationType.SUBTRACT,
    x=3946.69,
    y=6431.33,
)

res = None
try:
    res = s.simple_calculator.calculate(req)

except (errors.SDKError) as e:
    print(e) # handle exception


if res.res is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://examples.apimatic.io/apps/calculator` | None |

For example:

```python
import calculator
from calculator.models import operations, shared

s = calculator.Calculator(
    server_idx=0,
)

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


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import calculator
from calculator.models import operations, shared

s = calculator.Calculator(
    server_url="https://examples.apimatic.io/apps/calculator",
)

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
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that this sdk makes as follows:

```python
import calculator
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = calculator.Calculator(client: http_client)
```
<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
