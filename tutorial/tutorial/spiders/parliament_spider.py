import re
import scrapy
import csv, os, json


class ParliamentSpider(scrapy.Spider):
    name = "parliament"
    allowed_domains = ['www.parliament.bg']
    start_urls = [
        'https://www.parliament.bg/bg/MP/'
        # 'https://www.parliament.bg/bg/MP/2797',
        # 'https://www.parliament.bg/bg/MP/2790',
        # # 'https://www.parliament.bg/bg/MP/2753'
    ]
    base_url = [
        'https://www.parliament.bg'
    ]

    def parse(self, response):

        # print(f"Име: {full_name}")
        all_the_links = response.css("div.MPBlock div.MPBlock_columns div.MPinfo a::attr(href)")
        counter = 0

        for link in all_the_links:
            counter += 1
            single_page_link = self.base_url[0] + link.get()
            yield scrapy.Request(single_page_link, callback=self.parse_link)
        print(counter)

    def parse_link(self, response):
        name = response.xpath("//div/img/@alt").get()
        selection_path = "div.MPinfo ul.frontList li"
        all_data = response.css(selection_path).getall()
        # print(name)
        birthday = ""
        place_of_birth = ""
        profession = ""
        languages = ""
        party = ""
        previous_parliament = ""
        email = ""


        for data in all_data:
            if "Дата на раждане" in data:
                birthday = ''.join(re.findall(r"\d{2}/\d{2}/\d{4}", data))
                place_of_birth = ''.join([i.group() for i in re.finditer(r"(?<=(\d{4}\s))([А-Яа-я]).+(?=<)", data)])
                # print(birthday)
                # print(place_of_birth)
            elif "Професия" in data:
                profession = ', '.join([i.group() for i in re.finditer("(?<=\s|;)([А-Яа-я]+)", data)])
                # print(profession)
            elif "Езици" in data:
                languages = ', '.join([i.group() for i in re.finditer("(?<=\s|;)([А-Яа-я]+)", data)])
                # print(languages)
            elif "Избран(а) с политическа сила" in data:
                party = ''.join([i.group() for i in re.finditer("(?<=\:\s)([А-Яа-я]).+(?=\s\d)", data)])
                # print(party)
            elif "Участие в предишно НС" in data:
                previous_parliament = ', '.join([i.group() for i in re.finditer("(?<=(\>\s))+(\d{2,}\s)(НС)", data)])
                # print(previous_parliament)
            elif "E-mail" in data:
                email = ''.join([i.group() for i in re.finditer("[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@(parliament.bg)", data)][0])
                # print(email)

        data_export = {
            "Име": name,
            "Дата на раждане": birthday,
            "Място на  раждане": place_of_birth,
            "Професия": profession,
            "Езици": languages,
            "Избран(а) с политическа сила": party,
            "Участие в предишно НС": previous_parliament,
            "E-mail": email
                }

        yield data_export












