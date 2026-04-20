# TEST vs PROD drift detected: POS API

- Time: 2026-04-20T01:15:33Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `98b4df4c1f9b42d1ca5a2e34c4fa8ba57554c0912217b92b87fb61366ec6ca79`
- PROD hash: `dc9ec0ff2de69f35bc34b8cec081f6bbde19dd20731a7847685ff8c48713e352`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/AddBonusPaymentToCart

## Only in PROD
- None

## Different in TEST and PROD
- None
