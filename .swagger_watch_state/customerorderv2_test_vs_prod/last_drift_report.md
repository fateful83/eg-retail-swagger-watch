# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-18T06:19:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c543f312b9a47bec08abe97726b08820066f3324aa0486af80dedc5139c1d0ba`
- PROD hash: `31437d183a9c2c22947fd30d6accd810c01398a797a6d01cd676ecea3e898ebd`

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
