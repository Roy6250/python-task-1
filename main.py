list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

def merge_lists(list_1, list_2) -> list:

    list_1=sorted(list_1, key=lambda i: i['id'])
    list_2=sorted(list_2, key=lambda i: i['id'])
    list_3=[]
    
    i=0 # pointer for list_1
    j=0 # pointer for list_2

    while(i<len(list_1) and j<len(list_2)):
      # merging the same "id"s
      if(list_1[i]["id"]==list_2[j]["id"]):
        list_3.append(list_1[i]|list_2[j])
        i+=1
        j+=1
      #Adding the smaller "id"
      elif(list_1[i]["id"]>list_2[j]["id"]):
        list_3.append(list_2[j])
        j+=1
      elif(list_1[i]["id"]<list_2[j]["id"]):
        list_3.append(list_1[i])
        i+=1

    # for remaining elements
    while(i<len(list_1)):
        list_3.append(list_1[i])
        i+=1

    while(j<len(list_2)):
        list_3.append(list_2[j])
        j+=1   

    return list_3


list_3 = merge_lists(list_1, list_2)
print(list_3)
