# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-25T19:09:57Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `baebb75224b775170ae6c33d0cba6580bc15aadad1d214d781be98217b6efe86`
- PROD hash: `1514581505b8689f8bf16dbab2533d0540cdb0a80b7b86381d45f885ef61dba0`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/gateway/ServiceOrders/{storeNumber}

## Only in PROD
- None

## Different in TEST and PROD
- None
