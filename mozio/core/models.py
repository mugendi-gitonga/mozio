from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import *

# Create your models here.

class Provider(models.Model):

    L_CHOICES = [
            ('ENGLISH', 'ENGLISH'),
            ('RUSSIAN', 'RUSSIAN'),
            ('FRENCH', 'FRENCH'),
            ('ESPANYOL', 'ESPANYOL'),
            ('GERMAN', 'GERMAN'),
            ('DUTCH', 'DUTCH'),
            ('PORTUGUESE', 'PORTUGUESE'),
            ('SAMI', 'SAMI'),
            ('ITALIAN', 'ITALIAN')
    ]

    C_CHOICES = [
        ('ALL', 'Albania Lek'),
        ('AFN', 'Afghanistan Afghani'),
        ('ARS', 'Argentina Peso'),
        ('AWG', 'Aruba Guilder'),
        ('AUD', 'Australia Dollar'),
        ('AZN', 'Azerbaijan New Manat'),
        ('BSD', 'Bahamas Dollar'),
        ('BBD', 'Barbados Dollar'),
        ('BDT', 'Bangladeshi taka'),
        ('BYR', 'Belarus Ruble'),
        ('BZD', 'Belize Dollar'),
        ('BMD', 'Bermuda Dollar'),
        ('BOB', 'Bolivia Boliviano'),
        ('BAM', 'Bosnia and Herzegovina Convertible Marka'),
        ('BWP', 'Botswana Pula'),
        ('BGN', 'Bulgaria Lev'),
        ('BRL', 'Brazil Real'),
        ('BND', 'Brunei Darussalam Dollar'),
        ('KHR', 'Cambodia Riel'),
        ('CAD', 'Canada Dollar'),
        ('KYD', 'Cayman Islands Dollar'),
        ('CLP', 'Chile Peso'),
        ('CNY', 'China Yuan Renminbi'),
        ('COP', 'Colombia Peso'),
        ('CRC', 'Costa Rica Colon'),
        ('HRK', 'Croatia Kuna'),
        ('CUP', 'Cuba Peso'),
        ('CZK', 'Czech Republic Koruna'),
        ('DKK', 'Denmark Krone'),
        ('DOP', 'Dominican Republic Peso'),
        ('XCD', 'East Caribbean Dollar'),
        ('EGP', 'Egypt Pound'),
        ('SVC', 'El Salvador Colon'),
        ('EEK', 'Estonia Kroon'),
        ('EUR', 'Euro Member Countries'),
        ('FKP', 'Falkland Islands (Malvinas) Pound'),
        ('FJD', 'Fiji Dollar'),
        ('GHC', 'Ghana Cedis'),
        ('GIP', 'Gibraltar Pound'),
        ('GTQ', 'Guatemala Quetzal'),
        ('GGP', 'Guernsey Pound'),
        ('GYD', 'Guyana Dollar'),
        ('HNL', 'Honduras Lempira'),
        ('HKD', 'Hong Kong Dollar'),
        ('HUF', 'Hungary Forint'),
        ('ISK', 'Iceland Krona'),
        ('INR', 'India Rupee'),
        ('IDR', 'Indonesia Rupiah'),
        ('IRR', 'Iran Rial'),
        ('IMP', 'Isle of Man Pound'),
        ('ILS', 'Israel Shekel'),
        ('JMD', 'Jamaica Dollar'),
        ('JPY', 'Japan Yen'),
        ('JEP', 'Jersey Pound'),
        ('KZT', 'Kazakhstan Tenge'),
        ('KPW', 'Korea (North) Won'),
        ('KRW', 'Korea (South) Won'),
        ('KGS', 'Kyrgyzstan Som'),
        ('LAK', 'Laos Kip'),
        ('LVL', 'Latvia Lat'),
        ('LBP', 'Lebanon Pound'),
        ('LRD', 'Liberia Dollar'),
        ('LTL', 'Lithuania Litas'),
        ('MKD', 'Macedonia Denar'),
        ('MYR', 'Malaysia Ringgit'),
        ('MUR', 'Mauritius Rupee'),
        ('MXN', 'Mexico Peso'),
        ('MNT', 'Mongolia Tughrik'),
        ('MZN', 'Mozambique Metical'),
        ('NAD', 'Namibia Dollar'),
        ('NPR', 'Nepal Rupee'),
        ('ANG', 'Netherlands Antilles Guilder'),
        ('NZD', 'New Zealand Dollar'),
        ('NIO', 'Nicaragua Cordoba'),
        ('NGN', 'Nigeria Naira'),
        ('NOK', 'Norway Krone'),
        ('OMR', 'Oman Rial'),
        ('PKR', 'Pakistan Rupee'),
        ('PAB', 'Panama Balboa'),
        ('PYG', 'Paraguay Guarani'),
        ('PEN', 'Peru Nuevo Sol'),
        ('PHP', 'Philippines Peso'),
        ('PLN', 'Poland Zloty'),
        ('QAR', 'Qatar Riyal'),
        ('RON', 'Romania New Leu'),
        ('RUB', 'Russia Ruble'),
        ('SHP', 'Saint Helena Pound'),
        ('SAR', 'Saudi Arabia Riyal'),
        ('RSD', 'Serbia Dinar'),
        ('SCR', 'Seychelles Rupee'),
        ('SGD', 'Singapore Dollar'),
        ('SBD', 'Solomon Islands Dollar'),
        ('SOS', 'Somalia Shilling'),
        ('ZAR', 'South Africa Rand'),
        ('LKR', 'Sri Lanka Rupee'),
        ('SEK', 'Sweden Krona'),
        ('CHF', 'Switzerland Franc'),
        ('SRD', 'Suriname Dollar'),
        ('SYP', 'Syria Pound'),
        ('TWD', 'Taiwan New Dollar'),
        ('THB', 'Thailand Baht'),
        ('TTD', 'Trinidad and Tobago Dollar'),
        ('TRY', 'Turkey Lira'),
        ('TRL', 'Turkey Lira'),
        ('TVD', 'Tuvalu Dollar'),
        ('UAH', 'Ukraine Hryvna'),
        ('GBP', 'United Kingdom Pound'),
        ('USD', 'United States Dollar'),
        ('UYU', 'Uruguay Peso'),
        ('UZS', 'Uzbekistan Som'),
        ('VEF', 'Venezuela Bolivar'),
        ('VND', 'Viet Nam Dong'),
        ('YER', 'Yemen Rial'),
        ('ZWD', 'Zimbabwe Dollar')
    ]


    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=255)
    language = models.CharField(max_length=10, choices=L_CHOICES, default='ENGLISH')
    currency = models.CharField(max_length=30, choices=C_CHOICES, default='ENGLISH')

    def __str__(self):
        return '%s' % (self.name)


class Polygon (models.Model):

    polygon_name = models.CharField(max_length=30)
    polygon_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    polygon_area = PolygonField()
    price = models.IntegerField()

    def __str__(self):
        return '%s' % (self.polygon_name)