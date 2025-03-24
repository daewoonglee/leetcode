class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        ans = []
        min_idx = float('inf')
        for i, li1 in enumerate(list1):
            for j, li2 in enumerate(list2):
                if li1 == li2:
                    if i+j < min_idx:
                        ans = [li1]
                        min_idx = i+j
                    elif i+j == min_idx:
                        ans.append(li1)
        return ans


s = Solution()
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])) # ['Shogun']
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"])) # ["Shogun"]
print(s.findRestaurant(["happy","sad","good"], ["sad","happy","good"])) # ["sad","happy"]
