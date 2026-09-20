# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-20T19:52:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7967a74e9ccf5ba076c672e25af72b7da62ca4d105f44a733457c9fc5ef2ff0b`
- PROD hash: `c024fc186ecb8e79b45a7f91472e8299c612435b50011bbc614f6003af11aa2f`

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
