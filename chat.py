from fractions import Fraction

def add_fractions(num1, den1, num2, den2):
    result = Fraction(num1, den1) + Fraction(num2, den2)
    return result.numerator, result.denominator

def subtract_fractions(num1, den1, num2, den2):
    result = Fraction(num1, den1) - Fraction(num2, den2)
    return result.numerator, result.denominator
print("Сложение дробей: ", add_fractions(num1, den1, num2, den2))

if name == "main":
    main()
