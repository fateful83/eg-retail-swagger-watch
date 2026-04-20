# DEV vs TEST drift detected: POS API

- Time: 2026-04-20T01:15:33Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `0834085368aacbb7d7eae4f4da1570aa0cadd9ef6edf08dfb9315905181dffaf`
- TEST hash: `98b4df4c1f9b42d1ca5a2e34c4fa8ba57554c0912217b92b87fb61366ec6ca79`

## Summary
- Only in DEV: 0
- Only in TEST: 1
- Present in both but different: 0

## Only in DEV
- None

## Only in TEST
- POST /api/Payment/AddBonusPaymentToCart

## Different in DEV and TEST
- None
