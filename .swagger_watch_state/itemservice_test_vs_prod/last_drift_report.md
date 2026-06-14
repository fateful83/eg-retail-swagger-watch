# TEST vs PROD drift detected: ItemService

- Time: 2026-06-14T19:02:18Z
- Severity: breaking
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://itemservice.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7ce7308e9c0402e82b5fa3785a0f7163759dff7958f3f05095f578690f146163`
- PROD hash: `98d3fefa6188b48439efd7663b4d4ca054241a13f56e3765ae56bd465d8dee47`

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
