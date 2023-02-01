
"""
data_dict = {"years" :
            { "year" : "2023", "months":
            { "month" : "January", "days" :
            {"day" :
            {"no" : "1" , "workout" : "test"}}}}}
"""
data_dict =  {"days" : { "day" : { "no" : "1" , "workout" : "test"}}}
text = "Januar 2023"

#month, year = text.split(" ")
#data_dict["years"]["year"]["month"] = month
#data_dict["year"] = year

# add day to data_dict
data_dict.update(["days"]["day"]["no"] = "1")
print(data_dict)
