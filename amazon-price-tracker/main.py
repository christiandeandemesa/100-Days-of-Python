import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Alesis-Vortex-Wireless-High-Performance-Controller/dp/B078S9L1VZ/ref=sxin_16_pa_sp_search_thematic_sspa?content-id=amzn1.sym.abea0cd6-ddf4-4d67-9781-9599c1d665fc%3Aamzn1.sym.abea0cd6-ddf4-4d67-9781-9599c1d665fc&cv_ct_cx=keytar&keywords=keytar&pd_rd_i=B078S9L1VZ&pd_rd_r=685be2e7-c074-4538-813c-bad7c630b52f&pd_rd_w=fkRoa&pd_rd_wg=Z7wvB&pf_rd_p=abea0cd6-ddf4-4d67-9781-9599c1d665fc&pf_rd_r=2QB5AJ0HQZVADGRFH648&qid=1691711161&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-2-0cc546a2-7bf2-4d0e-b4ad-0f0d9092fdfc-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "Accept-Language": "en-US,en;q=0.9"
}
BUY_PRICE = 400
MY_EMAIL = "c53539588@gmail.com"
PASSWORD = "dlrlbtrfwrcwkqye"

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = float(price.split("$")[1])
title = soup.find(id="productTitle").get_text().strip()

if price_without_currency < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
