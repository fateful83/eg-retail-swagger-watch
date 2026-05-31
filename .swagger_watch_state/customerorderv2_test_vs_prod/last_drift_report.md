# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-31T08:30:51Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1c03b6c024dc94cb32b76e9f3886ee8864330effc210b4c8226c86007b44b72c`
- PROD hash: `be4c7f1dca736bf4ee7ee2bec2792d96ab7d4034948fc13ebf2a7e5e2f869fd0`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/gateway/ServiceOrders/{storeNumber}

## Only in PROD
- None

## Different in TEST and PROD
- None
