# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-19T01:55:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d059d7b4739172dd2e157ddb2d4416b97ed7c4b72455511e4d3f79daa73a2cc9`
- PROD hash: `99aa7e1af6a7889c36751822b62c83bf6370b4b269ebd06dac9ffdc5d950dd98`

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
