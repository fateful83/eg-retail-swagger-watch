# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-10T16:25:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `062d29f218fb0360e1c04c0a9e72ff7c2e3666d23e1b0e6144ca72ff0566452a`
- PROD hash: `957bc290410c23b9255825beac1f640e07cc8bde087edff015b5efe2c518b2d6`

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
