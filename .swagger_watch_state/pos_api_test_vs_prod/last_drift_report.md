# TEST vs PROD drift detected: POS API

- Time: 2026-10-28T21:56:20Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ce201de3fd6c4c70d8aa3854d42f7cd8d7b7c7e72850d6eedaa7e3d923ba6c70`
- PROD hash: `5d6c216c6753ab38565be0d1897ff829a1a796746997ca6f6059bd9779c52148`

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
