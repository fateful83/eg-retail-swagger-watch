# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-21T20:57:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3daa3234e528a1f8ac196dd50bca3acb39270f5b97735162c0b397e1066bf475`
- PROD hash: `529c49e3d4469af2bdc7955a12516d5aa904eed91c8e8a1611aab75a9976af08`

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
