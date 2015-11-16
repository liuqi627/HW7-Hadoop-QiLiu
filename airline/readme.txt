1.Briefly describing your programs:
    1.percentage departures later than 5 minutes from every airport

    	Map output: list of this:(Airport   “late”/“not_late”)
    	Reduce input: sorted list of (Airport   “late”/“not_late”)
    	Reduce output: list of (Airport   percentage)

    2.total hours of airtime per carrier have

    	Map output: list of this:(carrier   airtime_hour)
    	Reduce input: sorted list of (carrier   airtime_hour)
    	Reduce output: list of (carrier   total_airtime_hour)

2.some sample output (do not include the entire output files):
    1.percentage departures later than 5 minutes from every airport:

Adak Island	39.42%
Amarillo	31.12%
Aspen	31.30%
Atlantic City	18.74%
Austin	30.33%
Bangor	17.84%
Bend/Redmond	18.10%
Bismarck/Mandan	22.54%
Branson	38.21%
Burlington	24.49%
Carlsbad	20.10%
Charleston/Dunbar	28.56%
Chattanooga	23.76%
Cincinnati	23.82%
Cleveland	26.38%
College Station/Bryan	20.60%
Colorado Springs	23.96%
Columbia	25.35%
Columbus	28.47%
Detroit	24.87%
Dickinson	19.36%
Dubuque	24.00%
Elko	9.49%
Erie	27.52%
Eugene	21.88%
Flint	22.82%
Fort Smith	19.56%
Gainesville	20.81%
Garden City	23.87%
Gillette	18.18%
Grand Junction	15.52%
Grand Rapids	27.43%
Gustavus	45.45%
Hancock/Houghton	26.37%
Hattiesburg/Laurel	31.91%

    2.total hours of airtime per carrier have:

AA	1263972.0
AS	414587.0
F9	165811.0
B6	581891.0
DL	1555996.0
UA	1382888.0
US	832791.0
VX	180987.0
WN	1951028.0