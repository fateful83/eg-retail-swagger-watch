# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-05T01:29:45Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5b9caaa4909320eb55c85a51e5ed78b41e0b456530e80a27d30b98088ad07cb0`
- PROD hash: `952d645a8e56418909562b43f5767709e21ab544b6a0011bd35f354b7c516ad9`

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
