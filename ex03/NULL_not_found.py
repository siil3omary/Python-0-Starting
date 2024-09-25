def isNaN(num: float):
	return (num != num)


def NULL_not_found(object: any) -> int:
	if type(object) is float and isNaN(object) is True:
		print(f"Cheese: nan {type(object)}")
	elif type(object) is int and object == 0:
		print(f"Zero: 0 {type(object)}")
	elif type(object) is str and object == "":
		print(f"Empty: {type(object)}")
	elif type(object) is bool and object is False:
		print(f"Fake: False {type(object)}")
	elif object is None:
		print(f"Nothing: None {type(object)}")
	else:
		print("Type not Found")
		return 1
	return 0
	

# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ''
# Fake = False
# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))