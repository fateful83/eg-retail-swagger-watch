# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-11T01:33:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4d11f0e8c1b9daadfd5ebb98c973a70c5692ef75aad544e7b80696571b082e0f`
- PROD hash: `53b7be3dae3bf95d5ea126da01c7c00368b87ab78c1afbb5928263c3519281ce`

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
