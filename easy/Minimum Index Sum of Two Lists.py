class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # li1_dict = {k: i for i, k in enumerate(list1)}
        # li2_dict = {k: i for i, k in enumerate(list2)}
        # list1.sort()
        # list2.sort()
        # min_idx = float('inf')
        # ans = []
        # for i in li1_dict:
        #     if i in li2_dict:
        #         idx_sum = li1_dict[i] + li2_dict[i]
        #         min_idx = idx_sum if idx_sum < min_idx else min_idx
        #
        # for i in li1_dict:
        #     if i in li2_dict:
        #         if li1_dict[i] + li2_dict[i] == min_idx:
        #             ans.append(i)
        # return ans

        li1_dict = {k: i for i, k in enumerate(list1)}
        min_idx = float('inf')
        ans = []
        for j, li2 in enumerate(list2):
            if li2 in li1_dict:
                i = li1_dict[li2]
                if j + i < min_idx:
                    min_idx = j + i
                    ans = [li2]
                elif j + i == min_idx:
                    ans.append(li2)
        return ans


s = Solution()
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])) # ['Shogun']
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"])) # ["Shogun"]
print(s.findRestaurant(["happy","sad","good"], ["sad","happy","good"])) # ["sad","happy"]
