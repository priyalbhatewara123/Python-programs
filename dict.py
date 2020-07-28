# dictionaries are key value pairs...
MLB_team = {
    'colorado' : 'rockies',
    'boston' : 'red sox',
    'minnesota' :'twins',
    'seattle' : 'mariners',
    }
print(MLB_team['seattle'])
#to print all keys
print(MLB_team.keys())
#to print all values
print(MLB_team.values())
#to print all items
print(MLB_team.items())
#to delete something
del MLB_team['colorado']
print(MLB_team)
#alternate
MLB_team.pop('seattle')
print(MLB_team)

print(MLB_team.get('boston1',"it is not present"))

#to copy the dict
dict = MLB_team.copy()
print(dict)
#alternate
dict1 = {}
dict1.update(dict)  #here dict is parameter
print(dict1)
#to change value of a key
dict['boston'] = "priyal"
print(dict)