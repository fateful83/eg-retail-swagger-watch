# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-31T01:44:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0b211c90d0d23ec093df63acfa46a43f28a6c51609892ac4e1d2fad15d644568`
- PROD hash: `13c18ea64de5a151e5ae6c0bb430837333bdfa48f69de1df4ca92b4dae354916`

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
