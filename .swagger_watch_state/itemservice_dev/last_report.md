# Swagger/OpenAPI change detected: ItemService [DEV]

- Time: 2026-05-26T01:49:41Z
- Fetch completed at: 2026-05-26T01:49:41Z
- Fetch duration ms: 18799
- Swagger URL: https://itemservice.egretail-dev.cloud/swagger/v1/swagger.json
- Previous hash: `0101ea464a563c1e4f8705e70dfb3db0c4e2311bd8b44138d51f85a04e4da16f`
- Current hash: `995ece27122a64af32ec2f8c256acb3cbf0fcbba47e02e917a12b162d0d9eb9a`

## Summary
- Status: breaking
- Added operations: 0
- Removed operations: 10
- Changed operations: 0
- Breaking removed operations: 10
- Breaking changed operations: 0
- Non-breaking changed operations: 0

## Added
- None

## Removed
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

## Changed
- None

## Breaking classification
- Removed operations: 10
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

- Breaking changed operations: 0
- None

- Non-breaking changed operations: 0
- None
