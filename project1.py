location=input("What is your location?: ")
pm25= int(input("What is the PM2.5?: "))
pm10= int(input("What is the PM10?: "))
no2= int(input("What is the N02?: "))
so2= int(input("What is the SO2?: "))
co= int(input("What is the CO?: "))

def aqi_equation(Ihigh,Ilow,Chigh,Clow,Cp):
    return (Ihigh-Ilow)/(Chigh-Clow)*(Cp-Clow)+Ilow

if pm25 < 0 or pm25 > 500.4:
    print("PM2.5 Value is incorrect")
elif pm10 <0 or pm10 > 604:
    print("PM10 value is incorrect")
elif no2 < 0 or no2 > 2049:
    print("NO2 value is incorrect")
elif so2 <0 or so2 > 1004:
    print("SO2 Value is incorrect")
elif co < 0 or co > 50.4:
    print("CO value is incorrect")

if pm25 <= 12:
    aqiPM25 = aqi_equation(50, 0, 12, 0, pm25)
elif pm25 <= 35.4:
    aqiPM25 = aqi_equation(100, 51, 35.4, 12.1, pm25)
elif pm25 <= 55.4:
    aqiPM25 = aqi_equation(150, 101, 55.4, 35.5, pm25)
elif pm25 <= 150.4:
    aqiPM25 = aqi_equation(200, 151, 150.4, 55.5, pm25)
elif pm25 <= 250.4:
    aqiPM25 = aqi_equation(300, 201, 250.4, 150.5, pm25)
elif pm25 <= 500.4:
    aqiPM25 = aqi_equation(500, 300, 500.4, 250.5, pm25)

if pm10 <= 54:
    aqiPM10 = aqi_equation(50, 0, 54, 0, pm10)
elif pm10 <= 154:
    aqiPM10 = aqi_equation(100, 51, 100, 55, pm10)
elif pm10 <= 254:
    aqiPM10 = aqi_equation(150, 101, 254, 155, pm10)
elif pm10 <= 354:
    aqiPM10 = aqi_equation(200, 151, 354, 255, pm10)
elif pm10 <= 424:
    aqiPM10 = aqi_equation(300, 201, 434, 355, pm10)
elif pm10 <= 604:
    aqiPM10 = aqi_equation(500, 301, 604, 425, pm10)
    
if no2 <= 53:
    aqiNO2 = aqi_equation(50, 0, 53, 0, no2)
elif no2 <= 100:
    aqiNO2 = aqi_equation(100, 51, 100, 54, no2)
elif no2 <= 360:
    aqiNO2= aqi_equation(150, 101, 360, 101, no2)
elif no2 <= 649:
    aqiNO2 = aqi_equation(200, 151, 649, 361, no2)
elif no2 <= 1249:
    aqiNO2 = aqi_equation(300, 201, 1249, 650, no2)
elif no2 <= 2049:
    aqiNO2 = aqi_equation(500, 301, 2049, 1250, no2)

if so2 <= 35:
    aqiSO2 = aqi_equation(50, 0, 35, 0, so2)
elif so2 <= 75:
    aqiSO2 = aqi_equation(100, 51, 75, 36, so2)
elif so2 <= 185:
    aqiSO2 = aqi_equation(150, 101, 185, 76, so2)
elif so2 <= 304:
    aqiSO2 = aqi_equation(200, 151, 304, 186, so2)
elif so2 <= 604:
    aqiSO2 = aqi_equation(300, 201, 604, 305, so2)
elif so2 <= 1004:
    aqiSO2 = aqi_equation(500, 301, 1004, 605, so2)

if co <= 4.4:
    aqiCO = aqi_equation(50, 0, 4.4, 0, co)
elif co <= 9.4:
    aqiCO = aqi_equation(100, 51, 9.4, 4.5, co)
elif co <= 12.4:
    aqiCO = aqi_equation(150, 101, 12.4, 9.5, co)
elif co <= 15.4:
    aqiCO = aqi_equation(200, 151, 15.4, 12.5, co)
elif co <= 30.4:
    aqiCO = aqi_equation(300, 201, 30.4, 15.5, co)
elif co <= 50.4:
    aqiCO = aqi_equation(500, 301, 50.4, 30.5, co)

print(location)
print("AQI for pm2.5 is: ",round(aqiPM25))
print("AQI for pm10 is: ",round(aqiPM10))
print("AQI for NO2 is: ",round(aqiNO2))
print("AQI for SO2 is: ",round(aqiSO2))
print("AQI for CO is: ",round(aqiCO))
print("The final AQI is: ", round(max(aqiPM25,aqiPM10,aqiNO2,aqiSO2,aqiCO)))
