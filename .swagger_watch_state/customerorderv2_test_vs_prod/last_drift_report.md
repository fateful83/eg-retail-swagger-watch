# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-23T19:45:20Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d783d8d85b17ef223c92dca959036cf63385514243743efd13ea1875cedada2b`
- PROD hash: `ceec8167b6954e6d25f8129387d221e4ca8204ee7c1df4eb3b129049b9f80a2a`

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
