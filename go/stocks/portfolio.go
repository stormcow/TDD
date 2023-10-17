package stocks

import "errors"

type Portfolio []Money

func (p Portfolio) Add(money Money) Portfolio {
	p = append(p, money)
	return p
}

func createFailureMessage(failedConversions []string) string {
	failures := "["
	for _, f := range failedConversions {
		failures = failures + f + ","
	}
	failures = failures + "]"
	return failures
}

func (p Portfolio) Evaluate(bank Bank, currency string) (*Money, error) {
	total := NewMoney(0, currency)
	failedConversions := make([]string, 0)

	for _, m := range p {
		if convertedCurrency, err := bank.Convert(m, currency); err == nil {
			// total = total + convertedCurrency.amount
			total = *total.Add(convertedCurrency)
		} else {
			failedConversions = append(failedConversions, err.Error())
		}
	}

	if len(failedConversions) == 0 {
		return &total, nil
	}

	failures := createFailureMessage(failedConversions)

	return nil, errors.New("Missing exchange rate(s):" + failures)
}
