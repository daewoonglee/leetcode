class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        li1_dict = {k: i for i, k in enumerate(list1)}
        li2_dict = {k: i for i, k in enumerate(list2)}
        list1.sort()
        list2.sort()
        min_idx = float('inf')
        i, j = 0, 0
        ans = []
        while i < len(list1) and j < len(list2):
            if list1[i] == list2[j]:
                if li1_dict[list1[i]] + li2_dict[list2[j]] < min_idx:
                    ans = [list1[i]]
                    min_idx = li1_dict[list1[i]] + li2_dict[list2[j]]
                elif li1_dict[list1[i]] + li2_dict[list2[j]] == min_idx:
                    ans.append(list1[i])
                j += 1
            elif list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        return ans


s = Solution()
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])) # ['Shogun']
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"])) # ["Shogun"]
print(s.findRestaurant(["happy","sad","good"], ["sad","happy","good"])) # ["sad","happy"]
