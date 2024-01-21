def bar_chart(this: list, first: str, second: str): # not sure what was it for
    unpacked = [[item[first], int(item[second])] for item in this]
    print(unpacked)


def get_values(smth):
    whole = []
    for dic in smth:
        a = [value for key, value in dic.items()]
        whole.append(a)
    print(whole)


top_8_general = [
  {
    "description_tokens": "sql",
    "count": "19522"
  },
  {
    "description_tokens": "excel",
    "count": "13012"
  },
  {
    "description_tokens": "python",
    "count": "11178"
  },
  {
    "description_tokens": "power_bi",
    "count": "10797"
  },
  {
    "description_tokens": "tableau",
    "count": "10582"
  },
  {
    "description_tokens": "r",
    "count": "7026"
  },
  {
    "description_tokens": "sas",
    "count": "3556"
  },
  {
    "description_tokens": "powerpoint",
    "count": "2983"
  }
]

job_count = [
  {
    "day": "2022-11",
    "count": "2159"
  },
  {
    "day": "2022-12",
    "count": "3329"
  },
  {
    "day": "2023-01",
    "count": "3682"
  },
  {
    "day": "2023-02",
    "count": "2828"
  },
  {
    "day": "2023-03",
    "count": "2727"
  },
  {
    "day": "2023-04",
    "count": "2493"
  },
  {
    "day": "2023-05",
    "count": "2357"
  },
  {
    "day": "2023-06",
    "count": "2362"
  },
  {
    "day": "2023-07",
    "count": "2560"
  },
  {
    "day": "2023-08",
    "count": "3008"
  },
  {
    "day": "2023-09",
    "count": "3085"
  },
  {
    "day": "2023-10",
    "count": "3364"
  },
  {
    "day": "2023-11",
    "count": "2601"
  },
  {
    "day": "2023-12",
    "count": "2100"
  }
]

sites = [
  {
    "via": "via LinkedIn",
    "count": "13059"
  },
  {
    "via": "via Upwork",
    "count": "5852"
  },
  {
    "via": "via BeBee",
    "count": "4456"
  },
  {
    "via": "via Trabajo.org",
    "count": "2986"
  },
  {
    "via": "via ZipRecruiter",
    "count": "2283"
  },
  {
    "via": "via Indeed",
    "count": "1558"
  },
  {
    "via": "via Snagajob",
    "count": "846"
  },
  {
    "via": "via Adzuna",
    "count": "609"
  },
  {
    "via": "via Jobs Trabajo.org",
    "count": "518"
  },
  {
    "via": "via Monster",
    "count": "337"
  }
]

intern_general = [
  {
    "description_tokens": "excel",
    "count": "155"
  },
  {
    "description_tokens": "sql",
    "count": "145"
  },
  {
    "description_tokens": "power_bi",
    "count": "121"
  },
  {
    "description_tokens": "python",
    "count": "107"
  },
  {
    "description_tokens": "r",
    "count": "73"
  },
  {
    "description_tokens": "tableau",
    "count": "71"
  },
  {
    "description_tokens": "powerpoint",
    "count": "54"
  },
  {
    "description_tokens": "word",
    "count": "29"
  },
  {
    "description_tokens": "sas",
    "count": "28"
  },
  {
    "description_tokens": "spark",
    "count": "22"
  }
]

last_month_intern = [
  {
    "description_tokens": "sql",
    "count": "30"
  },
  {
    "description_tokens": "excel",
    "count": "28"
  },
  {
    "description_tokens": "power_bi",
    "count": "23"
  },
  {
    "description_tokens": "python",
    "count": "19"
  },
  {
    "description_tokens": "powerpoint",
    "count": "18"
  },
  {
    "description_tokens": "word",
    "count": "16"
  },
  {
    "description_tokens": "sap",
    "count": "13"
  },
  {
    "description_tokens": "qlik",
    "count": "13"
  },
  {
    "description_tokens": "tableau",
    "count": "9"
  },
  {
    "description_tokens": "sas",
    "count": "7"
  }
]

intern_listing = [
  {
    "day": "2022-11-01",
    "count": "8"
  },
  {
    "day": "2022-12-01",
    "count": "50"
  },
  {
    "day": "2023-01-01",
    "count": "20"
  },
  {
    "day": "2023-02-01",
    "count": "12"
  },
  {
    "day": "2023-03-01",
    "count": "16"
  },
  {
    "day": "2023-04-01",
    "count": "14"
  },
  {
    "day": "2023-05-01",
    "count": "12"
  },
  {
    "day": "2023-06-01",
    "count": "2"
  },
  {
    "day": "2023-07-01",
    "count": "4"
  },
  {
    "day": "2023-08-01",
    "count": "12"
  },
  {
    "day": "2023-09-01",
    "count": "49"
  },
  {
    "day": "2023-10-01",
    "count": "57"
  },
  {
    "day": "2023-11-01",
    "count": "46"
  },
  {
    "day": "2023-12-01",
    "count": "63"
  }
]

interns_schedule = [
  {
    "schedule_type": "Internship",
    "count": "233"
  },
  {
    "schedule_type": "Full-time and Internship",
    "count": "89"
  },
  {
    "schedule_type": "Full-time, Part-time, and Internship",
    "count": "27"
  },
  {
    "schedule_type": "Part-time and Internship",
    "count": "13"
  },
  {
    "schedule_type": "Temp work and Internship",
    "count": "3"
  }
]

line_general = [
  {
    "description_tokensday": "2022-11",
    "excel": "841.0",
    "power_bi": "642.0",
    "powerpoint": "146.0",
    "python": "698.0",
    "r": "520.0",
    "sas": "318.0",
    "sql": "1179.0",
    "tableau": "624.0"
  },
  {
    "description_tokensday": "2022-12",
    "excel": "1169.0",
    "power_bi": "923.0",
    "powerpoint": "203.0",
    "python": "971.0",
    "r": "665.0",
    "sas": "396.0",
    "sql": "1686.0",
    "tableau": "922.0"
  },
  {
    "description_tokensday": "2023-01",
    "excel": "1279.0",
    "power_bi": "922.0",
    "powerpoint": "373.0",
    "python": "929.0",
    "r": "581.0",
    "sas": "296.0",
    "sql": "2013.0",
    "tableau": "1184.0"
  },
  {
    "description_tokensday": "2023-02",
    "excel": "1045.0",
    "power_bi": "764.0",
    "powerpoint": "232.0",
    "python": "786.0",
    "r": "475.0",
    "sas": "241.0",
    "sql": "1434.0",
    "tableau": "725.0"
  },
  {
    "description_tokensday": "2023-03",
    "excel": "987.0",
    "power_bi": "785.0",
    "powerpoint": "189.0",
    "python": "781.0",
    "r": "493.0",
    "sas": "260.0",
    "sql": "1461.0",
    "tableau": "714.0"
  },
  {
    "description_tokensday": "2023-04",
    "excel": "849.0",
    "power_bi": "649.0",
    "powerpoint": "188.0",
    "python": "690.0",
    "r": "437.0",
    "sas": "235.0",
    "sql": "1206.0",
    "tableau": "680.0"
  },
  {
    "description_tokensday": "2023-05",
    "excel": "708.0",
    "power_bi": "686.0",
    "powerpoint": "145.0",
    "python": "639.0",
    "r": "395.0",
    "sas": "192.0",
    "sql": "1154.0",
    "tableau": "651.0"
  },
  {
    "description_tokensday": "2023-06",
    "excel": "763.0",
    "power_bi": "643.0",
    "powerpoint": "182.0",
    "python": "672.0",
    "r": "384.0",
    "sas": "150.0",
    "sql": "1163.0",
    "tableau": "693.0"
  },
  {
    "description_tokensday": "2023-07",
    "excel": "770.0",
    "power_bi": "719.0",
    "powerpoint": "219.0",
    "python": "693.0",
    "r": "447.0",
    "sas": "182.0",
    "sql": "1207.0",
    "tableau": "643.0"
  },
  {
    "description_tokensday": "2023-08",
    "excel": "964.0",
    "power_bi": "959.0",
    "powerpoint": "239.0",
    "python": "986.0",
    "r": "597.0",
    "sas": "286.0",
    "sql": "1657.0",
    "tableau": "861.0"
  },
  {
    "description_tokensday": "2023-09",
    "excel": "967.0",
    "power_bi": "893.0",
    "powerpoint": "249.0",
    "python": "885.0",
    "r": "596.0",
    "sas": "281.0",
    "sql": "1457.0",
    "tableau": "834.0"
  },
  {
    "description_tokensday": "2023-10",
    "excel": "1045.0",
    "power_bi": "843.0",
    "powerpoint": "240.0",
    "python": "944.0",
    "r": "547.0",
    "sas": "261.0",
    "sql": "1493.0",
    "tableau": "798.0"
  },
  {
    "description_tokensday": "2023-11",
    "excel": "849.0",
    "power_bi": "725.0",
    "powerpoint": "195.0",
    "python": "829.0",
    "r": "512.0",
    "sas": "235.0",
    "sql": "1301.0",
    "tableau": "662.0"
  },
  {
    "description_tokensday": "2023-12",
    "excel": "776.0",
    "power_bi": "644.0",
    "powerpoint": "183.0",
    "python": "675.0",
    "r": "377.0",
    "sas": "223.0",
    "sql": "1111.0",
    "tableau": "591.0"
  }
]

intern_count = [
  {
    "day": "2022-11-01",
    "count": "8"
  },
  {
    "day": "2022-12-01",
    "count": "50"
  },
  {
    "day": "2023-01-01",
    "count": "20"
  },
  {
    "day": "2023-02-01",
    "count": "12"
  },
  {
    "day": "2023-03-01",
    "count": "16"
  },
  {
    "day": "2023-04-01",
    "count": "14"
  },
  {
    "day": "2023-05-01",
    "count": "12"
  },
  {
    "day": "2023-06-01",
    "count": "2"
  },
  {
    "day": "2023-07-01",
    "count": "4"
  },
  {
    "day": "2023-08-01",
    "count": "12"
  },
  {
    "day": "2023-09-01",
    "count": "49"
  },
  {
    "day": "2023-10-01",
    "count": "57"
  },
  {
    "day": "2023-11-01",
    "count": "46"
  },
  {
    "day": "2023-12-01",
    "count": "63"
  }
]

last_intern_skill = [
  {
    "day": "2022-12-01",
    "description_tokens": "r",
    "count": "7"
  },
  {
    "day": "2023-01-01",
    "description_tokens": "r",
    "count": "4"
  },
  {
    "day": "2023-03-01",
    "description_tokens": "spark",
    "count": "2"
  },
  {
    "day": "2023-04-01",
    "description_tokens": "r",
    "count": "1"
  },
  {
    "day": "2023-05-01",
    "description_tokens": "r",
    "count": "7"
  },
  {
    "day": "2023-06-01",
    "description_tokens": "r",
    "count": "1"
  },
  {
    "day": "2023-08-01",
    "description_tokens": "r",
    "count": "9"
  },
  {
    "day": "2023-08-01",
    "description_tokens": "spark",
    "count": "8"
  },
  {
    "day": "2023-09-01",
    "description_tokens": "r",
    "count": "7"
  },
  {
    "day": "2023-09-01",
    "description_tokens": "spark",
    "count": "3"
  },
  {
    "day": "2023-10-01",
    "description_tokens": "r",
    "count": "18"
  },
  {
    "day": "2023-10-01",
    "description_tokens": "sap",
    "count": "2"
  },
  {
    "day": "2023-10-01",
    "description_tokens": "spark",
    "count": "2"
  },
  {
    "day": "2023-11-01",
    "description_tokens": "qlik",
    "count": "1"
  },
  {
    "day": "2023-11-01",
    "description_tokens": "r",
    "count": "12"
  },
  {
    "day": "2023-11-01",
    "description_tokens": "sap",
    "count": "1"
  },
  {
    "day": "2023-11-01",
    "description_tokens": "spark",
    "count": "1"
  },
  {
    "day": "2023-12-01",
    "description_tokens": "qlik",
    "count": "13"
  },
  {
    "day": "2023-12-01",
    "description_tokens": "r",
    "count": "7"
  },
  {
    "day": "2023-12-01",
    "description_tokens": "sap",
    "count": "13"
  },
  {
    "day": "2023-12-01",
    "description_tokens": "spark",
    "count": "6"
  }
]

# get_values(line_general)
# bar_chart(intern_count, 'day', 'count')

data_dict = {}
for entry in last_intern_skill:
    date = entry["day"]
    token = entry["description_tokens"]
    count = entry["count"]

    if date not in data_dict:
        data_dict[date] = {"qlik": "", "sap": "", "spark": "", "r": ""}
    data_dict[date][token] = count

# Step 2: Create a sorted list of unique dates
unique_dates = sorted(data_dict.keys())

# Step 3: Create the final list of lists
final_list = []
for date in unique_dates:
    entry = [date]
    entry.extend([data_dict[date][token] for token in ["qlik", "sap", "spark", "r"]])
    final_list.append(entry)

# Print the final list of lists
for item in final_list:
    print(item)