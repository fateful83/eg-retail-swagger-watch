# TEST vs PROD drift detected: ItemService

- Time: 2026-05-29T20:01:46Z
- Severity: breaking
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://itemservice.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `995ece27122a64af32ec2f8c256acb3cbf0fcbba47e02e917a12b162d0d9eb9a`
- PROD hash: `0101ea464a563c1e4f8705e70dfb3db0c4e2311bd8b44138d51f85a04e4da16f`

## Summary
- Only in TEST: 0
- Only in PROD: 10
- Present in both but different: 0

## Only in TEST
- None

## Only in PROD
- GET /api/CalculationRulesets
- GET /api/CalculationRulesets/DefaultRuleset
- GET /api/CalculationRulesets/{id}
- GET /api/Imports/{id}/calculationRuleset
- GET /api/PriceCalculations/StorePriceCalculations
- GET /api/RetailPriceCalculationRules
- POST /api/StorePrices/GetCorrelatedPrices
- POST /api/StorePrices/GetPriceCounts
- POST /api/StorePrices/PriceDateValidate
- POST /api/StorePrices/{id}/Copy

## Different in TEST and PROD
- None
