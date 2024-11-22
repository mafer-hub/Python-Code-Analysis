import nltk
nltk.download('popular')
from nltk.sentiment import SentimentIntensityAnalyzer



analyzer = SentimentIntensityAnalyzer()
text = "the text is here" 
sentiment = analyzer.polarity_scores(text)

print(sentiment)

#https://www.bbc.com/news/world-europe-48838438 
#An Italian court found her not guilty of endangering lives after the vessel hit a patrol boat at a quayside. Carola Rackete, who works for a charity, said her sole concern was the well-being of migrants who had been at sea for more than two weeks. The 31-year-old still faces possible charges of helping illegal immigration.

#https://www.bbc.com/news/world-europe-48809134
#Carola Rackete was arrested at the Italian port of Lampedusa after a two-week stand-off with police at sea. Her vessel, Sea-Watch 3, was banned from docking, but it eventually entered the port on Friday night. On Saturday, Mr Salvini called Ms Rackete a \"rich, white, German woman\" who had committed \"an act of war\".