# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-26T19:27:29Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5ff5fd844743d4a192fd26953679d6908249fc50721d636e893dc5a5aeb7864e`
- PROD hash: `1f0e445fc11b5b28dc71ba616811de5913f3b9beb9bab7cf15b5dffa7077de53`

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
