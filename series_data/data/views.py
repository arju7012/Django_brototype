from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




    
def series_list_view(request):
    """
    Renders the index.html template, passing the series_data dictionary.
    """
    series_data = {
        "series": [
        {
            "name": "Game of Thrones",
            "year": "2011-2019",
            "summary": "Nine noble families fight for control over the mythical lands of Westeros, while an ancient enemy returns after being dormant for thousands of years.",
            "rating": 8.9
        },
        {
            "name": "Breaking Bad",
            "year": "2008-2013",
            "summary": "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine to secure his family's financial future.",
            "rating": 9.5
        },
        {
            "name": "The Office (US)",
            "year": "2005-2013",
            "summary": "A mockumentary on the everyday lives of a group of office employees in the Scranton, Pennsylvania, branch of the fictional Dunder Mifflin Paper Company.",
            "rating": 9.0
        },
        {
            "name": "Stranger Things",
            "year": "2016-Present",
            "summary": "When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces, and one strange little girl.",
            "rating": 8.7
        },
        {
            "name": "The Crown",
            "year": "2016-2023",
            "summary": "Follows the political rivalries and romance of Queen Elizabeth II's reign and the events that shaped the second half of the 20th century.",
            "rating": 8.6
        },
        {
            "name": "Friends",
            "year": "1994-2004",
            "summary": "Follows the lives of six young adults living in Manhattan as they navigate relationships, careers, and the ups and downs of life in their 20s and 30s.",
            "rating": 8.9
        },
        {
            "name": "Chernobyl",
            "year": 2019,
            "summary": "Dramatizes the true story of the 1986 nuclear disaster in the Soviet Union and the sacrifices made to mitigate the catastrophe.",
            "rating": 9.3
        },
        {
            "name": "Black Mirror",
            "year": "2011-Present",
            "summary": "An anthology series exploring a twisted, high-tech near-future where humanity's greatest innovations and darkest instincts collide.",
            "rating": 8.8
        },
        {
            "name": "The Mandalorian",
            "year": "2019-Present",
            "summary": "The lone gunfighter travels to the outer reaches of the galaxy, far from the authority of the New Republic.",
            "rating": 8.7
        },
        {
            "name": "Succession",
            "year": "2018-2023",
            "summary": "The Roy family, owners of a global media and entertainment conglomerate, fight for control of the company amid uncertainty about their aging patriarch's health.",
            "rating": 8.8
        },
        {
            "name": "Attack on Titan",
            "year": "2013-2023",
            "summary": "Humanity lives within cities surrounded by enormous walls to protect themselves from gigantic humanoid creatures referred to as Titans.",
            "rating": 9.1
        },
        {
            "name": "Queen's Gambit",
            "year": 2020,
            "summary": "Orphaned chess prodigy Beth Harmon struggles with addiction while aspiring to become the world's greatest chess player.",
            "rating": 8.5
        },
        {
            "name": "The Wire",
            "year": "2002-2008",
            "summary": "Explores the drug trade in Baltimore through the eyes of drug dealers and law enforcement officers.",
            "rating": 9.3
        },
        {
            "name": "Band of Brothers",
            "year": 2001,
            "summary": "The story of Easy Company, 506th Regiment of the 101st Airborne Division, from their training in 1942 to the end of World War II.",
            "rating": 9.4
        },
        {
            "name": "Mr. Robot",
            "year": "2015-2019",
            "summary": "A brilliant but highly unstable young cyber-security engineer and vigilante hacker suffers from social anxiety disorder and clinical depression.",
            "rating": 8.6
        }
        ]
    }
    return render(request, 'index.html', series_data)
