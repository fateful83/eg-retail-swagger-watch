# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-07T02:02:43Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `111968d0acaa6a4fa53707e69df43230911cb9676846006aad5d01cb1dcc0f44`
- TEST hash: `ceb83d61b1917c114c12d1423078df0efa481b7413bd5ae838e00357fdcbc54d`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/order-status

## Only in TEST
- None

## Different in DEV and TEST
- None
