# TEST vs PROD drift detected: POS API

- Time: 2026-11-02T14:00:36Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3ac36cef81137c87e11e105a6fe8f084c79c06266757327ed167bcbb26e34d36`
- PROD hash: `b1c7b96d32c30f95f752b53dbf25c4f87eee0a316aff8307eb7ae4ccf5009c67`

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
