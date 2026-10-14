# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-14T16:01:04Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `be92f78185f25c84e8fe68841321136b1d8729964b76ef87e673b9c0ad045490`
- PROD hash: `85dbae0c7661f1078b083607f1059e3ffee1206d239c6f859a85d9ef15794da3`

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
