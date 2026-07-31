# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-31T19:01:08Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d91a0b982d402ef70b0daa56abb5d330808532f01716d9ac0626f01819bc7c56`
- PROD hash: `fa754bd9b24385424cc1e18a41312d0106f156a64002f32ef5af59336d5ae95b`

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
