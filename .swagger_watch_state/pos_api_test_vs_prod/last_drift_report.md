# TEST vs PROD drift detected: POS API

- Time: 2026-10-31T02:50:24Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6fa24e1bb00b21bf4ad68206c166ddd95d08d80c3630524a33dbb6c40a8702bd`
- PROD hash: `4d8cfd351776675d4a699a5f70f5a1fc7710f2e76e6540cca0b51c9318a4f673`

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
