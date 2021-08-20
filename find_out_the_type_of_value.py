import re

#Самый простой вариант1*********************************************************************************************************************
#data={
#
#             "data1.1":1,
#             "data1.2":2,
#             "res":'ok',
#             "data3":3
#      }
#
# print(*data.keys())
# list_arr=list(data)
# key_value='res'
# key_name='ok'
# i=0
# for i in list_arr:
#     key_name=i
#     key_value=data[i]
#     if key_value and key_name:
#         print('Hooray')
#         break
#
#     print(key_name,key_value)
#
# print('next')

#Самый простой вариант2****************************************************************************************************************
data2=[
    {
        "name1":"abc",
        "name2":"dfg",
        "res":"ok",
    },
    {
        "name3":"sfd",
        "name4":[
            {"name4.1.":"poi"},
            {
            "name4.1.1":"poi",
             "res":"ok"}
            ],
        "res":"ok"
    }
]
print(type(data2))
data2_str=str(data2)
#print(data2_str)
res=re.findall(r'\'res\'\: \'ok\'',data2_str)
#print(res)
count_res_in_dict=res.__len__()
print("'res':'ok' - встречается в дикте ", count_res_in_dict,"раз/а")
print("Вот путь к этим элементам")
i=0
z=0
data2_list=list(data2)
data2_len=data2_list.__len__()
while i<data2_len:
    data2_list[i]=dict(data2_list[i])
    dict_keys=data2_list[i].keys()
    dict_keys_len=dict_keys.__len__()
    dict_keys=list(dict_keys)
    while z < dict_keys_len:
            key_name=dict_keys[z]
            key_value=data2[i][key_name]
            if key_name=='res' and key_value=='ok':
                print("data2[",i,"]['",key_name,"']")
                break
            z+=1

    i+=1


#******************************************************************************************************************

#
# response=requests.get("https://6117d75e30022f0017a05ff1.mockapi.io/api/v1/Dict1").__dict__
# print(response)
# print(response.keys())

