class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang_version = ""

        # iterating throuth the address and changing . with [.]
        for i in range(len(address)):
            if address[i] == ".":
                defang_version += "[.]"
                continue
                
            defang_version += address[i]

        return defang_version
        