# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-25T12:52:50Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2f427d7eaf7ff492beb0ce76e501495518282e5db9b2d78798e93098e10a1311`
- PROD hash: `fe3ec058e895a43723125d6c5de0c4fbfbe103e2f4b364e1e803a754e2269602`

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
