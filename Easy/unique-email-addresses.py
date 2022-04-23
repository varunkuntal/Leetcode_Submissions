# Problem URL: https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        new = {}
        for i in emails:
            local, domain = i.split("@")
            local = "".join(local.split("."))
            local = local.split("+")[0]
            new[f"{local}@{domain}"]=1
            
        return len(new.keys())