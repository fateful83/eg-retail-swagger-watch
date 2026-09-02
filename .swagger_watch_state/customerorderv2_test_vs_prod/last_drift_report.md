# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-02T15:23:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `25f9350d308d69494e8a34ed906dc4e541c2b95661de579d8c73d27cf4ceb54d`
- PROD hash: `b502c4606ca3d861deacda1604a9d3290177859bc8078098c15eb94abe7c0faf`

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
