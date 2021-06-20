


import pandas as pd
import numpy as np



data = pd.read_csv("C:\\Users\\r.pan\\Desktop\\CSUF\\577\\data\\_output.csv")
zcode = pd.read_csv("C:\\Users\\r.pan\\Desktop\\CSUF\\577\\data\\Orange_County_zipcodes.csv")


def match(data,zcode):
    data["Zipcode"]= ""
    data1 = data.to_numpy()
    zcode1 = zcode.to_numpy()
    
    for i in range(len(data1)):
        lat = data1[i][1]
        long = data1[i][2]
        print("strating to match zipcode zone for record # {}, lat: {}, long: {}!".format(i,lat,long))
        min_dis = np.inf
        zipcode = 11111 
        for z in range(len(zcode1)):
            lat1 = zcode1[z][1]
            long1 = zcode1[z][2]
            zip1 = zcode1[z][0]
            print("checking numer "+ str(z) + " record of OC zipcode to see if it matches lat "+ str(lat) + " and long "+ str(long))

            distance = np.sqrt((lat-lat1)**2 + (long-long1)**2)
            if distance < min_dis :
                min_dis = distance
                zipcode = int(zip1)
            else:
                next 
        data1[i][-1] = zipcode
        print('finish looping through OC Zipcode and added {} possible match(es) for record # {}'.format(zipcode,i))


#     print(data1)
    return data1



output = match(data,zcode)


cols = list(data.columns)
cols[0] = "ID"

df = pd.DataFrame(output, columns = cols)




df.to_csv("C:\\Users\\r.pan\\Desktop\\CSUF\\577\\test1.csv")

