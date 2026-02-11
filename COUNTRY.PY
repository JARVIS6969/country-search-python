class Country:
    """Represents a country with name, capital, population, and area."""
    print("-"*90)
    x=input("hello sir ! what's your name :")
    print("-"*90)

    print( x," sir you're logged into Renaisance support")
    print("Welcome to Renaissance support")
    print("-"*90)

    def __init__(self, country_name, capital, population, area):
        """Initializes the Country object with the given attributes.""" 
        self.country_name = country_name
        self.capital = capital
        self.population = population
        self.area = area

    def show(self):
        """Displays all details of the country."""
        print("-" * 100)
        print("Country name :→", self.country_name, "\n"
              "Capital :→", self.capital, "\n"
              "Population :→", self.population, "\n"
              "Area :→", self.area, "\n")
        print("-" * 100)

# Create a list of Country objects
countries = [
    Country("Afghanistan", "Kabul", "42,239,854", "652,230 km²"),
Country("Albania", "Tirana", "2,832,797", "28,748 km²"),
Country("Algeria", "Algiers", "46,078,735", "2,381,741 km²"),
Country("Andorra", "Andorra la Vella", "81,214", "468 km²"),
Country("Angola", "Luanda", "37,027,816", "1,246,700 km²"),
Country("Antigua and Barbuda", "Saint John’s", "94,298", "442 km²"),
Country("Argentina", "Buenos Aires", "46,233,314", "2,780,400 km²"),
Country("Armenia", "Yerevan", "2,780,578", "29,743 km²"),
Country("Australia", "Canberra", "27,482,494", "7,692,024 km²"),
Country("Austria", "Vienna", "9,159,934", "83,871 km²"),
Country("Azerbaijan", "Baku", "10,398,764", "86,600 km²"),
Country("Bahamas", "Nassau", "412,628", "13,880 km²"),
Country("Bahrain", "Manama", "1,558,729", "778 km²"),
Country("Bangladesh", "Dhaka", "174,701,211", "147,570 km²"),
Country("Barbados", "Bridgetown", "281,995", "430 km²"),
Country("Belarus", "Minsk", "9,127,650", "207,600 km²"),
Country("Belgium", "Brussels", "11,769,700", "30,528 km²"),
Country("Belize", "Belmopan", "420,476", "22,966 km²"),
Country("Benin", "Porto-Novo", "14,797,514", "114,763 km²"),
Country("Bhutan", "Thimphu", "787,424", "38,394 km²"),
Country("Bolivia", "Sucre", "12,582,921", "1,098,581 km²"),
Country("Bosnia and Herzegovina", "Sarajevo", "3,191,354", "51,197 km²"),
Country("Botswana", "Gaborone", "2,830,335", "581,730 km²"),
Country("Brazil", "Brasília", "203,062,512", "8,515,767 km²"),
Country("Brunei", "Bandar Seri Begawan", "457,473", "5,765 km²"),
Country("Bulgaria", "Sofia", "6,384,798", "110,994 km²"),
Country("Burkina Faso", "Ouagadougou", "24,814,471", "274,222 km²"),
Country("Burundi", "Gitega", "13,483,657", "27,834 km²"),
Country("Cabo Verde", "Praia", "593,149", "4,033 km²"),
Country("Cambodia", "Phnom Penh", "17,072,115", "181,035 km²"),
Country("Cameroon", "Yaoundé", "29,858,126", "475,442 km²"),
Country("Canada", "Ottawa", "40,528,396", "9,984,670 km²"),
Country("Central African Republic", "Bangui", "5,742,315", "622,984 km²"),
Country("Chad", "N'Djamena", "19,680,925", "1,284,000 km²"),
Country("Chile", "Santiago", "19,878,341", "756,102 km²"),
Country("China", "Beijing", "1,413,142,852", "9,596,961 km²"),
Country("Colombia", "Bogotá", "52,312,220", "1,141,748 km²"),
Country("Comoros", "Moroni", "907,406", "1,862 km²"),
Country("Congo, Republic of the", "Brazzaville", "6,457,516", "342,000 km²"),
Country("Congo, Democratic Republic of the", "Kinshasa", "105,880,473", "2,344,858 km²"),
Country("Costa Rica", "San José", "5,290,192", "51,100 km²"),
Country("Croatia", "Zagreb", "3,855,641", "56,594 km²"),
Country("Cuba", "Havana", "11,079,266", "109,884 km²"),
Country("Cyprus", "Nicosia", "1,260,138", "9,251 km²"),
Country("Czech Republic", "Prague", "10,913,052", "78,865 km²"),
Country("Denmark", "Copenhagen", "5,952,484", "42,933 km²"),
Country("Djibouti", "Djibouti", "1,136,455", "23,200 km²"),
Country("Dominica", "Roseau", "72,414", "751 km²"),
Country("Dominican Republic", "Santo Domingo", "11,440,817", "48,671 km²"),
Country("Ecuador", "Quito", "18,226,736", "276,841 km²"),
Country("Egypt", "Cairo", "113,680,327", "1,010,408 km²"),
Country("El Salvador", "San Salvador", "6,486,201", "21,041 km²"),
Country("Equatorial Guinea", "Malabo", "1,740,705", "28,051 km²"),
Country("Eritrea", "Asmara", "3,748,901", "117,600 km²"),
Country("Estonia", "Tallinn", "1,354,661", "45,227 km²"),
Country("Eswatini", "Mbabane", "1,233,100", "17,364 km²"),
Country("Ethiopia", "Addis Ababa", "129,719,719", "1,104,300 km²"),
Country("Fiji", "Suva", "942,958", "18,274 km²"),
Country("Finland", "Helsinki", "5,565,275", "338,455 km²"),
Country("France", "Paris", "65,633,864", "551,695 km²"),
Country("Gabon", "Libreville", "2,473,724", "267,667 km²"),
Country("Gambia", "Banjul", "2,773,168", "11,295 km²"),
Country("Georgia", "Tbilisi", "3,728,282", "69,700 km²"),
Country("Germany", "Berlin", "83,823,335", "357,022 km²"),
Country("Ghana", "Accra", "34,825,759", "238,535 km²"),
Country("Greece", "Athens", "10,290,192", "131,957 km²"),
Country("Grenada", "St. George's", "126,183", "344 km²"),
Country("Guatemala", "Guatemala City", "18,248,901", "108,889 km²"),
Country("Guinea", "Conakry", "14,321,358", "245,857 km²"),
Country("Guinea-Bissau", "Bissau", "2,182,159", "36,125 km²"),
Country("Guyana", "Georgetown", "804,567", "214,969 km²"),
Country("Haiti", "Port-au-Prince", "11,859,264", "27,750 km²"),
Country("Honduras", "Tegucigalpa", "10,511,871", "112,492 km²"),
Country("Hungary", "Budapest", "9,570,753", "93,028 km²"),
Country("Iceland", "Reykjavík", "382,003", "103,000 km²"),
Country("India", "New Delhi", "1,428,627,663", "3,287,263 km²"),
Country("Indonesia", "Jakarta", "279,798,049", "1,904,569 km²"),
Country("Iran", "Tehran", "89,172,822", "1,648,195 km²"),
Country("Iraq", "Baghdad", "46,146,283", "438,317 km²"),
Country("Ireland", "Dublin", "5,119,140", "70,273 km²"),
Country("Israel", "Jerusalem", "9,833,634", "22,145 km²"),
Country("Italy", "Rome", "58,752,319", "301,340 km²"),
Country("Jamaica", "Kingston", "2,827,432", "10,991 km²"),
Country("Japan", "Tokyo", "123,753,041", "377,975 km²"),
Country("Jordan", "Amman", "11,372,587", "89,342 km²"),
Country("Kazakhstan", "Astana", "19,574,205", "2,724,900 km²"),
Country("Kenya", "Nairobi", "55,100,586", "580,367 km²"),
Country("Kiribati", "Tarawa", "134,183", "811 km²"),
Country("Kuwait", "Kuwait City", "4,438,610", "17,818 km²"),
Country("Kyrgyzstan", "Bishkek", "7,132,763", "199,951 km²"),
Country("Laos", "Vientiane", "7,754,755", "236,800 km²"),
Country("Latvia", "Riga", "1,830,152", "64,589 km²"),
Country("Lebanon", "Beirut", "5,324,357", "10,452 km²"),
Country("Lesotho", "Maseru", "2,332,345", "30,355 km²"),
Country("Liberia", "Monrovia", "5,520,209", "111,369 km²"),
Country("Libya", "Tripoli", "7,214,236", "1,759,540 km²"),
Country("Liechtenstein", "Vaduz", "39,947", "160 km²"),
Country("Lithuania", "Vilnius", "2,720,736", "65,300 km²"),
Country("Luxembourg", "Luxembourg City", "660,809", "2,586 km²"),
Country("Madagascar", "Antananarivo", "30,325,732", "587,041 km²"),
Country("Malawi", "Lilongwe", "21,854,083", "118,484 km²"),
Country("Malaysia", "Kuala Lumpur", "34,308,525", "330,803 km²"),
Country("Maldives", "Malé", "521,457", "300 km²"),
Country("Mali", "Bamako", "23,703,380", "1,240,192 km²"),
Country("Malta", "Valletta", "542,978", "316 km²"),
Country("Marshall Islands", "Majuro", "42,048", "181 km²"),
Country("Mauritania", "Nouakchott", "4,947,901", "1,030,700 km²"),
Country("Mauritius", "Port Louis", "1,309,605", "2,040 km²"),
Country("Mexico", "Mexico City", "130,262,216", "1,964,375 km²"),
Country("Micronesia", "Palikir", "98,346", "702 km²"),
Country("Moldova", "Chișinău", "3,202,658", "33,846 km²"),
Country("Monaco", "Monaco", "39,494", "2 km²"),
Country("Mongolia", "Ulaanbaatar", "3,511,481", "1,566,000 km²"),
Country("Montenegro", "Podgorica", "616,830", "13,812 km²"),
Country("Morocco", "Rabat", "38,009,677", "446,300 km²"),
Country("Mozambique", "Maputo", "34,703,164", "801,590 km²"),
Country("Namibia", "Windhoek", "2,698,767", "825,615 km²"),
Country("Nauru", "Yaren", "12,202", "21 km²"),
Country("Nepal", "Kathmandu", "30,547,580", "147,516 km²"),
Country("Netherlands", "Amsterdam", "17,815,508", "41,543 km²"),
Country("New Zealand", "Wellington", "5,322,780", "268,021 km²"),
Country("Nicaragua", "Managua", "7,256,276", "130,373 km²"),
Country("Niger", "Niamey", "28,664,417", "1,267,000 km²"),
Country("Nigeria", "Abuja", "229,152,217", "923,768 km²"),
Country("North Korea", "Pyongyang", "26,015,641", "120,540 km²"),
Country("North Macedonia", "Skopje", "2,065,823", "25,713 km²"),
Country("Norway", "Oslo", "5,581,312", "385,207 km²"),
Country("Oman", "Muscat", "4,644,384", "309,500 km²"),
Country("Pakistan", "Islamabad", "245,209,815", "881,913 km²"),
Country("Palau", "Ngerulmud", "18,058", "459 km²"),
Country("Panama", "Panama City", "4,468,087", "75,417 km²"),
Country("Papua New Guinea", "Port Moresby", "10,329,931", "462,840 km²"),
Country("Paraguay", "Asunción", "7,305,843", "406,752 km²"),
Country("Peru", "Lima", "34,352,720", "1,285,216 km²"),
Country("Philippines", "Manila", "119,106,224", "300,000 km²"),
Country("Poland", "Warsaw", "40,115,876", "312,696 km²"),
Country("Portugal", "Lisbon", "10,491,500", "92,212 km²"),
Country("Qatar", "Doha", "2,724,341", "11,586 km²"),
Country("Romania", "Bucharest", "18,706,625", "238,397 km²"),
Country("Russia", "Moscow", "145,725,477", "17,098,242 km²"),
Country("Rwanda", "Kigali", "14,374,252", "26,338 km²"),
Country("Saint Kitts and Nevis", "Basseterre", "48,376", "261 km²"),
Country("Saint Lucia", "Castries", "180,251", "616 km²"),
Country("Saint Vincent and the Grenadines", "Kingstown", "111,551", "389 km²"),
Country("Samoa", "Apia", "225,681", "2,831 km²"),
Country("San Marino", "San Marino", "34,882", "61 km²"),
Country("Sao Tome and Principe", "São Tomé", "235,402", "964 km²"),
Country("Saudi Arabia", "Riyadh", "36,947,025", "2,149,690 km²"),
Country("Senegal", "Dakar", "18,384,670", "196,722 km²"),
Country("Serbia", "Belgrade", "6,647,003", "88,361 km²"),
Country("Seychelles", "Victoria", "101,316", "452 km²"),
Country("Sierra Leone", "Freetown", "9,159,063", "71,740 km²"),
Country("Singapore", "Singapore", "6,014,700", "728 km²"),
Country("Slovakia", "Bratislava", "5,585,931", "49,035 km²"),
Country("Slovenia", "Ljubljana", "2,120,847", "20,271 km²"),
Country("Solomon Islands", "Honiara", "743,208", "28,896 km²"),
Country("Somalia", "Mogadishu", "18,143,378", "637,657 km²"),
Country("South Africa", "Pretoria", "62,343,598", "1,221,037 km²"),
Country("South Korea", "Seoul", "52,617,325", "100,363 km²"),
Country("South Sudan", "Juba", "11,633,200", "619,745 km²"),
Country("Spain", "Madrid", "48,345,650", "505,990 km²"),
Country("Sri Lanka", "Sri Jayawardenepura Kotte", "22,181,260", "65,610 km²"),
Country("Sudan", "Khartoum", "48,460,452", "1,886,068 km²"),
Country("Suriname", "Paramaribo", "632,995", "163,820 km²"),
Country("Sweden", "Stockholm", "10,602,674", "450,295 km²"),
Country("Switzerland", "Bern", "8,928,736", "41,290 km²"),
Country("Syria", "Damascus", "22,157,104", "185,180 km²"),
Country("Taiwan", "Taipei", "23,907,000", "36,193 km²"),
Country("Tajikistan", "Dushanbe", "10,374,711", "143,100 km²"),
Country("Tanzania", "Dodoma", "67,438,106", "945,087 km²"),
Country("Thailand", "Bangkok", "71,924,008", "513,120 km²"),
Country("Timor-Leste", "Dili", "1,395,309", "14,874 km²"),
Country("Togo", "Lomé", "9,053,799", "56,785 km²"),
Country("Tonga", "Nukuʻalofa", "107,773", "747 km²"),
Country("Trinidad and Tobago", "Port of Spain", "1,531,044", "5,131 km²"),
Country("Tunisia", "Tunis", "12,262,074", "163,610 km²"),
Country("Turkey", "Ankara", "86,466,514", "783,356 km²"),
Country("Turkmenistan", "Ashgabat", "7,240,193", "488,100 km²"),
Country("Tuvalu", "Funafuti", "11,703", "26 km²"),
Country("Uganda", "Kampala", "49,598,100", "241,038 km²"),
Country("Ukraine", "Kyiv", "42,162,960", "603,500 km²"),
Country("United Arab Emirates", "Abu Dhabi", "10,181,427", "83,600 km²"),
Country("United Kingdom", "London", "68,558,263", "243,610 km²"),
Country("United States", "Washington D.C.", "340,000,000", "9,833,517 km²"),
Country("Vanuatu", "Port Vila", "334,981", "12,189 km²"),
Country("Vatican City", "Vatican City", "825", "0.49 km²"),
Country("Venezuela", "Caracas", "32,882,535", "916,445 km²"),
Country("Vietnam", "Hanoi", "100,664,808", "331,212 km²"),
Country("Xenophobia-free Territory", "N/A", "0", "0 km²"),

Country("Yemen", "Sana'a", "33,212,438", "527,968 km²"),
Country("Zambia", "Lusaka", "20,792,369", "752,612 km²"),
Country("Zimbabwe", "Harare", "16,425,896", "390,757 km²"),


]

#main logic 

def search_simple(value, country_list):
    value = value.lower()
    found = False

    for c in country_list:
        if c.country_name.lower().startswith(value):
            c.show()
            found = True   # at least one match found

    if not found:
        print("No match found.")


    
# --- Interactive Usage (Taking Input) ---

# Prompt the user for input

user_input = input("Enter a country letter or country name to search (e.g., India, Japan, a,b, A, B, I, J): ")

# Call the search function with the user's input
search_simple(user_input, countries)

