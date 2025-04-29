class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        # 파이썬에선 5자리 맞추지 않고 반환해도 답을 인정
        return [celsius + 273.15, (celsius * 1.8) + 32]


s = Solution()
print(s.convertTemperature(36.50)) # [309.65000,97.70000]
print(s.convertTemperature(122.11)) # [395.26000,251.79800]
