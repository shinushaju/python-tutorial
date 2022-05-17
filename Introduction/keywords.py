# Python Keywords

# importing "keyword" for keyword operations
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is: ")
print(keyword.kwlist)
print()
print("The number of keywords is: ")
print(len(keyword.kwlist))

# The 'keyword.iskeyword()' checks whether a string is a keyword or not
print(keyword.iskeyword('While'))