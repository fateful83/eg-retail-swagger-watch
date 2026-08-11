# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-11T06:40:51Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fa54466243d1c452dac5b00e36a684ef1a33d4c4cd7183ad680f83e54e49bfbb`
- PROD hash: `b97666ea97676932fc799c610ae02ea457460342a9fbcaf0dcf60268d2db123a`

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
