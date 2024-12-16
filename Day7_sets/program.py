it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("twitter")
print(it_companies)
# Insert multiple IT companies at once to the set it_companies

it_companies.update(["java","html","data"])
print(it_companies)

# Remove one of the companies from the set it_companies

it_companies.pop()
print(it_companies)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Join A and B
C=A.union(B)
print(C)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets

print(A.isdisjoint(B))

# Join A with B and B with A
c=A.union(B)
d=B.union(A)
print(c)
print(d)

# Delete the sets completely
del C
print(c)