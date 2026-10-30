# TEST vs PROD drift detected: POS API

- Time: 2026-10-30T11:43:53Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `73f23abae34b9bdebc08a39785d54d3314d270e21daa2c6354f5fb0311b82c07`
- PROD hash: `acb2571c891b1cadb933ebd5ee224cba5323a5376f233ffb696984b50a780d6f`

## Summary
- Only in TEST: 3
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/UserService/PingHealth
- POST /api/UserService/Authenticate
- POST /api/UserService/CheckUserExists

## Only in PROD
- None

## Different in TEST and PROD
- None
