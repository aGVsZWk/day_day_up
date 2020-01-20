class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(key= lambda x: -x)
        answer = len([people.remove(i) for i in people if i == limit])

        while people:
            i, j = 0, len(people) - 1
            if i != j:
                if people[i] + people[j] > limit:
                    people.pop(i)
                    answer += 1
                elif people[i] + people[j] <= limit:
                    people.pop(j)
                    people.pop(i)
                    answer += 1
            else:
                answer += 1
                people.pop(i)
        return answer


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(key= lambda x: -x)
        answer = 0
        while people:
            i, j = 0, len(people) - 1
            if people[i] + people[j] > limit:
                people.pop(i)
                answer += 1
            elif i != j:
                people.pop(j)
                people.pop(i)
                answer += 1
            else:
                people.pop(i)
                answer += 1
        return answer


# 上面两种都很慢
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(reverse=True)
        answer = 0
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                i += 1
            answer += 1
        return answer


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if len(people) == 0:
            return 0

        people = sorted(people)
        count = 0
        while people:
            a = people.pop()
            if people and a + people[0] <= limit:
                people.pop(0)

            count += 1

        return count
