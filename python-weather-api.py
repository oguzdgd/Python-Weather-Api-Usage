import requests

# Weatherstack API anahtarını buraya ekleyin
API_KEY = 'd3f3cce0d0fba4f748ed67543322b946'

def hava_durumu_sorgula(sehir):
    base_url = "http://api.weatherstack.com/current"
    complete_url = f"{base_url}?access_key={API_KEY}&query={sehir}"

    response = requests.get(complete_url)
    data = response.json()

    if "current" in data:
        current_data = data["current"]
        sıcaklık = current_data["temperature"]
        nem_orani = current_data["humidity"]
        hava_durumu = current_data["weather_descriptions"][0]

        print(f"Hava Durumu: {hava_durumu}")
        print(f"Sıcaklık: {sıcaklık} °C")
        print(f"Nem Oranı: {nem_orani}%")
    else:
        print("Şehir bulunamadı veya hava durumu bilgileri alınamadı.")

if __name__ == "__main__":
    sehir = input("Hava durumu bilgisini almak istediğiniz şehri girin: ")
    hava_durumu_sorgula(sehir)
