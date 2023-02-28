data = {'Device_Type': ['AXO145', 'TRU151', 'ZOD231', 'YRT326', 'LWR245'], 'Stats_Access_Link': ['<url>https://xcd32112.smart_meter.com</url>',
                                                                                                 '<url>http://tXh67.dia_meter.com</url>',
                                                                                                 '<url>http://yT5495.smart_meter.com</url>',
                                                                                                 '<url>https://ret323_Tru.crown.com</url>',
                                                                                                 '<url>https://luwr3243.celcius.com</url>']}

for index, adress in enumerate(data['Stats_Access_Link']):
    adress = adress.replace('<url>', '').replace('</url>', '').replace('http://', '').replace('https://', '')
    print(data['Device_Type'][index], adress)
