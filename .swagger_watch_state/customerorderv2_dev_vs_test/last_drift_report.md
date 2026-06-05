# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-05T01:57:53Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `f98432047db164bc630309f9d23c461d64c7afb1e00ed97d7abe22be6f517c2a`
- TEST hash: `c9d836b4b41d236522c253b7c8da6a9fec5329783cab5a7852addae5e2093f02`

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
