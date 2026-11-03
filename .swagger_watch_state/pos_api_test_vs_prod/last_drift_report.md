# TEST vs PROD drift detected: POS API

- Time: 2026-11-03T00:05:49Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fe275ca70b93cbe0932fdcdd8b28919a2a6cb2ea6161ff6438708010644bd4b6`
- PROD hash: `589e8a4ba1e59a9621a76bee9990b4c16a245deaf839e97feb55911cc15fce68`

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
