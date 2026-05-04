# TEST vs PROD drift detected: POS API

- Time: 2026-05-04T01:23:43Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f17673d2326c8ed16c5004ac3966ba7a22be5c791258943a39356b2702e34fb0`
- PROD hash: `c5caa529b0138e971404a6f6342bd893864790ad48beb2decd3302fe4e0548e8`

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
