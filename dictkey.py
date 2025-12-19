#Get the key of a minimum value

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
min = None
result = None
for key in sample_dict.keys():
    if min is None:
        min = sample_dict[key]
        result = key
    else:
        if sample_dict[key] < min:
            min = sample_dict[key]
            result = key
print(result)
print(min)

