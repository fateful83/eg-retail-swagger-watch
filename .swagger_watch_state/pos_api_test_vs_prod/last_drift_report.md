# TEST vs PROD drift detected: POS API

- Time: 2026-10-30T17:17:14Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b5b3a883f1e18386b13673691a220d809cd6af98bfac80766cd408e57b714ed0`
- PROD hash: `1bce70816fd238a4699a0c70f817a4ed0ce55ce2ef5bffa2e572af034c2de5eb`

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
