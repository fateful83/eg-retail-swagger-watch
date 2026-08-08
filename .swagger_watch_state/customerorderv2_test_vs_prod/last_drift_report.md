# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-08T18:17:16Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bc6540e8f54d844842c2ce62d9c4af2439c447280012e44862bf0003b6cc6c11`
- PROD hash: `a95ad3b1e23bb1477627d3b4f1ead3e0ed6ded9ca2ac05c52477ef9901207a05`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 1

## Only in TEST
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in PROD
- None

## Different in TEST and PROD
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
