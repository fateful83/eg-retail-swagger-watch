# TEST vs PROD drift detected: POS API

- Time: 2026-05-05T07:50:15Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `30a468bc68e2de4fb3127428cf7249b4a79924bdf509ffa324f5d3882bed77df`
- PROD hash: `fcd8dfefbd388356c666919c8b554c9696e9e32e96aa18cc31c6bc339286ab13`

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
