# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-21T18:17:26Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `972511c77a2d2d3eb303b89c5468dc91271907b46929d198a034f6b2329f9cc9`
- PROD hash: `79c8c7d58d52796bfca980d62973d66db11cd9f264805c599fcc6bb6345489b7`

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
