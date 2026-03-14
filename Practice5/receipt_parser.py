import re
def solve_tasks():
        with open('raw.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.splitlines()

        # 1
        print("1. 'ab*':", re.findall(r'ab*', content)[:5])

        # 2
        print("2. 'ab{2,3}':", re.findall(r'ab{2,3}', content)[:5])

        # 3
        print("3. snake_case:", re.findall(r'[a-z]+_[a-z]+', content)[:5])

        # 4
        print("4. Upper + lower:", re.findall(r'[A-Z][a-z]+', content)[:5])

        # 5
        task5 = [l for l in lines if re.search(r'^a.*b$', l)]
        print("5. Start 'a', end 'b':", task5[:3])

        # 6
        print("6. Replace:", re.sub(r'[ ,.]', ':', content[:50]))

        # 7
        def to_camel(s):
            words = s.split('_')
            return words[0] + ''.join(w.capitalize() for w in words[1:])
        print("7. Snake to Camel:", to_camel("snake_case_string"))
        
        # 8
        print("8. Split at Upper:", re.findall(r'[A-Z][^A-Z]*', "SplitThisString"))

        # 9
        print("9. Insert spaces:", re.sub(r"(\w)([A-Z])", r"\1 \2", "InsertSpacesHere"))

        # 10
        def to_snake(s):
            return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
        print("10. Camel to Snake:", to_snake("CamelCaseString"))

if __name__ == "__main__":
    solve_tasks()