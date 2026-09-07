# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-07T16:42:32Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `281d0ab1acab90473244003fe5510baff77a6b984ab3af7f0ee27897f2f5dc37`
- PROD hash: `13becf9484bb89b33ac7ef410be06aacc92385f267a779f2ebbff0030c9e4903`

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
