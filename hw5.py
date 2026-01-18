from dateutil import parser

date_string = parser.parse("2020-07-30")
parsed_date = parser.parse("2020-07-30")
print(f"Распознанная дата: {parsed_date}")
print(f"Только год: {parsed_date.year}")