# TEST vs PROD drift detected: POS API

- Time: 2026-04-23T01:16:41Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e612b3b7ea25c00d32e2804d63b11671002eb1ccba7bb1b446168a11946f39c6`
- PROD hash: `254dcc65cc14bf4fdd288b46dc200e0fa4c3e934db094425dddfede323cfdc48`

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
