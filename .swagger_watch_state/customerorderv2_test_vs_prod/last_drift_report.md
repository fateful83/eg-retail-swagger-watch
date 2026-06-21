# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-21T19:08:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6e90582fff804cab179b0010c05ab86a7aa96db777db886722f7303962d27bb8`
- PROD hash: `570a86765c0952525650bab2f2dcfdb35a4544d31850d0b32ef76ade5823b66e`

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
