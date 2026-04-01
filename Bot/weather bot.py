import calendar
import random
from datetime import datetime
from pathlib import Path


WEATHERS = [
	"clear skies",
	"sunny",
	"partly cloudy",
	"mostly cloudy",
	"overcast",
	"light rain",
	"heavy rain",
	"showers",
	"thunderstorms",
	"drizzle",
	"mist",
	"fog",
	"hail",
	"sleet",
	"snow",
	"blizzard",
	"windy",
	"dust storm",
	"heatwave",
	"cold snap",
	"tropical storm",
	"rain then clearing",
	"sun breaks after rain",
	"sunny with passing showers",
]

SKY_DESC = [
	"a soft golden dawn",
	"a pale blue sky",
	"a slate-gray ceiling",
	"high, fast clouds",
	"low, heavy clouds",
	"broken cloud bands",
	"a hazy glow",
	"a sharp, crisp horizon",
]

WIND_DESC = [
	"calm winds",
	"a light breeze",
	"steady winds",
	"gusty winds",
	"strong crosswinds",
	"variable winds",
]

HUMIDITY_DESC = [
	"dry air",
	"comfortable humidity",
	"muggy air",
	"sticky humidity",
]

PRECIP_DESC = [
	"no chance of precipitation",
	"a slight chance of precipitation",
	"a moderate chance of precipitation",
	"a high chance of precipitation",
]

VISIBILITY_DESC = [
	"excellent visibility",
	"good visibility",
	"reduced visibility",
	"poor visibility",
]

EXTRAS = [
	"UV levels will be moderate",
	"UV levels will be high",
	"pollen levels will be elevated",
	"air quality will be fair",
	"air quality will be poor",
	"pressure will be steady",
	"pressure will be falling",
	"pressure will be rising",
	"cloud cover will be patchy",
	"cloud cover will be dense",
]


def random_temperature(min_c=-30, max_c=40):
	return random.randint(min_c, max_c)


def pick_weather():
	return random.choice(WEATHERS)


def random_date():
	current_year = datetime.now().year
	year = random.randint(current_year - 2, current_year + 2)
	month_number = random.randint(1, 12)
	month_name = datetime(year, month_number, 1).strftime("%B")
	last_day = calendar.monthrange(year, month_number)[1]
	day = random.randint(1, last_day)
	return year, month_name, str(day)


def generate_forecast(month=None, day=None):
	if month is None or day is None:
		year, month, day = random_date()
	else:
		year = datetime.now().year

	morning_weather = pick_weather()
	afternoon_weather = pick_weather()
	night_weather = pick_weather()

	a = random_temperature()
	b = random_temperature()
	c = random_temperature()

	lines = [
		f"The weather on {month} {day}, {year} will be {pick_weather()}.",
		f"In the morning, it will be {morning_weather}, and the temperature is expected to reach {a}°.",
		f"In the afternoon, it will be {afternoon_weather}, and the temperature is expected to reach {b}°.",
		f"At night, it will be {night_weather}, and the temperature is expected to reach {c}°.",
		f"Expect {random.choice(SKY_DESC)} with {random.choice(WIND_DESC)}.",
		f"There will be {random.choice(HUMIDITY_DESC)} and {random.choice(PRECIP_DESC)}.",
		f"Overall, {random.choice(VISIBILITY_DESC)} is likely.",
		f"Note: {random.choice(EXTRAS)}.",
	]

	return "\n".join(lines)


if __name__ == "__main__":
	output_path = Path(__file__).resolve().parent / "weather_report.txt"
	with output_path.open("w", encoding="utf-8") as report_file:
		for i in range(10):
			report_file.write(generate_forecast())
			if i < 9:
				report_file.write("\n" + ("-" * 40) + "\n")
