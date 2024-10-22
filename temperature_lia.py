def konversisuhu(temperature, value):
    if value == 'C':
        temperaturesuhu = (temperature - 32) *5/9
        return temperaturesuhu, 'C'
    else:
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'F'
    
celcius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celcius_temperature, 'F')
print(f"{celcius_temperature}°C dikonversi ke Fahrenheit adalah{temperaturesuhu}°{target_value}")
    
fahrenheit_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah{temperaturesuhu}°{target_value}")