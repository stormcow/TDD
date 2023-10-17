package stocks

type Money struct {
	amount   float64
	currency string
}

func (m Money) Times(multiplier int) Money {
	return Money{amount: m.amount * float64(multiplier), currency: m.currency}
}

func (m Money) Divide(divisor int) Money {
	return Money{amount: m.amount / float64(divisor), currency: m.currency}
}

func (m Money) Add(other *Money) *Money {
	if m.currency == other.currency {
		m.amount += other.amount
		sum := NewMoney(m.amount, m.currency)
		return &sum
	}
	return nil
}

func NewMoney(amount float64, currency string) Money {
	return Money{amount, currency}
}
