# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-08T15:24:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ac599d9b09ab3bb1afe23aecbaed4a299d72a28a755e5b0834ab58cca8815b33`
- PROD hash: `46fd05ffe55ee2779370b8b3de828eecc035227dcd3a1507bb82014ab47a4e61`

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
