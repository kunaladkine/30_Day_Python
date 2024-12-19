"""
syntax: 
for x in y:
    for t in x:
        print(x)
"""

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'}
}

for key in person:
    if key=="skills":
        for skills in person['skills']:
            print(skills)
            
for number in range(6):
    pass

