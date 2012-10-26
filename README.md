
Användarmanual för TDP003 portfolio.


1: Installation

Först behöver vi Flask, såhär installerar du Flask på Ubuntu:

$ pip install Flask

Öppna zip-filen och packa upp den vart du vill.
Server filen heter tdp003.py, detta är alltså filen du ska köra.
För att köra filen, skriv detta i kommandotolken:

$ python hello.py

Kör servern i valfritt program. 


2: Lägga till information

Servern använder sig av datalagager.py för att ta ut data från json filen data.json . 
Datan är lagrad på formen:
[
  {
    "start_date": "start datum",
    "short_description": "kort beskrivning av projektet",
    "course_name": "programming in java",
    "long_description": "programming in java programming in java programming in java programming in java programming in java programming in java programming in java ",
    "group_size": 2,
    "academic_credits": "Skaparna av projektet",
    "small_image": "../static/images/Java.jpg",
    "techniques_used": [
      "python",
      "Java"
    ],
    "project_name": "Java project",
    "course_id": "TDP023",
    "end_date": "2009-04-06",
    "project_no": 1,
    "big_image": "../static/images/Java.jpg"
  }
]

"small_image" ska länka till en bild som ligger i static/images/, samma sak med "big_image"
Där varje projekt blir en ny dictionary i listan. Här kan du ändra vad du vill.