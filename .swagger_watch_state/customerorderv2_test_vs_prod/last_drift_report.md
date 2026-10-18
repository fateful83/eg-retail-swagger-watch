# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-18T09:59:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `10794ff4bf5090520dd3429957ad77dc8b192db2e85ca649cc6cee274ec50da4`
- PROD hash: `954e55935610d9fd5d23b602d21bfe14c6d55e04238f48e6d7386142ce82f83f`

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
