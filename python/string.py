param1 = "Macacao fedido na balada"
param2 = "na"

if param2 in param1:
    param1 = param1.replace(param2, "")

print(param1)