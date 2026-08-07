# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-07T12:33:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f7ccb3cdd4024664f807c108248bc934745de88ee9f5f3634f05ba0de5d7f8bc`
- PROD hash: `0091fdffc5b9548582b091edf1bc045495728ee9048f4a9bb37508e0c6cd4d8c`

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
