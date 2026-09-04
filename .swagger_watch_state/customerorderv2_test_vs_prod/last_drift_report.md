# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-04T01:28:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `47ae69b0484f38f8be46a8ea037c38ce84ddea2b200edae535977687885d886c`
- PROD hash: `50ced59769ca97ff64cecb01fe51ba0c13f3404696313321c6b3cf8c9d17dff3`

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
