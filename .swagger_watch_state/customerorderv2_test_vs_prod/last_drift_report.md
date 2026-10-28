# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-28T11:43:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `eb1428fa429d347b963742dc906d73c979ffe586e153fdeb890de9164146397c`
- PROD hash: `cbf98c136e183a1a16480ab6ef3c4b5d05733eb960be09bac51d5e7e3072fa5b`

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
