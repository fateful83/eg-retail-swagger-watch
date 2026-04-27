# TEST vs PROD drift detected: POS API

- Time: 2026-04-27T19:00:25Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9edd9d953482420bf847bc03ae229e28ed5a30b6d2ddf5d2ffb601d22dd2ae70`
- PROD hash: `969ca1f13d8434dabbc263a24df5d691ff1430c86925dcd7b5ce806c2b3668c8`

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
