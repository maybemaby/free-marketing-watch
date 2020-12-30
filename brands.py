import re

fashion = r"""
([\s]?[Uu]niqlo[\s]?)?(Gap)?(H&M)?
(Levis?|Levi's)?(Carhartt)?(Brooks Brothers)?
(Apple)?(Patagonia)?(Everlane)?(J.?Crew)?(Zara)?
(Target|Goodfellow)?(Vans)?(Banana Republic|BR)?
([Oo]ld [Nn]avy)?(Saint Laurent)?([Pp]rada)?
([Cc]anada [Gg]oose)?([Cc]ommon [Pp]rojects)?
([Aa]llen [Ee]dmonds)?([Nn]ike)?([Aa]didas)?
([Aa]bercrombie & [Ff]itch|A&F|[Aa]bercrombie and [Ff]itch)?
(Amazon)?([Cc]alvin [Kk]lein|CK)?([Nn]orth [Ff]ace)?([Rr]alph [Ll]auren)?
([Ll]acoste)?([Tt]ommy [Hh]ilfiger|Tommy)?([Hh]ollister)?([Ll]{2} Bean|L.L. Bean)?
([Ll]ouis [Vv]uitton|LV)?([Tt]om [Ff]ord)?([Gg]ucci)?([Rr]olex)?([Bb]urberry)?
([Aa]merican [Aa]pparel)?(UGG|ugg)?(Express)?(\A[Aa]sket)?([Aa]ll [Ss]aints)?
([Cc]lub [Mm]onaco)?([Ss]cotch & [Ss]oda)?(Next [Ll]evel)?(J.?C.? Penney|JCPenney)?
([Cc]ostco|[Kk]irkland)?([Dd]arn [Tt]ough])?([Nn]orse [Pp]rojects|)?
([Rr]eigning [Cc]hamp)?([Nn]ew [Bb]alance|NB/b)?([Ss]tan [Ss]miths)?
([Yy]eezy)?([Mm]ichael [Kk]ors)?([Rr]ed [Ww]ings?)?([Ll]ululemon)?
([Mm]armot)?([Pp]uma)?([Ee]ddie [Bb]auer)?([Pp]endleton)?(3[Ss]ixteen)?([Bb]onobos)?
([Ee]ngineered [Gg]arments)?(Outlier)?(Armani)?([Gg]ildan)?(American Eagle)?([Cc]olumbia)?
([Cc]onverse)?([Dd]ockers)?([Bb]alenciaga)?(Juicy)?(Champion)?([Ll]and'?s [Ee]nd)?([Vv]iberg)?
([Aa]ldens?)?(Clarks)?([Cc]huck [Tt]aylors)?()
"""
