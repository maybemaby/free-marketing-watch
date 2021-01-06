import re

fashion = r"""
(?P<uniqlo>\s?[Uu]niqlo\s?)?
(?P<Gap>\s?Gap\s?|\s?GAP\s?)?
(?P<HM>\s?[Hh]&[Mm]\s?)?
(?P<Levis>\s?[Ll]evis?\s?|\s?[Ll]evi's\s?)?
(?P<Carhartt>\s?[Cc]arhartt\s?)?
(?P<BrooksBrothers>\s?[Bb]rooks\s?[Bb]rothers\s?|\s?[Bb]rooks\s?[Bb]ros\s?)?
(?P<Apple>\s?Apple\s?)?
(?P<Patagonia>\s?[Pp]atagonia\s?)?
(?P<Everlane>\s?[Ee]verlane\s?)?
(?P<JCrew>\s?J.?Crew\s?)?
(?P<Zara>\s?Zara\s?)?
(?P<Target>\s?Target\s?|\s?Goodfellows?\s?)?
(?P<Vans>\s?Vans\s?)?
(?P<BananaRepublic>\s?Banana\s?Republic\s?|\s?BR\s?)?
(?P<OldNavy>\s?[Oo]ld\s?[Nn]avy\s?)?
(?P<SaintLaurent>\s?Saint\s?Laurent\s?)?
(?P<Prada>\s?[Pp]rada\s?)?
(?P<CanadaGoose>\s?[Cc]anada\s?[Gg]oose\s?)?
(?P<CommonProjects>\s?[Cc]ommon\s?[Pp]rojects\s?)?
(?P<AllendEdmonds>\s?[Aa]llen\s?[Ee]dmonds\s?)?
(?P<Nike>\s?[Nn]ike\s?)?
(?P<Adidas>\s?[Aa]didas\s?|\s?[Ss]tan\s?[Ss]miths\s?)?
(?P<Abercrombie>\s?[Aa]bercrombie\s?&\s?[Ff]itch\s?|\s?A&F\s?|\s?[Aa]bercrombie\s?and\s?[Ff]itch\s?|\s?[Aa]bercrombie\s?)?
(?P<Amazon>\s?Amazon\s?)?
(?P<CalvinKlein>\s?[Cc]alvin\s?[Kk]lein\s?|\s?CK\s?)?
(?P<NorthFace>\s?[Nn]orth\s?[Ff]ace\s?)?
(?P<RalphLauren>\s?[Rr]alph\s?[Ll]auren\s?)?
(?P<Lacoste>\s?[Ll]acoste\s?)?
(?P<TommyHilfiger>\s?[Tt]ommy\s?[Hh]ilfiger\s?|\s?Tommy\s?)?
(?P<Hollister>\s?[Hh]ollister\s?)?
(?P<LLBean>\s?[Ll]{2}\s?Bean\s?|\s?L.L.\s?Bean\s?)?
(?P<LouisVuitton>\s?[Ll]ouis\s?[Vv]uitton\s?|\s?LV\s?)?
(?P<TomFord>\s?[Tt]om\s?[Ff]ord\s?)?
(?P<Gucci>\s?[Gg]ucci\s?)?
(?P<Rolex>\s?[Rr]olex\s?)?
(?P<Burberry>\s?[Bb]urberry\s?)?
(?P<AmericanApparel>\s?[Aa]merican\s?[Aa]pparel\s?)?
(?P<Uggs>\s?\bUGGs?|\bUggs?\s?)?
(?P<Express>\s?Express\s?)?
(?P<Asket>\s?\b[Aa]sket\s?)?
(?P<Birkenstocks>\s?[Bb]irkenstocks?\s?)?
(?P<ClubMonaco>\s?[Cc]lub\s?[Mm]onaco\s?)?
(?P<ScotchandSoda>\s?[Ss]cotch\s?&\s?[Ss]oda\s?)?
(?P<NextLevel>\s?Next\s?[Ll]evel\s?)?
(?P<JCPenney>\s?J.?C.?\s?Penney\s?|\s?JCPenney\s?)?
(?P<Costco>\s?[Cc]ostco\s?|\s?[Kk]irkland\s?)?
(?P<DarnTough>\s?[Dd]arn\s?[Tt]ough\s?)?
(?P<NorseProjects>\s?[Nn]orse\s?[Pp]rojects\s?)?
(?P<ReigningChamp>\s?[Rr]eigning\s?[Cc]hamp\s?)?
(?P<NewBalance>\s?[Nn]ew\s?[Bb]alance\s?|\s?NB/b)?
(?P<Frye>\s?[Ff]rye\s?)?
(?P<Yeezy>\s?[Yy]eezy\s?)?
(?P<MichaelKors>\s?[Mm]ichael\s?[Kk]ors\s?)?
(?P<RedWings>\s?[Rr]ed\s?[Ww]ings?\s?)?
(?P<Lululemon>\s?[Ll]ululemon\s?|\s?[Ll]ulus?\s?)?
(?P<Marmot>\s?[Mm]armot\s?)?
(?P<Puma>\s?[Pp]uma\s?)?
(?P<EddieBauer>\s?[Ee]ddie\s?[Bb]auer\s?)?
(?P<Pendleton>\s?[Pp]endleton\s?)?
(?P<ThreeSixteen>\s?3[Ss]ixteen\s?)?
(?P<Bonobos>\s?[Bb]onobos\s?)?
(?P<EngineeredGarments>\s?[Ee]ngineered\s?[Gg]arments\s?)?
(?P<Outlier>\s?Outlier\s?)?
(?P<Armani>\s?Armani\s?)?
(?P<Gildan>\s?[Gg]ildan\s?)?
(?P<AmericanEagle>\s?American\s?Eagle\s?)?
(?P<Columbia>\s?[Cc]olumbia\s?)?
(?P<Converse>\s?[Cc]onverse\s?)?
(?P<Dockers>\s?[Dd]ockers\s?)?
(?P<Balenciaga>\s?[Bb]alenciaga\s?)?
(?P<Juicy>\s?Juicy\s?)?
(?P<Champion>\s?Champion\s?)?
(?P<LandsEnd>\s?[Ll]and'?s\s?[Ee]nd\s?)?
(?P<Viberg>\s?[Vv]iberg\s?)?
(?P<Aldens>\s?[Aa]ldens?\s?)?
(?P<Clarks>\s?Clarks\s?)?
(?P<ChuckTaylors>\s?[Cc]huck\s?[Tt]aylors\s?)?
(?P<VictoriaSecret>\s?[Vv]ictoria'?s?\s?[Ss]ecret\s?)?
(?P<Dickies>\s?[Dd]ickie'?s\s?)?
(?P<SteveMadden>\s?[Ss]teve\s?[Mm]adden\s?)?
(?P<Thrifted>\s?[Tt]hrifted\s?)?
(?P<Margiela>\s?[Mm]argiela\s?)?
(?P<Visvim>\s?[Vv]isvim\s?)?
(?P<Loft>\s?[Ll]oft\s?|\s?LOFT\s?)?
(?P<AnnTaylor>\s?[Aa]nn\s?[Tt]aylor\s?)?
(?P<PullsandBears>\s?[Pp]ull\s?&\s?[Bb]ear\s?)?
(?P<Madewell>\s?[Mm]adewell\s?)?
(?P<KennethCole>\s?[Kk]enneth\s?[Cc]ole\s?)?
(?P<Mango>\s?Mango\s?)?
(?P<Modcloth>\s?[Mm]odcloth\s?)?
(?P<DocMartens>\s?[Dd]oc\s?Marten'?s?\s?|\s?Docs\s?)?
(?P<KateSpade>\s?[Kk]ate\s?[Ss]pade\s?)?
(?P<Stradivarius>\s?[Ss]tradivarius\s?)?
(?P<MarcJacobs>\s?[Mm]arc\s?[Jj]acobs\s?)?
(?P<Allsaints>\s?[Aa]llsaints\s?|\s?[Aa]ll\s?[Ss]aints\s?)?
(?P<Primark>\s?[Pp]rimark\s?)?
(?P<EileenFisher>\s?[Ei]leen\s?[Ff]isher\s?)?
(?P<Aaritzia>\s?[Aa]ritzia\s?)?
(?P<Topshop>\s?[Tt]opshop\s?)?
(?P<Naturalizer>\s?[Nn]aturalizer\s?)?
(?P<SpierandMackay>\s?Spier\s?|\s?Spier\s?&\s?[Mm]ackay\s?)?
(?P<RogueTerritory>\s?[Rr]ogue\s?[Tt]erritory\s?)?
(?P<Muji>\s?[Mm]uji\s?)?
(?P<Arcteryx>\s?[Aa]rcteryx\s?)?
(?P<Paraboots>\s?[Pp]araboot\s?)?
(?P<Blundstone>\s?[Bb]lundstones?\s?)?
(?P<StanRays>\s?[Ss]tan\s?[Rr]ay\s?)?
(?P<Deveaux>\s?[Dd]eveaux\s?)?
(?P<Epaulet>\s?Epaulet\s?)?
(?P<BergsandBergs>\s?Berg\s?&\s?Berg\s?)?
(?P<ONI>\s?ONI\s?)?
(?P<GrantStone>\s?[Gg]rant\s?[Ss]tone\s?)?
(?P<EvanKinori>\s?[Ee]van\s?[Kk]inori\s?)?
(?P<NakedandFamous>\s?[Nn]aked\s?and\s?[Ff]amous?)?
(?P<Supreme>\s?Supreme\s?)?
(?P<Drakes>\s?Drake's\s?)?
"""
fashionlist = {
    "uniqlo": "",
    "Gap": "",
    "H&M": ["H&M", "H and M", "HnM"],
    "Levis": ["Levis", "Levi's"],
    "Carhartt": "",
    "Brooks Brothers": ["Brooks Brothers", "Brooks Bros"],
    "Apple": "",
    "Patagonia": "",
    "Everlane": "",
    "J.Crew": ["J.Crew", "J Crew", "JCrew"],
    "Zara": "",
    "Target": ["Target", "Goodfellow & co", "goodfellow"],
    "Banana Republic": "",
    "Old Navy": "",
    "Saint Laurent": "",
    "Prada": "",
    "Canada Goose": "",
    "Common Projects": "",
    "Allend Edmonds": "",
    "Nike": "",
    "Adidas": "",
    "Abercrombie": ["Abercrombie", "Abercrombie and Fitch", "Abercrombie & Fitch"],
    "Amazon": "",
    "Calvin Klein": "",
    "North Face": "",
    "Ralph Lauren": "",
    "Lacoste": "",
    "Tommy Hilfiger": "",
    "Hollister": "",
    "LLBean": ["L.L. Bean", "LL Bean", "L L Bean"],
    "Louis Vuitton": "",
    "Tom Ford": "",
    "Gucci": "",
    "Rolex": "",
    "Burberry": "",
    "American Apparel": "",
    "Uggs": "",
    "Express": "",
    "Asket": "",
    "Birkenstocks": "",
    "Club Monaco": "",
    "ScotchandSoda": ["Scotch and Soda", "Scotch & Soda"],
    "Next Level": "",
    "JCPenney": ["JCPenney", "JC Penney", "J.C Penney"],
    "Costco": ["Costco", "kirkland"],
    "Darn Tough": "",
    "Norse Projects": "",
    "Reigning Champ": "",
    "New Balance": "",
    "Frye": "",
    "Yeezy": "",
    "Michael Kors": "",
    "Red Wings": "",
    "Lululemon": "",
    "Marmot": "",
    "Puma": "",
    "Eddie Bauer": "",
    "Pendleton": "",
    "ThreeSixteen": ["threesixteen", "3sixteen"],
    "Bonobos": "",
    "Engineered Garments": "",
    "Outlier": "",
    "Armani": "",
    "Gildan": "",
    "American Eagle": "",
    "Columbia": "",
    "Converse": "",
    "Dockers": "",
    "Balenciaga": "",
    "Juicy": "",
    "Champion": "",
    "Lands End": ["Land's End", "Lands End"],
    "Viberg": "",
    "Aldens": "",
    "Clarks": "",
    "Chuck Taylors": "",
    "Victoria Secret": "",
    "Dickies": "",
    "Steve Madden": "",
    "Thrifted": "",
    "Margiela": "",
    "Visvim": "",
    "Loft": "",
    "Ann Taylor": "",
    "Pulls and Bears": ["Pulls&Bears", "Pulls and Bears", "Pulls & Bears"],
    "Madewell": "",
    "Kenneth Cole": "",
    "Mango": "",
    "Modcloth": "",
    "Doc Martens": "",
    "Kate Spade": "",
    "Stradivarius": "",
    "Marc Jacobs": "",
    "Allsaints": "",
    "Primark": "",
    "Eileen Fisher": "",
    "Aaritzia": "",
    "Topshop": "",
    "Naturalizer": "",
    "Spier and Mackay": ["Spier and Mackay", "Spier & Mackay", "Spier&Mackay"],
    "Rogue Territory": "",
    "Muji": "",
    "Arcteryx": "",
    "Paraboots": "",
    "Blundstone": "",
    "StanRays": ["Stan Ray", "Stan Rays", "Stanrays", "Stanray"],
    "Deveaux": "",
    "Epaulet": "",
    "BergsandBergs": [
        "BergsandBergs",
        "Bergs&Bergs",
        "Bergs & Bergs",
        "Bergs and Bergs",
    ],
    "ONI": "",
    "Grant Stone": "",
    "Evan Kinori": "",
    "Naked and Famous": ["Naked and Famous", "Naked & Famous"],
    "Supreme": "",
    "Drakes": ["Drake's", "Drakes"],
}