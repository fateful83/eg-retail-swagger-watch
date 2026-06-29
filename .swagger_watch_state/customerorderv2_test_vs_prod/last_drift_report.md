# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-29T10:14:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b99fc58b614321e853c5047d3354bf2d49f3614405629ad7c0032255b670de7a`
- PROD hash: `76bda7f3d07665b0bb685aedbb56dd0e661221cbf3136f0b29ba4b40aeb474ca`

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
