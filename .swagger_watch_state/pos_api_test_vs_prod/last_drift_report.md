# TEST vs PROD drift detected: POS API

- Time: 2026-11-01T02:42:48Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `383b614488925102f9b341dc52e6f0fe68ce4d3be28ec87d50474ff7c81150fe`
- PROD hash: `516f9527f1a2beab1b7f38d3dd8183bc68e645c904cd926e695eff24605375e6`

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
