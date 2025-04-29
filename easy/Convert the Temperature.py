from decimal import Decimal, getcontext


class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        getcontext().prec = 11
        celsius = Decimal(celsius)
        kelvin = celsius + Decimal('273.15')
        fahrenheit = celsius * Decimal(1.8) + Decimal('32')
        return [kelvin.quantize(Decimal('0.00001')), fahrenheit.quantize(Decimal('0.00001'))]


s = Solution()
print(s.convertTemperature(36.50)) # [309.65000,97.70000]
print(s.convertTemperature(122.11)) # [395.26000,251.79800]
