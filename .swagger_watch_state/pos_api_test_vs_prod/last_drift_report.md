# TEST vs PROD drift detected: POS API

- Time: 2026-04-24T12:50:30Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `17dabc62fdca9d9611b0348da6687b812c7d31c2f9e077524cceec67b514bba6`
- PROD hash: `63711de8800547654569f58ca846f479085ad1ce7e97f3060d110e3defdeac1c`

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
