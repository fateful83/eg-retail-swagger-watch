# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-17T19:44:50Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d533651397dc0039d4b6e20ac41a58644df25c0b8774cac777fc00975c9f881c`
- PROD hash: `513f563f3f8c00ae2f348260bb08db22b8fb74e01134971d684df81536cec1e9`

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
