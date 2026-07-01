# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-01T09:23:08Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `823650c4570eb4b6161b6192572ae3aae104e7cae85e19c4568fbb0fd3e0989c`
- PROD hash: `296ed73665f1dc169d824d994f10d71886b6fca82e6654080303d615e1403b0e`

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
