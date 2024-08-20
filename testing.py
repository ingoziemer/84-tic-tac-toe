import pandas as pd

columns = ["A", "B", "C"]
field = pd.DataFrame(columns=columns, index=range(1, 4))
field["A"] = ""
field["B"] = ""
field["C"] = ""
# print(field)


data = pd.DataFrame({
    'name': ['sravan', 'ojsawi', 'bobby',  'rohith',
             'gnanesh', 'sravan', 'sravan', 'ojaswi'],
    'subjects': ['java', 'php', 'java', 'php', 'java',
                 'html/css', 'python', 'R']
})
print(data)
print(data["subjects"][1])