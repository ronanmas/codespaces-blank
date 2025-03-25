# Mr. Rosenthal Lesson

# record_db = []
# record = {}
# record['age'] = 55
# record_db.append(record)
# record = {}
# record['age'] = 35
# record_db.append(record)
# record = {}
# record['age'] = 48
# record_db.append(record)
# record = {}
# record['age'] = 24
# record_db.append(record)
# print(record_db)
# token = ['age','>','45']
# query_str = "db_entry[" + "'" + token[0] + "'" + "]" + "'" + token[1] + " " + token[2]
# print(query_str)
# for db_entry in record_db:
#   if eval(query_str):
#     print(db_entry)






# Mr. Girsch Lesson

    # String: "..."
    # List: [...]
    # Dictionary: {...}
    # {"kw": value, ...}






# create a list whose elements are the headers from the text file


def is_valid_query(query, headers, types): 
    operators = ['=', '<=','>=', '>','<']

    query_list = query.split()

    for index in range(len(query_list)):
        token = query_list[index]
        print(token)
        if index % 4 == 0:
            if token not in headers:
                print( False, [])
            else:
                location = headers.index(token)
                letter = types[location]
        elif index % 4 == 1 and query_list[index] not in operators:
            return False, []
        elif index % 4 == 2 and letter == 'N' and not query_list[index][0].isdigit(): 
            return False, []
        elif index % 4 == 2 and letter == 'S' and not token[0].isalpha():
            return False, []    
        elif index % 4 == 3 and (token != 'and' or token != 'or'): 
            return False, []
    return True, query_list





    # create a list whose elements are the letters from the 2nd row of the text file

with open("company_db.txt") as f:
    data = f.readlines()

header_list = data[0].split()
print(range(len(header_list)))

type_list = data[1].split()
# print(type_list)

user_query = 'age < 40 and Dept = sales'

is_valid, query_list = is_valid_query(user_query,header_list, type_list) 
print(is_valid, query_list)




db_list = []
for line in data[2:]:
        # split the line of data into parts
    data_list = line.split()


        #    empty dictionary to fill with employee data
    db_dict = {}
    
    # separate the employee data
    db_dict["header_list"]= data_list[0]
    db_dict["gender"] = data_list[1]
    db_dict["age"] = data_list[2]
    db_dict["start_date"] = data_list[3]
    db_dict["salary"] = data_list[4]
    db_dict["dept"] = data_list[5]

        # add the employee dictionary to the database list
    db_list.append(db_dict)

print(db_list)













