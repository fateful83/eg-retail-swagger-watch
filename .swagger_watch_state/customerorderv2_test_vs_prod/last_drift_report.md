# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-06T14:48:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `90624b0a94e7f22a7eeb73d5b7996541b84e13baf7ee8f52122820afee4bff1b`
- PROD hash: `bee0d736536d5303508013cbc718caef49fa1ad0f9dd9bf4f979bf1c455ff203`

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
