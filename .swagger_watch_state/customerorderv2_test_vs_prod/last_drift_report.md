# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-08T01:15:56Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8dcf678019a1444a13dbb14b176488030d249eb5b4eb07d9804a71d7d19af2a2`
- PROD hash: `a3a11ab6f557f03eb59155a770df36198a68d2e0eb9a7c6e5249557d7c7851ec`

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
