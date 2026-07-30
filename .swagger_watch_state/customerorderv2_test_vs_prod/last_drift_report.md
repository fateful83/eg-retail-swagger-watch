# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-30T01:07:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3ce32f4dc460b4211e78d48c295ae4b3677de73c82a7ee1fd68069ef816f6575`
- PROD hash: `06f987b0bbefea2a7db85edb27c6af7c217932ceba673e8d48b6da803f92e6c9`

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
