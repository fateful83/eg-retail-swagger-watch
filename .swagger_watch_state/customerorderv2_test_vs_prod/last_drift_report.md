# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-16T13:09:23Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ecbff3fe7e322b9f4740b4e846a68fb7c943dd238a65934b35feb142fcfaf898`
- PROD hash: `a2961150aa6a7ab914a82dbb84de37b2fe92e50b9a8491b8cd56321b640a38cc`

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
