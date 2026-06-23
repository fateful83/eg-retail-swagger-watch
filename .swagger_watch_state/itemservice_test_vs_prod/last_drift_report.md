# TEST vs PROD drift detected: ItemService

- Time: 2026-06-23T08:52:20Z
- Severity: breaking
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://itemservice.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a27f5a097b735452111e44b74f4fd42b1f1c2372f8eaae5947ead2adf973e658`
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
