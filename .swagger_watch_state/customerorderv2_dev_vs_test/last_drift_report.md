# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-04T14:23:56Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `76661fb3071d4e1f013416f71f1c5c9ef32c4d67cf69521e4d696cc727cf508d`
- TEST hash: `0cd05a8e8ef9eb7fa84a7b1e27e1f63afa813d71b3b47ccc6806d280d2d04358`

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
