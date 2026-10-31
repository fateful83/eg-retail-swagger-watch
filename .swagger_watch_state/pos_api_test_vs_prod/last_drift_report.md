# TEST vs PROD drift detected: POS API

- Time: 2026-10-31T20:43:21Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d1b7a95be04f9f2d0c4924de96a20f409d75fb4f903dc2917015962f90e4543b`
- PROD hash: `675022137112385fab0e14a7b72ad6a7c82238ec14cbe9db5832217475ed1b51`

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
