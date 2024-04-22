from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)
exit = False
while exit == False:
    topic = str(input("Enter a category for trends data: "))
    pytrends.build_payload(kw_list=[topic])
    subTopics = pytrends.related_queries()
    df = pd.DataFrame(subTopics[topic]["rising"])
    print(df)
    interestOT = pd.DataFrame(pytrends.interest_over_time()).rank()
    print(topic + " was trending the most on: " + str(interestOT.index[0]))
   # print(topic + " was trending the least on: " + str(interestOT.at[interestOT.size()-1, "date"]))
    end = str(input("Ask another question? (yes or no): "))
    if end == "no":
        exit = True