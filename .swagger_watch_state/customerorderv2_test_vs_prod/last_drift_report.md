# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-24T02:03:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `415acbcb17f459588a5293820f38d04021056639a8b39ac9548d507f9c33d90e`
- PROD hash: `b0280ad40cc14f3dab8d40f786cfccf6322b31a860872fd35b49c5ef66005d7b`

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
