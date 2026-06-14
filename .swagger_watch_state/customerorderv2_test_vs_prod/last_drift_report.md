# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-14T19:02:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2ec6461db183d3b09ccd962516ad48a78d3037cb1315bd7bfd458900f158871a`
- PROD hash: `5b5b75e93db9140c979a27945647137e38c5b9e014ea059f24b6e6c8e6cff00e`

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
