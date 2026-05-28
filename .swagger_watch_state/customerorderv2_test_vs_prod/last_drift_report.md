# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-28T14:57:56Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b7dc4a8be9223d0e9239a8764f8151b63f263961ad9859aa4771234972eb5353`
- PROD hash: `4926b6aec4b2e5434ce08192d8787a90dcf34a916f7c5be65464a04c75edd6d1`

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
