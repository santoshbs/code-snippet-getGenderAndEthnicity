############################################################################################
# Created on Mon Jan 24 2022;
# @author: santoshbs;
# @purpose: Infer ethnicity based on the last name of a person; 
# @package-used: http://www.digitalhumanities.org/dhq/vol/9/3/000223/000223.html; (r gender package)
# @other notes: https://stackoverflow.com/questions/35183395/genderdata-package-unavailable-for-r-3-2-3 (to install genderdata library)
############################################################################################


library(gender)
library(data.table)
library(stringr)
library(dplyr)

f= './persons.csv' #read the input data file 
df= fread(f)
names(df)
head(df)

df_sub= df[which(df$person_country_code == 'US'), ] #filter as necessary
df_sub$name_first= str_to_title(df_sub$name_first) #to sanitize names into caps

persons= unique(df_sub$name_first)
inferred_gender= gender(persons, method= 'ssa') #call the gender package
head(inferred_gender)
inferred_gender= inferred_gender[, c("name", "gender", "proportion_male", "proportion_female")]
colnames(inferred_gender)= c("name_first", "person_gender_inferred", "person_gender_inferred_proportion_male", "person_gender_inferred_proportion_female")
head(inferred_gender)

df_sub_gender= left_join(df_sub, inferred_gender)
df_sub_gender$person_gender_inferred[is.na(df_sub_gender$person_gender_inferred)]= "unknown"
head(df_sub_gender)
tail(df_sub_gender)
table(df_sub_gender$person_gender_inferred, useNA= "always")

f= './persons_inferred_gender_usingRGenderAPI_v1.csv'
fwrite(df_sub_gender, f)




