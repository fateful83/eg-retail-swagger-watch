# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-06T01:24:08Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4c4f044afd89a3db717d7d8dc4201daadfd801c65b9f1fb61e957f40f452a6d4`
- PROD hash: `6b0454dfb42f559b83cc316d7be7f3ec5d6c2824f3e78cbc236a7954f718672c`

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
